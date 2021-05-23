## 5. FizzBuzz
# A classic; write a program that prints out a sequential string of numbers.
# If divisible by 3, output `"Fizz`.
# If divisible by 5, output `"Buzz`.
# If divisible by both 3 and 5, output `FizzBuzz`.
# Otherwise, print out the string.

# Between 1 and 5, output:
# "1"
# "2"
# "Fizz"
# "4"
# "Buzz"
# ```

def fizz_buzz(num):
    for n in range (num + 1):
        if (n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(str(n))

fizz_buzz(100)