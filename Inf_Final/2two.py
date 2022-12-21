class Order:

    def __init__(self, items, cost):
        self.__items = items
        self.__cost = cost
    
    def __eq__(self, other):
        if not isinstance(other, Order): return False

        return sorted(self.__items) == sorted(other.__items) and self.__cost == other.__cost

print( Order(["Beer", "Wine", "Beer"], 14.50) == Order(["Wine", "Beer", "Beer"], 14.50) )
print( Order(["Beer", "Wine", "Beer"], 14.50) != Order(["Wine", "Beer"], 14.50) )
print( Order(["Beer", "Pretzels"], 14.50) == "Healthy meal" )