file=open("darsh.txt","w")
file.write("Hello World! ")
file.close()

file=open("darsh.txt","a")
file.write("How are you?")
file.close()

file=open("darsh.txt","r")
print(file.read())
file.close()