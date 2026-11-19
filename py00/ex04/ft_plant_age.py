def ft_plant_age() -> None:
    plant_age = int(input("Enter plant age in days: "))
    print(f"Plant age: {plant_age} days")
    if plant_age < 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
