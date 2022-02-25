fin=open("C:\\Users\\Aditya\\Downloads\\chatb2\\chatb2\\hello.txt","r")
x=fin.read()
print(x)
fin.close()

with open( "C:\\Users\\Aditya\\Downloads\\chatb2\\chatb2\\hello.txt") as f:
    y=f.read()
print(y)