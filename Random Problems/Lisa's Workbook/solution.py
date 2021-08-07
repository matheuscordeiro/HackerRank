def workbook(n, k, arr):
    special = current_page = 0
    for value in arr:
        problems_per_page = 0
        current_page += 1
        for i in range(value):
            problems_per_page += 1
            if i + 1 == current_page:
                special += 1

            if problems_per_page == k:
                problems_per_page = 0
                if i != value-1:
                    current_page += 1

    return special

if __name__ == "__main__":
    print(workbook(5, 3, [4, 2, 6, 1, 10]))

