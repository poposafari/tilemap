import json
import os

file_mapping = {
    "1": "floor.json",
    "2": "edge.json",
    "3": "object.json",
    "4": "object_urban.json",
    "5": "urban.json"
}

def start():
    file_choice = input("1~5 중에서 JSON 파일 선택 (1: floor, 2: edge, 3: object, 4: object_urban, 5: urban): ").strip()
    suffix_number = input("정수값을 입력하세요 (예: 1): ").strip()
    tile_ids_str = input("사용할 타일 ID들을 입력하세요 (예: 0,1,2,10,30,...): ").strip()

    file_name = file_mapping.get(file_choice)
    if not file_name:
        print("잘못된 번호")
        return

    file_path = os.path.join(os.getcwd()+'/json', file_name)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"JSON 파일 읽기 실패: {e}")
        return

    base_keys = [
        "columns", "image", "imageheight", "imagewidth", "margin", "name",
        "spacing", "tilecount", "tiledversion", "tileheight", "tilewidth",
        "transparentcolor", "type", "version"
    ]
    result = {key: data[key] for key in base_keys if key in data}
    result["firstgid"] = 1

    try:
        tile_ids = sorted(set(int(x.strip()) for x in tile_ids_str.split(',') if x.strip().isdigit()))
    except ValueError:
        print("타일 ID 형식 오류")
        return

    original_tiles = data.get("tiles", [])
    filtered_tiles = [tile for tile in original_tiles if tile["id"] in tile_ids]
    result["tiles"] = filtered_tiles

    output_dir = os.path.join(os.getcwd(), "result")
    os.makedirs(output_dir, exist_ok=True)
    output_file_name = f"overworld-{suffix_number}_{file_name.replace('.json', '')}.json"
    output_path = os.path.join(output_dir, output_file_name)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"저장 완료: {output_path}")

if __name__ == "__main__":
    start()