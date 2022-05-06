# Find Middle Number
# Given a number (n) and an array of numbers (num_list) as input to a function, 
# return True if the number is greater than the middle number of the array. 
# Return False if the number is less than the middle number of the array.
# If the array has an even amout of indexes you must decide how to handle that.

# Example Input: n = 4, array = [3,5,8, 10]
# Example Output: False
# Example Input: n = 105, array = [10,30,44,22,100]
# Example Output: True

# write a function with two inputs


def middle_number(n, num_list):
    return n > num_list[len(num_list)//2]