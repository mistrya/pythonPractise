import random
import string

def hello():    
    print("Hello, World!")

# Ways to read data from a file. 

# Creating a file
file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing data to a file
file1.write("Hello \n") 
file1.writelines(L)
file1.close() # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# byte from the beginning. 
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline 
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))
print()

file1.seek(0)

# readlines function 
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close() 


# This script will generate an 18 character password
word_length = 18
# Generate a list of letters, digits, and some punctuation
components = [string.ascii_letters, string.digits, "!@#$%&"]
# flatten the components into a list of characters
chars = []
for clist in components:
  for item in clist:
    chars.append(item)
def generate_password():
  # Store the generated password
  password = []
  # Choose a random item from 'chars' and add it to 'password'
  for i in range(word_length):
    rchar = random.choice(chars)
    password.append(rchar)
  # Return the composed password as a string
  return "".join(password)
# Output generated password
print(generate_password())
