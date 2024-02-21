 
array = [1,3,4,5]

def rec(array):
    if len(array) == 0:
        return []
    else:  
   
        return (array[0] + 1)  + rec(array[1:])


print(rec(array))