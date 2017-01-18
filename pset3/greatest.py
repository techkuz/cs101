# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    
    if list_of_numbers != []:
        temp = list_of_numbers[0]
        i = 0
        while i != len(list_of_numbers) - 1:
            
            if temp < list_of_numbers[i + 1]:
                temp = list_of_numbers[i + 1]
            i = i + 1
        return temp
        
    return 0
                




#        return max(list_of_numbers)
#    else:
#        return 0


print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0