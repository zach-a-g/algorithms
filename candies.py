# 2. Candies
# Given the list `candies` and the integer `extra_candies`, where `candies[i]` represents the number of candies that the `ith` kid has.
# For each kid, check if there is a way to distribute the `extra_candies` amount to the kids such that they can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

candies = [2,3,5,1,3]
extra_Candies = 3

def kidsWithCandies():
    ans = []
    max_candies = max(candies)
    for kid in candies:
        if kid + extra_Candies >= max_candies:
            ans.append(True)
        else:
            ans.append(False)
        print(ans)

print(kidsWithCandies())

# expected output: [True,True,True,False,True