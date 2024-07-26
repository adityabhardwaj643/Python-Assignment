#Write a Python program to read the contents of a text file and print them to the console
f = open('textFile.txt','r')
content = f.read()
print(content)
f.close()