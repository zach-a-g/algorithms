# Algos
# 1. Bubble Sort
# Write a program to sort a list of numbers in ascending order, comparing and swapping two numbers at a time.
# Normal to see on an interview question

def bubble_sort(list_a):
    indexing_length = len(list_a) - 1 
    sorted = False # local variable
    while not sorted:
        sorted = True 
        for i in range(0, indexing_length): # loop
            if list_a[i] > list_a[i+1]: # [i] means number to the left and [i+1] is the value to the right
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] # This line flips the numbers to be in the correct order.+
                print(list_a)

print(bubble_sort([6,3,4,1,2,5]))
# [1,2,3,4,5,6]