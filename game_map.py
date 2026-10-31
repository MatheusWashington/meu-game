
from pygame import Rect


class GameMap:
    def __init__(self):
        self.tile_size = 40
        self.exit_rect = Rect(720, 520, 40, 40)

        self.layout = [
            "####################",
            "#..................#",
            "#..####....####....#",
            "#..................#",
            "#....####....####..#",
            "#..................#",
            "#.####....####....##",
            "#..................#",
            "#....####....####..#",
            "#..................#",
            "#.####....####....##",
            "#..................#",
            "#....####....####..#",
            "#..................#",
            "####################"
        ]

    def draw(self, screen):
        for row_index, row in enumerate(self.layout):
            for column_index, tile in enumerate(row):
                x = column_index * self.tile_size
                y = row_index * self.tile_size

                if tile == "#":
                    screen.draw.filled_rect(
                        Rect(x, y, self.tile_size, self.tile_size),
                        (45, 50, 65)
                    )

        screen.draw.filled_rect(
            self.exit_rect,
            (0, 118, 110)
        )
        screen.draw.text(
            "EXIT",
            center=self.exit_rect.center,
            color="white"
        )

    def is_walkable(self, x, y):
        column = int(x // self.tile_size)
        row = int(y // self.tile_size)

        if row < 0 or row >= len(self.layout):
            return False

        if column < 0 or column >= len(self.layout[row]):
            return False

        return self.layout[row][column] == "."
