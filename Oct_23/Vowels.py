text=input("Please enter a string")
str=text.lower()

vowels=0
consonents=0


for i in str :
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels=vowels+1
    else:
        consonents=consonents+1
print("The number of vowels:", vowels)
print("\nThe number of consonant:", consonents)



