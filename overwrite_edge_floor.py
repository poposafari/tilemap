import shutil
from pathlib import Path

MAP_DIR = Path(__file__).parent / "map"
SOURCE_DIR = MAP_DIR / "p000"
FILES_TO_COPY = ["edge.tsx", "floor.tsx"]

EXCLUDE = {f"p{str(i).zfill(3)}" for i in range(2, 10)}

targets = sorted(
    d for d in MAP_DIR.iterdir()
    if d.is_dir() and d.name != "p000" and d.name not in EXCLUDE
    and d.name[0] in ("p", "s") and d.name[1:].isdigit()
)

for target in targets:
    for filename in FILES_TO_COPY:
        src = SOURCE_DIR / filename
        dst = target / filename
        shutil.copy2(src, dst)
        print(f"{dst.relative_to(MAP_DIR)}")

print(f"\nDone: {len(FILES_TO_COPY)} files copied to {len(targets)} directories.")
