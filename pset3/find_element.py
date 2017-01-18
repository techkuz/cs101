# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.


def find_element(list1, value):
    
    for i in list1:
        p = str(i).find(str(value))
        #print p
        #print list1[i-1]
        #print i
        if p != -1:
            return list1.index(value)
    return -1


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1