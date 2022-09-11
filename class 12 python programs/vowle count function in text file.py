# Write a python program to
# open a file in read mode
# and count number of vowels
# in this text file
# Assume that the text file has the name
# mytext.txt and is on D drive
# Assume that mytext.txt file has the 
# following contents without hash sign

# This file contains some example text.

# open file in read mode
file1 = open("poem.txt", "r")

# read all the contents of file
# and store in a string variable 
# named str1 using read() function

str1 = file1.read()

# find the number of the vowels in file

vowel_count =  0
for i in str1:
    if( i=='A' or i=='a' or i=='E' or i=='e' or i=='I'
        or i=='i' or i=='O' or i=='o'
	or i=='U' or i=='u'):
        	vowel_count +=1
        

print('The Number of Vowels in text file :', vowel_count)

file1.close()

