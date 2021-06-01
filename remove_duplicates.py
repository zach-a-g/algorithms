# Given a string of letters and / or numbers, remove all duplicates and return the new string. 
# Study the example carefully. 
# Please avoid any special built in methods or operators (Set).

# Version1:
def duplicates(string):
    checked = ""
    previousChar = None
    for currentChar in string:
        if currentChar != previousChar:
            checked += currentChar
            previousChar = currentChar
    return checked.title()

print(duplicates("Loops are cool!"))

# Version 2:
def duplicates2(string):
    scanned = set()
    checked = ""
    for currentChar in string:
        if currentChar not in scanned:
            scanned.add(currentChar)
            checked += currentChar
    return checked.title()

print(duplicates2("Loops are cool!"))


# Expected outcome =
#   "Loops are cool!!"
#   "Lops are cl!"