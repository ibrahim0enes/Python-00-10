def ft_count_harvest_recursive() -> None:
    count = int(input("Days until harvest: "))

    def helper(count: int, current: int) -> None:
        if current > count:
            print("Harvest time!")
        else:
            print(f"Day {current}")
            helper(count, current+1)
    helper(count, 1)
