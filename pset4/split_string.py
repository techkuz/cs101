# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source,splitlist):
    
    
    i = 0
    splitted_symbols = []
    while i != len(splitlist):
        splitted_symbols.append(splitlist[i])
        i = i + 1
    
    resulting_list = []
    
    for entry in splitted_symbols:
        b = 0
        start_loc = 0
        if resulting_list == []:
            
            while b != len(source):
                
                if source[b] == entry:
                    
                    resulting_list.append(source[start_loc:b])
                    start_loc = b + 1
                    b = b + 1
                    
                
                elif b == len(source) - 1:
                    resulting_list.append(source[start_loc:])
                    b = b + 1
                    
                
                elif source[b] != entry:
                    b = b + 1
    
        
        
        if resulting_list != []:
            for index, d in enumerate(resulting_list):
                
                b = 0
                while b != len(d):
                    
                    if d[b] == entry:
                        
                        if b == len(d) - 1: 
                            resulting_list[index] = d[:b]
                            b = b + 1
                        
                        else: 
                            resulting_list.insert(index + 1, d[b + 1:])
                            resulting_list[index] = d[:b]
                            b = b + 1
                
           
                    elif d[b] != entry:
                        b = b + 1
    
  
    return resulting_list    
        
     

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']