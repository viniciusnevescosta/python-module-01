class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._statistics = self.Statistics()
        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return False
        self._height = height
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return False
        self._age = age
        return True

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name

    def grow(self, amount: float = 1.0) -> None:
        self.set_height(self._height + amount)
        self._statistics.record_grow()

    def age(self, days: int = 1) -> None:
        self.set_age(self._age + days)
        self._statistics.record_age()

    def show(self) -> None:
        self._statistics.record_show()
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._age} days old"
        )

    def display_statistics(self) -> None:
        self._statistics.display()


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_blooming:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    class Statistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._tree_statistics = self.Statistics()
        self._statistics = self._tree_statistics

    def produce_shade(self) -> None:
        self._tree_statistics.record_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{round(self._trunk_diameter, 1)}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = 0

    def bloom(self, seed_count: int = 42) -> None:
        super().bloom()
        self._seed_count = seed_count

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_statistics()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(
        "Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        "Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )
    print()

    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print()

    oak = Tree("Oak", 200.0, 365, 5.0)
    print("=== Tree")
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print()

    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    print("=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print()

    anonymous = Plant.create_anonymous()
    print("=== Anonymous")
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
