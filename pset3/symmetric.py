# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(some_list):
    # Your code here
    number_of_rows = len(some_list) 
    if some_list == []:
        number_of_columns = 0
    else:
        number_of_columns = len(some_list[0]) 
    
    if number_of_columns != number_of_rows: 
        return False
    i = 0
    j = number_of_columns

    while i != number_of_rows:
        
        b = 0
        while b != number_of_rows:
            
            if some_list[i][b] != some_list[b][i]:    
                return False
            
            b = b + 1
        i = i + 1
    return True
        
print symmetric([])    

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
               [2, 3, 4, 5],
              [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False