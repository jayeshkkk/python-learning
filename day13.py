#THIS LECTURE IS ABOUT STRING AND STRING METHODS
'''strings are immutable in python which means we cannot 
change the value of string once it is created'''

#changing the string into upper or lower case using string methods
a="hello this is a string"  

print(a.upper()) #this will convert the string into upper case
print(a.lower()) #this will convert the string into lower case
'''technically we can use the upper and lower case methods to
 change the string but it will not change the original string as 
 strings are immutable in python they just print a new string in upper or 
 lower case but the original string remains the same'''


#STRIPPING CHARACTERS 
b="!!!!!!!!!!!!hello!!!!!!!!!!!!!!!"
print(b)
print(b.rstrip("!")) #this will remove the ! from the string
'''it does not remove ! from the front of the string as it is 
only used to remove the characters from the right side of
 the string'''

#REPLACE FUNCTION
c="hello this is a string"
print(c)
print(c.replace("string", "sentence")) #this will replace the word string with sentence

#SPLIT FUNCTION
'''this function is used to split
 the string into a list of words'''
d="hello this is a string"
print(d.split(" ")) #this will split the string into a list of words

#COUNT FUNCTION 
# this  is used to count the number of occurrences of a substring in a string
e="hello this is a string"
print(e.count("is")) #this will count the number of occurrences of the word is in
#ENDS WITH FUNCTION
s="hello world !!!!!"
print(s.endswith("!")) #this will return true if the string ends with ! otherwise false
print(s.find("world")) #this will return the index of the first occurrence of the word world in the string
print(s.isalnum()) #this will return true if the string contains only alphanumeric characters otherwise false
print(s.isalpha())#this will return true if the string contains only alphabetic characters otherwise false  