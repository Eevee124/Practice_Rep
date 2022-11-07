def remove_every(l, n):
    res = []
    #unsure whether one would need to check for edge cases, though those would
    #be rather simple to implement

    for i in range(len(l)):
        if (i + 1)%n != 0:
            res.append(l[i])
    
    return res

print( remove_every([1, 2, 3, 4, 5], 2) )
print( remove_every([1, 2, 3, 4, 5, 4, 3, 2, 1], 3) )