
less_than = lambda x, y: True if x < y else False
greater_than = lambda x, y: True if x > y else False

def insert(el, pred, lst):
    if lst == []:
        return [el]
    elif pred(el, lst[0]):
        return [el] + lst
    else:
        return [lst[0]] + insert(el, pred, lst[1:])

# Test cases
print(insert(10, less_than, [2, 3, 7, 9]))    
print(insert(10, greater_than, [11, 9, 7, 8]))  