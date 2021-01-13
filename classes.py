import random

class Vehicle:
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance

  
    

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight
    
    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False

class Cars(Vehicle):
    def __init__(self, make, model, year, weight, isDriving = False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = isDriving
    
    def drive(self):
        self.isDriving = True
    
    def stop(self):
        if self.isDriving:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isDriving = False


def randomly_drive_car(car):
    drive_times = random.randint(1, 101)
    for i in range(drive_times):
        car.drive()
        car.stop()


def print_car_specs(car):
    print('Make ',car.make)
    print('Model ',car.model)
    print('Year ',car.year)
    print('Weight ',car.weight)
    print('Needs Maintenance ',car.needsMaintenance)
    print('Trips Since Maintenance ',car.tripsSinceMaintenance)
    print('Weight ',car.weight)


carOne = Cars("volkswagen group", "ameo", 2010, 1033 )
carTwo = Cars("volkswagen group", "polo", 2008, 1038 )
carThree = Cars("volkswagen group", "vento", 2010, 1023 )


randomly_drive_car(carOne)
randomly_drive_car(carTwo)
randomly_drive_car(carThree)

print_car_specs(carOne)
print_car_specs(carTwo)
print_car_specs(carThree)
