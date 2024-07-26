#Write a Python program to write a list of strings to a text file, each on a new line. 
def writeListToFile(strings,file_path):
    with open(file_path,'w') as f:
        for string in strings:
            f.write(string + '\n')

strings = ["Hello Everyone.", "This is Task2.", "Writing in textFIle2"]
file_path = 'textFile2.txt'  
writeListToFile(strings, file_path)           