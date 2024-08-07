names = "C:/Users/USER/Desktop/names.txt"
output = "C:/Users/USER/Desktop/output .txt"

#reading file and display
with open(names, "r") as file:
    text = file.read()
    wordcount = len(text.split())
    print(text)
    print("word count:" ,wordcount)

#writing a file
with open(output, "w") as file:
    line1 = file.write('careers IT\n')
    line2 = file.write('system development\n')
    line3 = file.write('assessor - Mr Masiya')
    file.close()
