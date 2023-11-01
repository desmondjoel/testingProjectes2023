num=[1,2,3,4,5,6,7,100,66]

def even_num(num):
    return num%2==0;

even=list(filter(even_num,num))
print(even)

#is_positive

dig=[1,10,-9,-7,-99,100,101,-77]

def is_positive(n):
    return n>0

postive=list(filter(is_positive,dig))
print(postive)

#---------------------------------------------------------------------------

#lenght
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
min_len = 6

def item_len(item):
    return len(item)>=min_len

item_list=list(filter(item_len,words))
print(item_list)