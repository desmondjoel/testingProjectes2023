# find the largest number in a list

list1 = [10,15,5,50,100,90,34,-560]

max1 = list1[0]

for x in list1:

    if x > max1 :
        max1=x
    else:
        pass
print(f"Largest number in list is {max1}")

list2=list1.copy()
list2.sort()
print(f"largest number in list using direct methods is {list2[-1]}")
print("Largest element is:", max(list1))