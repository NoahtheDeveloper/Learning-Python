# This copies a document information and pastes it somewhere.

# This has to be named where u want to take the text from.
myfile = open('TEST.txt')

# Reads the file.
content = myfile.read()

# Closes file.
myfile.close()
print('I have closed this file.')

# Opens the file its gonna be pasted in.
newfile = open('TEST1.txt', 'w')
print('I have opened this new file.')

#This types the content
newfile.write(content)
print('I have printed text in this file.')


# File now closed
newfile.close()
