#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia 
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000 
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------    
#                             Sum                123 
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.     
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a 
# given positive integer value.
# 
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3
from __future__ import print_function

def print_abacus(value):
    row_factor = 10
    row = 9
    temp1, temp2 = 0, 0
    normal = 5
    
    while row != -1:
        if row != 9:
            print ("\n", end="")
        count = 0
        print ('|',end="")
        if value > row_factor ** row:    
        
            while value >= row_factor ** row:
                
                #print (value, row_factor, row)
                value = value - row_factor ** row
                count = count + 1
            
            if count > normal:
                #print count,normal
                temp1 = count - normal
                temp2 = 5 - temp1
                print ('0' * temp2, end="")
                print ('   ', end="")
                print ('0' * temp1, end="")
                print ('*' * normal, end="")
            
            if count <= normal:
                #print count,normal
                temp1 = normal - count
                print ('0' * normal, end="")
                print ('*' * temp1, end="")
                print ('   ', end="")
                print ('*' * count, end="")

        else: 
            print ('0' * 5, end="")
            print ('*' * 5, end="")
            print ('   ', end="")
            
        print ('|', end="")
        
        row = row - 1
        
    


###  TEST CASES
print ('\n')
print ("Abacus showing 0:")
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print ('\n')
print ("Abacus showing 12345678:")
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print ('\n')
print ("Abacus showing 1337:")
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|
