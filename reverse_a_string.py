# Reverse a string

def reverse_a_string(string):
    new_string = ''
    index = len(string)
    while index:
        index -= 1                    
        new_string += string[index] 
    return new_string

print(reverse_a_string("Hello World!"))


# Different way
def reversed_string(a_string):
    return a_string[::-1]

print(reversed_string('Hello World'))
