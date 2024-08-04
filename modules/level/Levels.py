from os import walk

levelsAmount: int = len(next(walk("../../levels/"))[1]) - 2
# We subtract 2 folders made by tiled (External CSV Level editor).

levelsInfo = []
overworldInfo = []
levels = {}
# We load the layouts for all levels.
for i in range(levelsAmount):
    levelsInfo.append({
        "background": f"../levels/{i}/level_{i}_background.csv",
        "boxes": f"../levels/{i}/level_{i}_boxes.csv",
        "coins": f"../levels/{i}/level_{i}_coins.csv",
        "constraints": f"../levels/{i}/level_{i}_constraints.csv",
        "constraints2": f"../levels/{i}/level_{i}_constraints2.csv",
        "constraints3": f"../levels/{i}/level_{i}_constraints3.csv",
        "enemies": f"../levels/{i}/level_{i}_enemies.csv",
        "lucky_blocks": f"../levels/{i}/level_{i}_lucky_blocks.csv",
        "decoration": f"../levels/{i}/level_{i}_windows_and_doors.csv"
    })
# We set up the overworld nodes for each level.
for i in range(levelsAmount):
    multiplier: float = 0.5
    if i % 2 == 0:
        multiplier = 2
    overworldInfo.append({
        "nodePos": (110 * (i * multiplier), 400 * (i * multiplier)),
        "content": levelsInfo[i],
        "unlock": i,
        "nodeAssets": f"../../assets/menu/overworld/{i}.png"
    })

# We assign a key for every level.
for i in range(levelsAmount):
    levels.update({i: overworldInfo[i]})

if __name__ == "__main__":
    print(f"Levels Amount: {levelsAmount}")
    print("Each level overworld info:")
    for i in range(levelsAmount):
        print("===========================")
        print(f"Level: {i}")
        print(overworldInfo[i])
        print(f"Level info: {overworldInfo[i].get('content')}")
        print("===========================")
