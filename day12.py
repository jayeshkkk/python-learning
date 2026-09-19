#THIS LECTURE IS ABOUT STRING SLICES IN PYTHON
name = "jayeshkhandelwal"
print(name[0:6]) #prints from index 0 to 5
print(name[:6]) #it automatically takes value from 0 if left empty
#we can use this syntax to print a range slice of string

'''we can find the length of the string using len() function'''
print(len(name))#this is an example of lenght function
'''we can use operations like + and - while printing
a range of string using the lenth function''' 
print(name[:len(name)-6]) 
print(name[:-4])#PYTHON TAKES THE LENGTH FUNCTION AUTOMATICALLY IF WE USE NEGATIVE INDEXING 
print(name[-7:8])
'''this works in a way that it will start printing 
from -7(including) and will print till 8(excluding)'''