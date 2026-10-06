class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_in_days = age

    def grow(self, amount: float = 1.0) -> None:
        self.height += amount

    def age(self, days: int = 1) -> None:
        self.age_in_days += days

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age_in_days} days old"
        )


def main() -> None:
    plants = (
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    )

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
