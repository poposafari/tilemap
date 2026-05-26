import json
import os
import re
import xml.etree.ElementTree as ET

EXTRACT_TARGET_KEYS = [
    "compressionlevel", "height", "infinite", "layers", "nextlayerid", "nextobjectid",
    "orientation", "renderorder", "tiledversion", "tileheight", "tilesets", "tilewidth",
    "type", "version", "width"
]

EXTRACT_INNER_KEYS = [
    "columns", "image", "imageheight", "imagewidth", "name", "tilecount",
    "tiles", "tilewidth", "tileheight", "type"
]

OUTDOOR_TILESET_NAMES = [
    "floor", "edge", "urban", "object_urban", "object", "event"
]

INDOOR_TILESET_NAMES = [
    "floor","object", "event"
]

def remove_Lx_prefix(s: str) -> str:
    return re.sub(r"^L\d+_", "", s)

def parse_tsx_animations(tsx_path: str) -> dict[int, list[dict]]:
    if not os.path.exists(tsx_path):
        return {}
    animations = {}
    tree = ET.parse(tsx_path)
    for tile_elem in tree.getroot().findall('tile'):
        anim_elem = tile_elem.find('animation')
        if anim_elem is None:
            continue
        tile_id = int(tile_elem.get('id'))
        frames = []
        for frame in anim_elem.findall('frame'):
            frames.append({
                "tileid": int(frame.get('tileid')),
                "duration": int(frame.get('duration'))
            })
        if frames:
            animations[tile_id] = frames
    return animations

def extract(file_number: str, overworld_type:str,tile_type: str):
    input_path = f"./map/before/{overworld_type}{file_number}.json"
    output_path = f"./map/after/{overworld_type}{file_number}.json"

    if tile_type == "indoor":
        TILE = INDOOR_TILESET_NAMES
    elif tile_type == "outdoor":
        TILE = OUTDOOR_TILESET_NAMES

    if not os.path.exists(input_path):
        print(f"[ERROR] {input_path} is not found!")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    extracted = {key: data[key] for key in EXTRACT_TARGET_KEYS if key in data}
    layers = data.get("layers", [])
    tilesets = data.get("tilesets", [])

    tile_maps = {}
    for tile_name in TILE:
        tile_maps[tile_name] = {
            "firstgid": 0,
            "used": set()
        }

    tsx_animations = {}

    for tile in tilesets:
        source = tile.get("source", "")
        firstgid = tile.get("firstgid")
        name = os.path.splitext(os.path.basename(source))[0]
        if name in tile_maps:
            tile_maps[name]["firstgid"] = firstgid
            tsx_path = os.path.normpath(os.path.join("./map/before", source))
            anims = parse_tsx_animations(tsx_path)
            if anims:
                tsx_animations[name] = anims

    for layer in layers:
        name = remove_Lx_prefix(layer.get("name", ""))
        map_data = layer.get("data", [])

        if name == 'foreground_0':
            continue
        if name == 'foreground_1':
            continue

        if name in tile_maps:
            tile_maps[name]["used"].update(map_data)
            tile_maps[name]["used"].discard(0)

    for tile_name in TILE:
        firstgid = tile_maps[tile_name]["firstgid"]
        adjusted_used = {tile_id - firstgid for tile_id in tile_maps[tile_name]["used"]}
        tile_maps[tile_name]["used"] = sorted(x for x in adjusted_used if x >= 0)

    extracted_tilesets = []
    for key in TILE:
        tile_file = f"./tiles/json/{tile_type}/{key}.json"
        if not os.path.exists(tile_file):
            print(f"[ERROR] {tile_file} is not found!")
            return

        with open(tile_file, "r", encoding="utf-8") as f:
            tile_data = json.load(f)

        used_ids = set(tile_maps[key]["used"])
        all_tiles = tile_data.get("tiles", [])
        filtered_tiles = [tile for tile in all_tiles if tile.get("id") in used_ids]

        animations = tsx_animations.get(key, {})
        if animations:
            existing_ids = {t["id"] for t in filtered_tiles}
            for tile in filtered_tiles:
                tid = tile.get("id")
                if tid in animations:
                    tile["animation"] = animations[tid]
            for tid, anim in animations.items():
                if tid not in existing_ids and tid in used_ids:
                    filtered_tiles.append({"id": tid, "animation": anim})

        new_tileset = {}
        for inner_key in EXTRACT_INNER_KEYS:
            if inner_key == "tiles":
                new_tileset["tiles"] = filtered_tiles
            elif inner_key in tile_data:
                new_tileset[inner_key] = tile_data[inner_key]

        new_tileset["firstgid"] = tile_maps[key]["firstgid"]
        new_tileset["name"] = f"{tile_type}_{key}"
        extracted_tilesets.append(new_tileset)

    extracted["tilesets"] = extracted_tilesets

    os.makedirs("./map/after", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)

    print(f"[SUCCESS] complete → {output_path}")

if __name__ == "__main__":
    file_number = input("input overworld idx > ").strip()
    overworld_type = input("plaza? gate? safari?(p or g or s) > ").strip()
    file_type = input("indoor? outdoor? > ").strip()
    extract(file_number,overworld_type,file_type)
