class Vehicle:
    def __init__(self, max_speed, milage) :
        self.max_speed = max_speed
        self.milage = milage
    
subaru = Vehicle(240,1800)
print(f"{subaru.max_speed} km/h with {subaru.milage} miles")

class Vehicle:
    pass

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

bus = Vehicle('Volvo', 180, 12)
print(f"Vehicle name: {bus.name} Speed: {bus.max_speed} milage: {bus.mileage}")

# or
class Bus(Vehicle):
    pass
school_bus = Bus('School Volvo', 180, 12)
print('vehicle name:',school_bus.name,'speed:',school_bus.max_speed,'milage:', school_bus.mileage)


class Courses:
    def __init__(self, course_code, name) -> None:

        self.course_code = course_code
        self.name = name

Course = Courses("DCIT105", "Maths for IT Professionals")
print(Course.course_code)
print(f"what time do we have {Course.name} ?\n")
input('enter time: ')