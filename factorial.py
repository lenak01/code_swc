def dna_starts_with(st1, st2):
    '''Returns True if str1 starts with str2
    >>> dna_starts_with('acgtgtcgat', 'acgtgtcgat')
    True
    >>> dna_starts_with('acgtgtcgat', 'a')
    True
    >>> dna_starts_with('acgtgtcgat', 'acgtgtcgatacgtgtcgat')
    False
    '''
    return st1[0:len(st2)]==st2
    

def factorial(n):
    '''Returns the factorial of an integer n>=0
    Simple test
    >>> factorial(4)
    24

    Non-integer
    >>> factorial(4.1)
    Traceback (most recent call last):
    ...
    ValueError: n must be an integer
    ''' 
    if not n>=0:
        raise ValueError('n must be >= 0')
    if type(n) != int:
        raise ValueError('n must be an integer')
    result = 1
    factor = 2
    while factor<=n:
        result *= factor
        factor += 1
    return result
if __name__ == '__main__':
    import doctest
    doctest.testmod()

