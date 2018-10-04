class RdMaze:

    def __init__(self, map):
        self.map = map
        print("Dice mazes init")

    def roll_dice(self):
        print("Roll dice")

if __name__ == "__main__":
    dice_mazes = RdMaze("map")
    dice_mazes.roll_dice()
