def sum_multi():
    """
    Sum of multiples of 3 and 5 below 1000
    """
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)  
    