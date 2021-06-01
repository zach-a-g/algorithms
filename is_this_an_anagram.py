# Given two strings, check if they are anagrams, and return a boolean.

def anagram(str1, str2):
    if len(str1) != len(str2):
        return False
     
    list1 = list(str1)
    list2 = list(str2)

    for letters in list1:
        if letters not in list2:
            print(f"{str1} and {str2} are not anagrams")
            return False
        else:
            print(f"{str1} and {str2} are anagrams")
            return True

anagram("cat", "rat")
anagram("dog", "god")

# Expected outcome:
    #"god" "dog" ✅

    #"rat" "cat" 🚫