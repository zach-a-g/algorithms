## 3. Shuffle
# Given a string `s` and an integer list of `indices` of the same length, shuffle the string such that the character at the `ith` position moves to `incices[i]`.
# Return the shuffled string.

s = "odce"
indices = [1,2,0,3]
def unshuffle(string, indices):
    print(indices)
    print(string)
    n = len(indices)
    returnString = ""
    for i in range(n):
        for j in range(n):
            if indices[j] == i:
                returnString = returnString + string[j]
    return returnString

print(unshuffle(s, indices))


# return "code"