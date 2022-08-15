#creating a class(qn.1)
class Vehicle:
    def __init__(self,name,max_speed,mileage): 
        self.max_speed=max_speed
        self.mileage=mileage
        self.name=name

#creating an object(qn.2)
Bus=Vehicle("School Volvo",180,12)
print("Vehicle Name: {} Speed: {} mileage: {}".format(Bus.name,Bus.max_speed,Bus.mileage))        

#inheritance(qn.3)
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage,Seating_capacity=50):
        super().__init__(name, max_speed, mileage)
        self.Seating_capacity=Seating_capacity
#creating an object with only 3 arguments.    
motors=Bus("School volvo",180,12)      
print("The seating capacity of a bus is {} passengers".format(motors.Seating_capacity))    

#class attribute and instance attribute.(qn.4)
class Vehicle:
    color="white"
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        print("color: {}, Vehicle name: {}, Speed: {}, mileage: {}".format(self.color,self.name,self.max_speed,self.mileage))
class Bus(Vehicle):
    pass
class Car(Vehicle):
    pass

cycle1=Bus("School Volvo",180,12)  
cycle2=Car("Audi QS",240,18)

#functions(qn.5)
class Vehicle:
    def __init__(self,name,mileage,capacity): 
        self.name=name
        self.mileage=mileage
        self.capacity=capacity

    def fare(self):
        return self.capacity*100
class Bus(Vehicle):
    def fare(self): #overriding(change how a function works) 
     total_fare=self.capacity*100 
     return total_fare +0.1*total_fare  
School_bus=Bus("School Volvo",12,50) 
print("Total Bus fare is: ", School_bus.fare())            

