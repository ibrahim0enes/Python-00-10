def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if seed_type == "Tomato":
        print(f"{seed_type}: {quantity} {unit} available")
    elif seed_type == "Carrot":
        print(f"{seed_type}: {quantity} {unit} total")
    elif seed_type == "Lettuce":
        print(f"{seed_type}: covers {quantity} {unit} square meters")
    else:
        print("Unknown unit type")
