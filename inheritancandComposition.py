class Tires:
    def __init__(self,numOfTires,size):
        self.numOfTires=numOfTires
        self.__size=size
        
    def pump(self,pressure):
        self.pressure=pressure
    
    def get_pressure(self):
        return self.pressure
        
    @property
    def size(self):
        return self.__size
        
    @size.setter
    def size(self,size):
        self.__size = size
        
        
class Engine:
    def __init__(self, fuelType):
        self.__fuelType =fuelType
        
    @property
    def fuelType(self):
        return self.__fuelType
        
    @fuelType.setter
    def fuelType(self,fuelType):
        self.__fuelType = fuelType 
        
    def start(self):
        self.state ="started"
        print("starting engine with fuel type{}".format(self.__fuelType))
        
    def stop(self):
        self.state ="stopped"
        print("stopped engine with fuel type{}".format(self.__fuelType))
        
    def get_state(self):
        return self.state
        
class Vehicle:
    def __init__(self,VIN,engine,tires):
        self.__VIN=VIN
        self.engine = engine
        self.tires = tires
        
    @property
    def VIN(self):
        return self.__VIN
        
    @VIN.setter
    def VIN(self,VIN):
        self.__VIN = VIN 
        
city_tires = Tires(4,15)
off_road_tires = Tires(4,18)
electric_engine = Engine("electric") 
petrol_engine = Engine("petrol") 

city_car =Vehicle(123, electric_engine, city_tires)
all_terrain_car=Vehicle(323, petrol_engine, off_road_tires)
city_car.tires.pump(89)
print("city_car tires' pressure: ", city_car.tires.get_pressure())
city_car.engine.start()
print("city_car engine's state: ", city_car.engine.get_state())
city_car.engine.stop()
print("city_car's VIN: ", city_car.VIN)

all_terrain_car.tires.pump(99)
print("all_terrain_car tires' pressure: ", all_terrain_car.tires.get_pressure())
all_terrain_car.engine.start()
print("all_terrain_car engine's state: ", all_terrain_car.engine.get_state())
all_terrain_car.engine.stop()
print("all_terrain_car's VIN: ", all_terrain_car.VIN)
        
