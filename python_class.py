class Car:
    def __init__(self, brand, color, _type):
        self.color = color
        self.brand = brand
        self.type = _type
        self.drive_count = 0
        self.is_service_due = False
        
    def drive(self):
        if self.is_service_due:
            raise Exception("Car is due")
        
        self.drive_count += 1
        if (self.drive_count % 10) == 0:
            self.is_service_due = True
    
    def service(self):
        self.is_service_due = False

mariam_car = Car("benz", "black", "suv")
tawa_car = Car("lexus", "white", "convertible")
halima_car = Car("toyata", "wine", "suv")

import pdb; pdb.set_trace()
print()