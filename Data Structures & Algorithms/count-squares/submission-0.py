class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        x, y = point

        self.points[(x, y)] = self.points.get((x, y), 0) + 1

    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0

        for (px, py), freq in self.points.items():

            if px == x or py == y:
                continue

            if abs(x - px) != abs(y - py):
                continue

            corner1 = (x, py)
            corner2 = (px, y)

            result += (
                freq * self.points.get(corner1, 0) * self.points.get(corner2, 0)
            )

        return result
