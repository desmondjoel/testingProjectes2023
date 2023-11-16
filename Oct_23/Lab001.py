
# Palindrome
# Reverse the String and match with the old String it should be same.
# 1 By using a Traditional method
# 2 Built in functions


def rev_string(input):
    rev_str=""
    for a in input:
        rev_str=a + rev_str
    return rev_str

orgi_str="jorl"
rev_str=rev_string(orgi_str)
print(rev_str)

if orgi_str == rev_str:
    print("Its a Palindrome")
else:
    print("Not a Palindrome")



 #=====================================================================
test="naman"


def is_palindrome(a):
    revv_str = a[::-1]
    print(revv_str)
    if (a == revv_str):
        print("Its a Palindrome")
    else:
        print("Not a Palindrome")


test = "naman"
is_palindrome(test)

