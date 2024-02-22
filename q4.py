def stack():

    return("stack", [])

def contents(stack):
   
    return stack[1]

def top(stack):
    return stack[1][-1]
    
def is_stack(obj):
    """Returns True if obj is a tuple and the first part is 'stack'."""
    return isinstance(obj, tuple) and obj[0] == 'stack'

def stack_empty(stack):
    if len(stack[1]) == 0:
        return True
    
def push(stack, e):
    stack[1].append(e)

def pops(stack):
    stack[1].pop()

def is_operator(a):
     
     if a in ['+', '-', '*', '/']:
       return True 
     else:
        return False 

def apply_operator(o,pe,pf):

    