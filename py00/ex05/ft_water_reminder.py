def ft_water_reminder() -> None:
    days_since_watering = int(input("Days since last watering: "))
    if days_since_watering <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
