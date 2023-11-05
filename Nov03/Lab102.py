class Car():
    brand=None
    color=None
    TopSpeed=None

    def car_details(self):
      print("your car details are" ,self.brand, self.color)


car_brand=input("Enter the car brand")
car_color=input("Enter the car color")

car_obj_ref= Car()
car_obj_ref.brand=car_brand
car_obj_ref.color=car_color
car_obj_ref.car_details()