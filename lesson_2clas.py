#class wotk
for i, j in  enumerate( range(10) ):
    print(i, j)


class Animal:
    name = None
    animal_type = None

    def __init__(self, name, type):
        self.name = name
        self.animal_type = type

    def move( self ):
        print("i`am moving")

    def eat(self):
        print("i`am eating")

    def sleep(self):
        print("i`am sleeping")

    def who_am_i(self):
        print("i`am the {}. My Type is {}".format(self.name, self.animal_type))

    def __del__(self):
        print("пака")


animal_obj = Animal('шарик','dog')

animal_obj.eat( )
animal_obj.sleep( )
animal_obj.who_am_i( )


print( Animal.name )
del animal_obj
