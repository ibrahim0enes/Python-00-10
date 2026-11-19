class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, growth):
        self.height += growth
        self.age += 1


if __name__ == '__main__':

    rose = Plant("Rose", 25, 30)
    print("=== Welcome to My Garden ===")
    print(f"{rose.name}: {rose.height}cm {rose.age} days old")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        print(f"{rose.name}: {rose.height:.1f}cm {rose.age} days old")
    print()
    print("=== End of Program ===")
