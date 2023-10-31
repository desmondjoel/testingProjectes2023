# find the smallest number in a list

list1 = [10,15,5,50,100,90,34,-560]

min1 = list1[0]

for x in list1:

    if x < min1 :
        min1=x
    else:
        pass
print(f"Largest number in list is {min1}")

list2=list1.copy()
list2.sort()
print(f"largest number in list using direct methods is {list2[0]}")
print("Largest element is:", min(list1))