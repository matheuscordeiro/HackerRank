def update_alphabet(rotation, character, max_value, min_value, alphabet):
    position = ord(character) + rotation
    if position > max_value:
        alphabet[character] = chr(position-max_value-1+min_value)
    else:
        alphabet[character] = chr(position)


def caesarCipher(s, k):
    MAX_LOWER = ord("z")
    MIN_LOWER = ord("a")
    MAX_UPPER = ord("Z")
    MIN_UPPER = ord("A")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_lower = {}
    alphabet_upper = {}
    if k > MAX_LOWER-MIN_LOWER+1:
        k = k % (MAX_LOWER-MIN_LOWER+1)
        
    for character in alphabet:
        update_alphabet(k, character, MAX_LOWER, MIN_LOWER, alphabet_lower)
        update_alphabet(k, character.upper(), MAX_UPPER, MIN_UPPER, alphabet_upper)

    name = ""
    for character in s:
        if character in alphabet_lower:
            name += alphabet_lower[character]
        elif character in alphabet_upper:
            name += alphabet_upper[character]
        else:
            name += character

    return name


if __name__ == "__main__":
    print(caesarCipher("There's-a-", 3))
