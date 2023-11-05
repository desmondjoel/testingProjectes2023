class Car():
    brand=None
    color=None
    TopSpeed=None

    def startcar(self):
        print("Car is running")

    def stopcar(self):
        print("car has stopped")

ford_obj= Car()
ford_obj.brand="Ford"
ford_obj.color="Back"
ford_obj.TopSpeed="200"
ford_obj.stopcar()
ford_obj.stopcar()