#Program from vehicle
class Vehicle:
    seats = 0
    _wheels = 4
    _engine = "V8"
    _electro = False
    _name = None

    def start(self):
        print("dr-dr-dr")

    def beep(self):
        print("some beep sound")

    def get_seats(self):
        print(self.seats)

    def get_wheels(self):
        print(self._wheels)

    def get_name(self):
        print(self._name)


class Automobile(Vehicle):
    seats = 4
    _wheels = 4
    _engine = "V8"
    _electro = True
    _name = 'Automobile'

    def beep(self):
        print('beep')


class Truck (Vehicle):
    seats = 2
    _wheels = 12
    _engine = "V8"
    _electro = False
    _name = 'Truck'

    def beep(self):
        print('I am truck, get away')


auto = Automobile()
truck = Truck()

auto.get_name()
auto.get_seats()
auto.get_wheels()
auto.beep()

truck.get_name()
truck.get_seats()
truck.get_wheels()
truck.beep()
