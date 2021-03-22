from constant import COLOR_MAP

starting_points_map = {(0, 0, 0): "middle",
                       (0, 0, 1): "center",
                       (0, 1, 1): "edge",
                       (1, 1, 1): "corner"}

def human_step_by_step(sudoku_map):
    dice_order = sorted(sudoku_map.items(), key=lambda i: i[1].index)
    start = dice_order[0][0].coords
    print(f"starting point: {starting_points_map[start]}")
    def direction(coord_a, coord_b):
        if coord_a.x > coord_b.x:
            return "left"
        if coord_a.x < coord_b.x:
            return "right"
        if coord_a.y > coord_b.y:
            return "front"
        if coord_a.y < coord_b.y:
            return "back"
        if coord_a.z > coord_b.z:
            return "up"
        if coord_a.z < coord_b.z:
            return "down"
    for i in range(len(dice_order) - 1):
        print(f"({COLOR_MAP[dice_order[i + 1][1].color]}) -> {direction(dice_order[i][0], dice_order[i + 1][0])}")

