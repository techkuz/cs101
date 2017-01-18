# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    result_list = []
    n = 0
    result_list.append(int(string[:1]))
    temp_list = []
    compare = 0
    
    for i in string[1:]:
          
        if compare != 0:
            print '!=0 ' + compare, i, temp_list, string[n:n+1] 
            
            if i <= compare:
                temp_list.append(int(i))
                
            if i > compare:
                result_list.append(temp_list)  
                temp_list = []
                result_list.append(int(i))
                compare = 0
                
        else:
            print compare, i, temp_list, string[n:n+1] 
            
            
            if i <= string[n:n+1]:
                
                compare = i
                temp_list.append(int(i))
                    
            else:
                
                if temp_list != []:
                    result_list.append(temp_list)  
                    temp_list = []
                result_list.append(int(i))
                
        n = n + 1
    
    if temp_list != []:
        result_list.append(temp_list)
    print result_list 
    return result_list

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
