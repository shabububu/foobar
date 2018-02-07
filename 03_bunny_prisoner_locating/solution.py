def consecutive_sum(n):
    return (n*(n+1)/2)
    
def answer(x, y):
    """
    See readme.txt for problem description
    
    Input: (int) x, y coordinates for your bunny cells
    Output: (str) ID of the bunny.
    
    Okay, as I draw this out, I'm seeing a patern.
    I don't know if it's the best pattern, but I'm
    going to run with it here...
    
    22
    16 23
    11 17 24
    7  12 18 25
    4  8  13 19 26
    2  5  9  14 20 27
    1  3  6  10 15 21 28
    
    Going across the x-axis:
    The bottom row (y=1) looks like the sum of n consecutive
    numbers starting from 1 to x. (Or, x(x+1)/2)
    This is what I call the base in my code.
    
    Going up the y-axis:
    As you increase y, it's a different sum of consecutive
    numbers that starts at x and continues until
    (x-1)+(y-1). So, to find this sum, you can take the
    sum of consecutive numbers from 1..(x-1)+(y-1). Then,
    subtract from it, the sum of consecutive numbers from
    1..(x-1).
    
    Once you combime these two sets of consecutive numbers,
    you'll have the ID to these annoying little bunnies...
    """
    base = consecutive_sum(x)
    vertical = consecutive_sum((y-1)+(x-1)) - consecutive_sum(x-1)
    return str(base + vertical)
