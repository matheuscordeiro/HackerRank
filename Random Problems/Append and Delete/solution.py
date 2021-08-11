YES = "Yes"
NO = "No"

def appendAndDelete(s, t, k):
    if k >= len(s) + len(t):
        return YES

    i = j = 0
    while i < len(s) and j < len(t) and s[i] == t[j]:
        i += 1
        j += 1

    moves_delete = len(s) - i
    moves_append = len(t) - j
    if moves_delete + moves_append > k:
        return NO
    elif moves_delete + moves_append == k:
        return YES
    elif (k % 2 == 0 and (moves_append + moves_delete) % 2 == 0) or  (k % 2 != 0 and (moves_append + moves_delete) % 2 != 0): 
        return YES
    else:
        return NO

    
if __name__ == "__main__":
    s = "yu"
    t = "y"
    print(appendAndDelete(s,t,2))