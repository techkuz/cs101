# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True 
# if the given square is antisymmetric and False otherwise. 
# An nxn square is called antisymmetric if A[i][j]=-A[j][i] 
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.


def antisymmetric(A):
    # Your code here
    number_of_rows = len(A) 
    if A == []:
        number_of_columns = 0
    else:
        number_of_columns = len(A[0]) 
    
    if number_of_columns != number_of_rows: 
        return False
    i = 0
    j = number_of_columns

    while i != number_of_rows:
        
        b = 0
        while b != number_of_rows:
            
            if A[i][b] != -1 * A[b][i]:    
                return False
            
            b = b + 1
        i = i + 1
    return True
        
        
        
        

# Test Cases:

print antisymmetric([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])   
#>>> True

print antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]])
#>>> True

print antisymmetric([[0, 1, 2], 
                     [-1, 0, -2], 
                     [2, 2,  3]])
#>>> False

print antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]])
#>>> False


