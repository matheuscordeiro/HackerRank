# Fraudulent Activity Notifications
# Difficulty: medium

# Credits: https://www.thepoorcoder.com/hackerrank-fraudulent-activity-notifications-solution/

def get_median_2x(count_array, d):
    count_numbers = 0
    ref1, ref2 = d//2, d//2 + 1
    a = b = 0
    for key, value in enumerate(count_array):
        count_numbers += value
        if ref1 <= count_numbers and not a:
            a = key
        if ref2 <= count_numbers:
            b = key
            break

    return b*2 if d%2 else a+b


def activityNotifications(expenditure, d):
    notifications = 0
    count_array = [0]*201
    for i in range(d):
        count_array[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        median = get_median_2x(count_array, d)
        if expenditure[i] >= median:
            notifications += 1

        if i == len(expenditure)-1:
            break

        count_array[expenditure[i-d]] -= 1
        count_array[expenditure[i]] += 1

    return notifications


if __name__ == "__main__":
    array = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    print(activityNotifications(array, 5))
