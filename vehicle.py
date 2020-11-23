import random
 

class Vehicle:
    def __init__(self,make,model,year,weight,NeedsMaintenance=False,TripsSinceMaintenance=0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance
    
    # getters
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight

    #setter
    def setMake(self,make):
        self.make = make

    def setModel(self,model):
        self.model = model

    def setYear(self,year):
        self.year = year

    def setWeight(self,weight):
        self.weight = weight
    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False

# define cars class 
class Cars(Vehicle):
    def __init__(self,make, model, year, weight,isDriving = False):
        Vehicle.__init__(self,make, model, year, weight)
        self.isDriving = isDriving

    def Drive(self):
        self.isDriving =True

    def stop(self):
        if self.isDriving:
            self.tripsSinceMaintenance+=1
            if self.TripsSinceMaintenance > 100:
                self.NeedsMaintenance = True

        self.isDriving = False

# define plane class
class Plane(Vehicle):
    def __init__(self, make, model, year, weight, isFlying = False):
            Vehicle.__init__(self, make, model, year, weight)
            self.isFlying = isFlying
    
    def flying(self):
        if self.needsMaintenance == True:
            return False
        self.isFlying = True
        return True
    
    def landing(self):
        if self.isFlying:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isFlying = False

 

 # drive and stop car random no of times
def randomly_drive_car(car):
    drive_times = random.randint(1, 101)
    for i in range(drive_times):
        car.drive()
        car.stop()

# fly and land plane random no of times
def randomly_fly_plane(plane, fly_times = None):
    fly_times = random.randint(1, 101) if fly_times is None else fly_times
    for i in range(fly_times):
        is_flying = plane.flying()
        if is_flying:
            plane.landing()
        else:
            print("plane " + plane.model + " can't fly until it's repair", 'red', attrs=['bold'])
            print("Repairing... " + plane.model, 'blue', attrs=['bold'])
            plane.repair()

# print car attributes         
def print_car_specs(car):
    print("========================")
    print('Make ',car.make)
    print('Model ',car.model)
    print('Year ',car.year)
    print('Weight ',car.weight)
    print('Weight ',car.weight)
    print("========================\n")

# print plane attributes
def print_plane_specs(plane):
    print("========================")
    print('Make ',plane.make)
    print('Model ',plane.model)
    print('Year ',plane.year)
    print('Weight ',plane.weight)
    print('Weight ',plane.weight)
    print("========================\n")

# creating three instances from Cars class
carOne = Cars("Toyota", "Corolla", 2020, 1044 )
carTwo = Cars("Toyota", "Camry", 2013, 1200 )
carThree = Cars("Toyota", "Venza", 2015, 1300 )

# creating two objects from Plane class
planeOne = Plane("Aeronca","15 AC Sedan", 1992, 2050)
planeTwo = Plane("Aeronca","12 AC Sedan", 1982, 2030)

 

# printing cars and plane attributes
print_car_specs(carOne)
print_car_specs(carTwo)
print_car_specs(carThree)
print_plane_specs(planeOne)
print_plane_specs(planeTwo)