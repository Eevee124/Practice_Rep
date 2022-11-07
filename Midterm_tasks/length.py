def length(iterable) :
     
    # if we reach at the
    # end of the string
    
    if (type(iterable) == tuple and iterable == ()) or (type(iterable) == str and iterable == '') or (type(iterable) == list and iterable == []):
        return 0
        
    else :
        return 1 + length(iterable[1:])

print( length([1, 2, [3, 4]]) )
print( length(("a", 1, 2, None)) )
print( length("oh dear"))