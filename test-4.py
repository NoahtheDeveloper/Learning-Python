# Opens files and reads them..

# The file name should be in ('XXX')
myfile = open('TEST.txt')

print("\nWe have opened a file that contains an eight-line poem.\n")
print("\nWe'll create a list with readlines() ...\n")

# Reads information in the txt file.
line_list = myfile.readlines()

print("I have stated everything in that txt document.")

# Prints entire list out.
print(line_list)



# This will close the file.
myfile.close()
print("File has now been closed.")
