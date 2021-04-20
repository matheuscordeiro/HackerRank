# Balanced Queries
# Difficulty: medium


brackets = {
    "(": ")",
    "{": "}",
    "[": "]"
}

def isBalanced(s):
    stack = []
    for bracket in s:
        if brackets.get(bracket):
            stack.append(bracket)
        elif not stack:
            return "NO"
        elif brackets.get(stack.pop()) != bracket:
            return "NO"

    return "YES" if not stack else "NO"


if __name__ == "__main__":
    print(isBalanced("{{[[(())]]}}"))

