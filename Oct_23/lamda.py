#Create a Lambda expression to triple power 2**3 a number
a=int(input("Enter the Number"))
cube=lambda a:a**3
print(f"The Cube of given number {a} ,using lambda function is {cube(a)}")