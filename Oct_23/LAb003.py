

def is_palindrome(a):
     revv_str=a[::-1]
     print(revv_str)
     if(a==revv_str):
         print("Its a Palindrome")
     else:
         print("Not a Palindrome")

test="naman"
is_palindrome(test)
