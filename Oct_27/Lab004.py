# Write a Python program to count the number of strings in a list where the string length is 2 or more and
# the first and last character are the same.

list1 = ['aba', 'abcd', 'hello', 'madam', '121', 'bb']
list2 = []

for x in list1:
    if len(x) >= 2 and x[0] == x[-1]:
        list2.append(x)
    else:
        pass

print(list1)
print(list2)
print(f"count of strings with the given logic is : {len(list2)} ")
