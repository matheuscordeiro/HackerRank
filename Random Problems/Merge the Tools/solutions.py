def merge_the_tools(string, k):
    substrings = int(len(string)/k)
    size_substring = int(len(string)/substrings)
    count = 0
    frequency = {}
    word = ""
    for value in string:
        count += 1
        if not value in frequency:
            word += value
            frequency[value] = True
        
        if count == size_substring:
            print(word)
            word = ""
            count = 0
            frequency = {}

if __name__ == "__main__":
    merge_the_tools("AABCAAADA", 3)