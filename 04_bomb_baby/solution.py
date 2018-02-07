def answer(M, F):
    """
    See readme.txt for the problem description.
    
    The approach for this solution is to start with the
    input (M, F) and work backwards to see if we 
    can achieve (1,1).
    
    Loop invariant --
    (m, f) represent the number of Mach and Facula bombs
    that we have at a certain point in time, and num_cycles
    represents the number of cycles that we have gone 
    backwards in time to get there.
    
    Input:
        M - (string) number of Mach bombs needed to destroy 
            the LAMBCHOP
        F - (string) number of Facula bombs needed
            the LAMBCHOP
    Returns: 
        (string) The number of cycles/generations that are 
        needed to achieve the input M, F bombs. If it's
        not possible, then "impossible" is returned.
    """
    m = int(M)
    f = int(F)

    num_cycles = 0
    while True:
        if ((m < 1) or (f < 1)):
            # Impossible Case:
            # If at any point, we get a negative number
            # of bombs, it's impossible.
            return "impossible"
        elif (m == 1):
            # Stopping Case:
            # Having only one Mach bomb left means we can
            # work back f-1 cycles more to achieve the goal
            return str(num_cycles + f - 1)
        elif (f == 1):
            # Stopping Case:
            # Having only one Facula bomb left means we can
            # work back m-1 cycles more to achieve the goal
            return str(num_cycles + m - 1)
        elif (m>f):
            # Speed optimization:
            # For cases where m is way bigger than f,
            # we can jump ahead by dividing m by f
            # and continuing with the remainder. 
            cycle_jump, remainder = divmod(m,f)
            num_cycles += cycle_jump
            m = remainder
        elif (f>m):
            # Speed optimization:
            # For cases where f is way bigger than m,
            # we can jump ahead by dividing f by m
            # and continuing with the remainder. 
            cycle_jump, remainder = divmod(f,m)
            num_cycles += cycle_jump
            f = remainder
        else:
            # This is the typical case. 
            # We subtract the smaller number of bombs from
            # larger number, and increase the cycle count.
            num_cycles += 1
            if (f > m):
                f -= m
            else:
                m -= f
