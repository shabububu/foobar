def generous_lamb_generator():
    """
    Returns a sequence of numbers, where the next element
    doubles the value of its predecessor.
    The sequence starts with 1.
    """
    prev = 1
    nextelem = prev + prev
    while True:
        yield prev
        prev = nextelem
        nextelem = prev + prev

def stingy_lamb_generator():
    """
    Returns the fibonacci-like sequence that starts with 
    1, 1
    
    Example: 1, 1, 2, 3, 5, 8, 13, 21, ...
    """
    prevprev, prev = 1,1
    nextelem = prevprev + prev
    while True:
        yield prevprev
        prevprev = prev
        prev = nextelem
        nextelem = prevprev + prev

def num_henchmen_paid(total_lambs, generator):
    henchmen_count = 0
    sum = 0
    for lambs in generator:
        henchmen_count += 1
        sum += lambs
        # Once we go over the total_lambs that we have
        # to give, we can back off one.
        if (sum > total_lambs):
            henchmen_count -= 1
            break
    return henchmen_count

def answer(total_lambs):
    """
    See readme.txt for description.
    Input: 
      total_lambs (int)
    Output: 
      the difference in the min and max number of henchmen
      who can share the total_lambs passed as input (int)
    """
    max = num_henchmen_paid(total_lambs, stingy_lamb_generator())
    min = num_henchmen_paid(total_lambs, generous_lamb_generator())
    return max - min
