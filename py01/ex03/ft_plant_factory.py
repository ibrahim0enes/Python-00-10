class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name} : {self.height:.1f}cm, {self.age} days old")


if __name__ == '__main__':
    Rose = Plant("Rose", 25, 30)
    Oak = Plant("Oak", 200, 365)
    Cactus = Plant("Cactus", 5, 90)
    Sunflower = Plant("Sunflower", 80, 45)
    Fern = Plant("Fern", 15, 120)

    Rose.show()
    Oak.show()
    Cactus.show()
    Sunflower.show()
    Fern.show()
