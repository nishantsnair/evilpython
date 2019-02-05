name = input("What is your name?")
file = open("yournameis.txt",'w')
file.write(name)
file.close()
