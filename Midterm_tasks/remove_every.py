def remove_every(l, n):
    res = []

    while n <= len(l) - 1:
        res.append(l[n-1])
        n *= 2
    
    print(res)

    return [x for x in l if not x in res]

print( remove_every([1, 2, 3, 4, 5], 2) )
print( remove_every([1, 2, 3, 4, 5, 4, 3, 2, 1], 3) )
