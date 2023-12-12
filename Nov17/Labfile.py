try:
    with open("test.txt","r") as textfile:
        content= textfile.read()
        print(content)
except FileNotFoundError as error:
    print(error)
