#********this lecture is about type casting in  python ******
''''type casting means to convert a data type into another 
like there is a string storing 27 and we want to convert it into integer so we can use int() 
function to convert it into integer
we can also convert integer into string using 
str() function and we can convert float into integer using 
int() function but it will remove the decimal part of the 
float number'''

a= "27"
b = "12"
print (a+b)
print(int(a)+int(b))   

'''there is TWO TYPES of type casting in python-
        1.IMPLICIT CASTING -data type conversion is done by python 
                             automatically without
                           any manual intervention by the developer
                           as some data types have higher precedence
                             than others so python automatically example 
                             int and float .....float have higher order
        2.EXPLICIT CASTING -the comnversion of data type manually by
                            developer
                           is called explicit casting'''
'''