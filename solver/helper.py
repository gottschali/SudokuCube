starting_points = {0: "middle",
                   1: "center",
                   2: "edge",
                   3: "corner"}

dirs = {"x": ["left", "right"],
              "y": ["front", "back"],
              "z": ["up", "down"]
        }

def human(partial):
    """ Gives human understandable directions to solve the cube """
    dice_order = sorted(partial.items(), key=lambda i: i[1][1]) # Sort by index
    print(f"starting point: {starting_points[sum(map(abs, dice_order[0][0]))]}")
    def direction(ca, cb):
        
        for d, a, b in zip(("x", "y", "z"), ca, cb):
            if (a > b) or (b > a):
                return dirs[d][a > b]
    for i in range(len(dice_order) - 1):
        print(f"({dice_order[i + 1][1][0].name}) -> {direction(dice_order[i][0], dice_order[i + 1][0])}")
