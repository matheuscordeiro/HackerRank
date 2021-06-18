def sockMerchant(n, ar):
    colors = {}
    pairs = 0
    for _, color in enumerate(ar):
        if color in colors:
            pairs += 1
            del colors[color]
        else:
            colors[color] = True

    return pairs


if __name__ == "__main__":
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sockMerchant(9, ar))