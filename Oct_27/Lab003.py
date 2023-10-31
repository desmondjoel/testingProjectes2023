# program to sum all numbers in a list.

list1 = [10,15,5,50,100,90,34,560]

total = 0

for a in list1:
    total = total + a

print(f"Sum of all number in list is {total}")

print(f"Sum of all number in list using sum function is  {sum(list1)} ")
