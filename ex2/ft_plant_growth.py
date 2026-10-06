class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float,
    ) -> None:
        self.name = name
        self.height = height
        self.age_in_days = age
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.age_in_days += 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age_in_days} days old"
        )


def main() -> None:
    rose = Plant("Rose", 25.0, 30, 0.8)
    starting_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()

    weekly_growth = round(rose.height - starting_height, 1)
    print(f"Growth this week: {weekly_growth}cm")


if __name__ == "__main__":
    main()
