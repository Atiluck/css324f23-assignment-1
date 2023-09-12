def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    # Pour from one to another but possible only pour until the source bottle is empty or until the destination bottle is full.
    t = 8-x
    if ( y > 0 or z > 0 ) and t > 0: 
    # From 5 or 3 Liters to 8 Liters
        if y < t: 
            yield ((x+y, 0, z), y)
        if z < t:
            yield ((x+z, y, 0), z)  
    t = 5-y
    if ( x > 0 or z > 0 ) and t > 0: 
    # From 8 or 3 Liters to 5 Liters
        if x > t:
            yield ((x-t, 5, z), t)
        else:
            yield ((0, x+y, z), x)
        if z < t:
            yield ((x, y+z, 0), z)  
    t = 3-z
    if ( x > 0 or y > 0 ) and t > 0:
    # From 8 or 5 Liters to 3 Liters
        if x > t:
            yield ((x-t, y, 3), t) 
        else:
            yield ((0, y, x+z), x)
        if y > t:
            yield ((x, y-t, 3), t)  
        else:
            yield ((x, 0, y+z), y)  
    return s
