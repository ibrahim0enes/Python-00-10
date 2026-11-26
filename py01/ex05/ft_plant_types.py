class Plant:
    def __init__(self, name, height, age):
        self._name = name
        self._height = float(height)
        self._age = age
        print(f"Plant created: {self.name}: {self._height}cm, {self._age} days old")

    def show(self):
        name = self._name.capitalize()
        print(f"{name} : {height}cm, {age} days old")

    def grow(self, amount : float):
        self._height += amount

    def age(self, days: int) -> None:
        self._current_age += days

    class Flower (Plant):
        def __init__(self, name , height, age , color):
            super().__init__(name, height, current_age)
            self._color = color
            self._is_bloomed = false

    def bloom(self):
        print("[asking the rose to bloom]")
        self._is_bloomed = True
    
    
    class Tree (Plant):

    def produce_shade(): 

    class Vegetable (Plant):


    


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    