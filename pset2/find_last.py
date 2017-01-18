# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and returns the last position in the search string
# where the target string appears, or -1 if there
# are no occurrences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(search_string, target_string):
    value_search = 0
   
    final_value = 0
    
    search_begin = 0
    
    value_search = search_string.find(target_string)
    if value_search == -1:
        return -1
    if value_search != -1:
        final_value = value_search
        while search_begin != -1:
            
            value_search = search_string.find(target_string, value_search + 1)
            search_begin = value_search
        
            if search_begin != -1:
                final_value = value_search
            
    
    return final_value
        
    





print find_last('aaaa', 'a')
#>>> 3

print find_last('aaaaa', 'aa')
#>>> 3

print find_last('aaaa', 'b')
#>>> -1

print find_last("111111111", "1")
#>>> 8

print find_last("222222222", "")
#>>> 9

print find_last("", "3")
#>>> -1

print find_last("", "")
#>>> 0

print find_last('ccabccdddbcbacadaddabbbdddaacb', 'dab')