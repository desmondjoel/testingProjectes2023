with open("example.txt", "r") as  file:
    line = file.readlines()
    print(line)
    for a in line:
        print(a, end='')
