
# Almost sorted
# Difficulty: Medium

def almostSorted(arr):
    arr_sorted = sorted(arr)
    count = 0
    first = last = None
    for key, value in enumerate(arr):
        
        if value != arr_sorted[key]:
            count += 1
            if first is None:
                first = key
            else:
                last = key

    if count == 0:
        print("yes")
        return
    elif count == 2:
        if arr[first] == arr_sorted[last] and arr[last] == arr_sorted[first]:
            print("yes")
            print(f"swap {first+1} {last+1}")
            return
    elif count > 2:
        arr_new = arr[first:last+1]
        arr_new.reverse()
        if arr_new == arr_sorted[first:last+1]:
            print("yes")
            print(f"reverse {first+1} {last+1}")
            return
    
    print("no")

if __name__ == "__main__":
    almostSorted([1,5,4,3,2,6])