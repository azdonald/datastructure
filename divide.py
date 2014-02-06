'''
This function implements the divide functionality 
without using the divide operator
'''

def divide(a,b):
    count = 0
    remainder = 0
    while a > b or a == b:
        a = a - b
        count = count + 1
    if a < b:
        remainder = a
    return count,remainder
