QTD_CONDITIONS = 4
MIN_LENGTH = 6

def minimum_number(password):
    numbers = dict.fromkeys("0123456789", True)
    lower_case = dict.fromkeys("abcdefghijklmnopqrstuvwxyz", True)
    upper_case = dict.fromkeys("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True)
    special_characters = dict.fromkeys("!@#$%^&*()-+", True)

    conditions = 0
    frequency = {"numbers": False, "lower_case": False, "upper_case": False, "special_characters": False}
    for character in password:
        if character in numbers and not frequency.get("numbers"):
            frequency["numbers"] = True
            conditions += 1
        elif character in lower_case and not frequency.get("lower_case"):
            frequency["lower_case"] = True
            conditions += 1
        elif character in upper_case and not frequency.get("upper_case"):
            frequency["upper_case"] = True
            conditions += 1
        elif character in special_characters and not frequency.get("special_characters"):
            frequency["special_characters"] = True
            conditions += 1
    
    return max(QTD_CONDITIONS - conditions, MIN_LENGTH - len(password))
    

if __name__ == "__main__":
    print(minimum_number("2opeaz"))
    print(minimum_number("2bb#A"))
    print(minimum_number("Ab1"))
    print(minimum_number("1"))
    print(minimum_number("1oPe@z"))
    print(minimum_number("aaaaa"))