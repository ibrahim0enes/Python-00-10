class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = float(height)
        self._age = age
        print(
            f"Plant created: {self._name}: "
            f"{self._height}cm, {self._age} days old"
        )

    def show(self):
        name = self._name.capitalize()
        print(
            f"{name}: {self._height}cm, "
            f"{self._age} days old"
        )

    def grow(self, amount: float) -> None:
        self._height += amount

    def age(self, days: int) -> None:
        self._age += days


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._is_bloomed = False

    def bloom(self):
        self._is_bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")

        if self._is_bloomed:
            print(f"{self._name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self._name.capitalize()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = float(trunk_diameter)

    def produce_shade(self):
        print(f"[asking the {self._name} to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and "
            f"{self._trunk_diameter}cm wide."
        )

    def show(self):
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self, amount: float) -> None:
        super().grow(amount)
        self._nutritional_value += 1

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("rose", 15, 10, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print()
    print("=== Tree")
    oak = Tree("oak", 200, 365, 5)
    oak.show()

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print()
    print("=== Vegetable")
    tomato = Vegetable("tomato", 5, 10, "April")
    tomato.show()

    print("[make tomato grow and age for 20 days]")
    tomato.grow(2)
    tomato.age(20)
    tomato.show()