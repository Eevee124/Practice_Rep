import random
# this line of code makes it so that calls to random always produce the same
# successive values so that the examples below always produce the same results
random.seed(7)
def lottery(limit, guess, prize):
    numbers = []
    for i in range(len(guess)):
        numbers.append(random.randrange(1, limit, 1))
    
    difference = 0
    
    for i in range(len(numbers)):
        if not numbers[i] in guess:
            difference += 1
    
    prize /= 2**difference
    
    return (guess, len(guess) - difference, prize)

print( lottery(52, [4, 8, 15, 16, 23, 42], 1000000) ) # 2 matching
print( lottery(3, [1, 2, 3], 1000000) )               # inevitable perfect match
print( lottery(10000, [1, 2, 3], 1000000) )           # zero matching