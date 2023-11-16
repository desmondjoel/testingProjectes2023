class Person():
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name (self):
        return self.__name

    def set_name(self,name):
         self.__name =name

    def print_details(self):
        print("You details", self.__name, self.__age)

person = Person("Joel",25)
person.print_details()
namenew=person.get_name()
print(namenew)
newname = input("Enter new name")
person.set_name(newname)

namenew=person.get_name()
print(namenew)