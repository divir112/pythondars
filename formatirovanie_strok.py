#способ1
f = open("newfile.txt", "w")
f.write("Hello\n")
f.write("world\n")
f.close()
print(f.closed)
f = open("newfile.txt", "r")
print(f.read())
y = f.readlines()
print(y)
f.seek(0)

x = f.read()
print(x.split())
print(x)
print(f.closed)

#способ2

with open("newfile.txt") as file:
    data = file.read()
print(data)
print(file.closed)






