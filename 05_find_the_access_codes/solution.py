def is_factor(i,j):
    """ Returns True if i is a factor of j """
    return (j % i == 0)

def find_multiples(x, list):
    """ returns a list of indices of numbers in the list that are multiples                
        of x. if no multiple exists, then returns an empty list """
    ret_list = []
    for i in xrange(len(list)):
        if is_factor(x,list[i]) and (x <= list[i]):
            ret_list.append(i)
    return ret_list

def brute_force(l):
    if len(l) < 3:
        return 0
    lucky_triple_count = 0
    for i in xrange(len(l)-2):
        l2 = l[i+1:]
        l2indices = find_multiples(l[i], l2)
        for i2 in l2indices:
           if (i2+1 < len(l2)):
               l3 = l2[i2+1:]
               l3indices = find_multiples(l2[i2],l3)
               lucky_triple_count += len(l3indices)
    return lucky_triple_count

def more_optimal(l):
    if len(l) < 3:
        return 0

    # First, let's think of l's values as going from left to right
    # as l[i] increases.
    # Now, let's think of storing all of the indices of multiples for a certain                 
    # value of l[i] in index_of_right_multiples[i], where a "right multiple"
    # is just a multiple of l[i] that exists to the right of it.
    index_of_right_multiples = [None] * len(l)
    for i in xrange(len(l)):
        l2 = l[i+1:]
        l2indices = find_multiples(l[i], l2)
        index_of_right_multiples[i] = [(i2+i+1) for i2 in l2indices]

    # Using the index_of_right_multiples, let's optimize the brute force approach          
    # by reducing the number of calls to find_multiples()                                  
    lucky_triple_count = 0
    for i in xrange(len(l)-2):
        multiples = index_of_right_multiples[i]
        for i2 in multiples:
            lucky_triple_count += len(index_of_right_multiples[i2])
    return lucky_triple_count

def answer(l):
    #return brute_force(l)
    return more_optimal(l)

print "--------------> %d" % answer([1])
print "--------------> %d" % answer([1, 1, 1])
print "--------------> %d" % answer([1, 2, 3])
print "--------------> %d" % answer([1, 2, 3, 4, 5, 6])
print "--------------> %d" % answer([1, 2, 3, 4, 5, 6, 7])
print "--------------> %d" % answer([1, 2, 3, 4, 5, 6, 7, 8])
    
    
