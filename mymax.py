#These are my MyMax Funtions:

def maxoftwo(x,y):
    """Gets the max of two"""
    if x > y:
        return x
    elif y > x:
        return y
    else:
        print('The numbers are equal')

def maxofthree(x,y,f):
    """Gets the max of three"""
    if x > y and x > f:
        return x
    elif y > x and y > f:
        return y
    elif f > x and f > y:
        return f
    else:
        print('The numbers are equal')


def listMax(list):
    """Gets the max of a list plus the index"""
    x = max(list)
    y = list.index(x)
    return x, y


#end