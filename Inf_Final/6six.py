class Airplane:
    def __init__(self, model, tail_number):
        self.__model = model
        self.__tail_number = tail_number
        self.__passen = []
    
    def board(self, passen):
        self.__passen += passen

    def get_passengers(self, class_=None):
        if class_ is None:
            return self.__passen
        return [p for p in self.__passen if p.class_ == class_]
    
    @staticmethod
    def parse_manifest(manifest):
        passengers = []
        for line in manifest.split(";"):
            name, section, seat = line.split(",")
            passengers.append(Passenger(name, section, seat))
        return passengers
    
class Passenger:
    def __init__(self, name, class_, seat):
        self.__name = name
        self.class_ = class_
        self.__seat = seat

    def __str__(self):
        return f"{self.__name}, {self.class_}, {self.__seat}"

passengers = Airplane.parse_manifest(("Montgomery,Rich,1;Tim,Merchant,2;Sally,Sale,2;Peter,Poor,3"))
a = Airplane("A388", "G-XLEK")
a.board(passengers)
print(a.get_passengers())
p = a.get_passengers(2)
print(type(p[1]))
print(p[1])