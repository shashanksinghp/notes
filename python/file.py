"r, w, a"
file = open("geek.txt", "w")
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

file = open("geek.txt", "a")
file.write("This will add this line")
file.close()
