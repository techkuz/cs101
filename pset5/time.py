import time

def time_execution(some_code):
    start = time.clock()
    result = eval(some_code)
    run_time = time.clock() - start
    return result, run_time
    
def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1
        
        
print(time_execution('spin_loop(1000)'))