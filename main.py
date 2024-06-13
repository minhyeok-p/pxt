list2: List[number] = []
# 깎기
def cuter(x1: number, y1: number, z1: number, y1ext: number):
    blocks.fill(AIR,
        world(x1, y1, z1),
        world(x1, y1 + y1ext, z1),
        FillOperation.REPLACE)
# 실행기

def on_on_chat():
    절벽()
player.on_chat("oto", on_on_chat)

def 작은타워(x2: number, y2: number, z2: number):
    blocks.fill(SANDSTONE,
        world(x2, y2, z2),
        world(x2 + 6, y2 + 6, z2 + 6),
        FillOperation.REPLACE)
    blocks.fill(AIR,
        world(0, y2, 0),
        world(x2, y2 + 6, z2),
        FillOperation.REPLACE)
    for 값 in list2:
        pass
# 절벽 메인
def 절벽():
    blocks.replace(WATER, GRASS, world(-60, -61, -60), world(60, -63, 70))
    blocks.fill(AIR,
        world(-99, -60, -99),
        world(99, 99, 99),
        FillOperation.REPLACE)
    blocks.fill(SANDSTONE,
        world(0, -60, 0),
        world(13, -52, 27),
        FillOperation.REPLACE)
    blocks.fill(SANDSTONE,
        world(17, -60, 8),
        world(13, -52, 19),
        FillOperation.REPLACE)
    blocks.fill(SANDSTONE,
        world(0, -61, -1),
        world(8, -52, -2),
        FillOperation.REPLACE)
    blocks.fill(STONE,
        world(0, -51, 0),
        world(13, -51, 27),
        FillOperation.REPLACE)
    blocks.fill(STONE,
        world(16, -51, 8),
        world(14, -51, 19),
        FillOperation.REPLACE)
    _9block(18, -60, 12, 0, 8, 0)
    _9block(18, -60, 11, 0, 5, 0)
    _9block(2, -61, -3, 1, 8, 0)
    _9block(3, -61, -3, 3, 7, 0)
    _9block(9, -61, -1, 4, 7, 0)
    _9block(14, -60, 3, 0, 7, 5)
    _9block(14, -60, 0, 0, 9, 3)
    cuter(16, -51, 19, 1)
    cuter(16, -51, 8, 1)
    cuter(17, -52, 8, -1)
    cuter(17, -52, 19, -2)
    cuter(17, -52, 18, -1)
    cuter(0, -52, -2, -1)
def _9block(x12: number, y12: number, z12: number, x1ext2: number, y1ext2: number, z1ext2: number):
    blocks.fill(SANDSTONE,
        world(x12, y12, z12),
        world(x12 + x1ext2, y12 + y1ext2, z12 + z1ext2),
        FillOperation.REPLACE)