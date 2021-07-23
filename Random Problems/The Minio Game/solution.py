def minion_game(string):
    vowels = {"A": True, "E": True, "I": True, "O": True, "U": True}
    kevin = stuart = 0
    for key, value in enumerate(string):
        if value in vowels:
            kevin += len(string) - key
        else:
            stuart += len(string) - key

    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")

if __name__ == "__main__":
    minion_game("BANANA")