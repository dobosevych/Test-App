def is_prime(n):
    """
    Checks is integer prime.
    :param n: the positive integer number.
    :return: result of prime validation.
    
    >>> is_prime(10)
    False
    >>> is_prime(11)
    True
    """
    import math
    for i in range(int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True




