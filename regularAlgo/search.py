programming_languages = ["JavaScript","Python","Java","Python","C++","Python"]

python_indices  = [index for (index, item) in enumerate(programming_languages) if item == "Python"]

print(python_indices)

Row = 4 #int(input("Enter the number of rows:"))
Column = 4 #int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries row wise:")

# For user input
# A for loop for row entries
for row in range(Row):    
    a = []
    # A for loop for column entries
    for column in range(Column):   
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()

mystring = "mr bean do do do ooo "
word = " sqllll "
if word in mystring: 
   print('success')

# take input of string from user
string = input("Enter strings to remove commas: ")

# use replace() function
new_string = string.replace(",", "")

string = input("Enter strings to remove commas: ")

# use replace() function
new_string = string.replace(",", "",1)

import re

# take input of string from user 
string = input("Enter strings to remove commas: ")

# use re.sub|() function
new_string = re.sub(",", "", string)
