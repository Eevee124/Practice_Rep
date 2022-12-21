#take ord() of chars in given string and add num to ord then interweave with 
#list todo in order to create encoded string

class Coder:
    def __init__(self, todo):
        self.__todo = todo
        self.__ind = 0
    
    def iter(self):
        if self.__ind >= len(self.__todo):
            self.__ind = 0

        val = self.__todo[self.__ind]
        self.__ind += 1
        return val

def encode(to, num, todo):
    encoder = Coder(todo)


    first = []
    inter = []

    for char in to:
        first.append(ord(char) + num)
        inter.append(ord(char) + num)
        inter.append(encoder.iter())

    #takes the encoding list and turns it into string by
    #casing all ascii numbers to char
    res = "".join(chr(i) for i in inter)

    print(first, inter, res)

    return first, inter, res

def decode(to, num, todo):
    encoder = Coder(todo)

    inter = []

    res = ""
    for char in to:
        if len(inter) < num:
            inter.append(ord(char))
        else:
            res += chr(inter.pop(0))
            inter.append(ord(char))
    while inter:
        res += chr(inter.pop(0))

    print(inter, res)

    return inter, res

print(encode("hello", 3, [65,99,120]) ==
     ([107, 104, 111, 111, 114], [107, 65, 104, 99, 111, 120, 111, 65, 114, 99], 'kAhcoxoArc'))
print(decode("kAhcoxoArc", 3, [65,99,120]) ==
     ([107, 65, 104, 99, 111, 120, 111, 65, 114, 99], [107, 104, 111, 111, 114], 'hello'))