numList = [30, 2, -15, 17, 9, 100]

def num_greater(n):
    return n>10

output= list(filter(num_greater,numList))
print(output)

output1= list(filter(lambda n:n>10,numList))
print(output1)

numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def num_even (n):
    return n%2==0

res=list(filter(num_even,numbers_tuple))
print(res)