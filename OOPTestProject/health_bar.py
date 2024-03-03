import os

os.system("")

class HealthBar:
    symbol_remaining: str = "[]"
    symbol_lost: str = "_"
    barrier: str = "|"
    colors: dict = {"red": "\033[91m",
                    "green": "\033[92m",
                    "default": "\033[0m"}
    def __init__(self,
                 entity,
                 length: int =20,
                 is_colored: bool = True,
                 color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.maxhp
        self.current_value = entity.health

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw(self) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"{self.entity.name}'s HEALTH: {self.entity.health}/{self.entity.maxhp} ")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")

