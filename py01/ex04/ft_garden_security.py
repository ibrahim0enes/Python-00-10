class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = float(height)
        self._age = age
        print(f"Plant created: {self.name}: {self._height}cm, {self._age} days old")

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print()

    rose.set_height(25)
    print(f"Height updated: {int(rose.get_height())}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days")
    print()

    rose.set_height(-5)
    rose.set_age(-5)

    print()
    print(f"Current state: {rose.name}: {rose.get_height()}cm, {rose.get_age()} days old")
