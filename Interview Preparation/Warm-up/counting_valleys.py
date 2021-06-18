def countingValleys(steps, path):
    total = hike = LEVEL_SEA = 0
    from_down = False
    for step in path:
        if step == "D":
            hike -= 1
        elif step == "U":
            hike += 1

        if hike == LEVEL_SEA and from_down:
            total += 1
            from_down = False
        elif hike < LEVEL_SEA:
            from_down = True

    return total


if __name__ == "__main__":
    print(countingValleys(8, ["U", "D", "D", "D", "U", "D", "U", "U"]))
