import numpy as ny

# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

input_array_ex1 = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
reversed_arr = input_array_ex1[::-1]
print(reversed_arr)

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]

input_array1_ex2 = [0, 10, 20, 40, 60]
input_array2_ex2 = [10, 30, 40]

isin_result = ny.isin(input_array1_ex2, input_array2_ex2)
print(isin_result)

# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]

input_array1_ex3 = [1,6,4,8,9,-4,-2,11]
result_max_ex3 = ny.max(input_array1_ex3)
result_min_ex3 = ny.min(input_array1_ex3)
print(result_max_ex3)
print(result_min_ex3)

# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...
