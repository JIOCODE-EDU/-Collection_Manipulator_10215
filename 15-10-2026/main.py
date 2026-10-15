import geomatry

# import math
# import datetime

# print("Attributes and Methods of math module")

# for item in dir(math):
#   print(item)

# for item in dir(datetime):
#   print(item)


# dir() with custom object

# class Student:
#   def __init__(self , name , age):
#     self.name = name
#     self.age = age

#   def display(self):
#     print("Name :" , self.name)
#     print("Age :" , self.age)

# student = Student("Rahul" , 20)

# for item in dir(student):
#   print(item)

# print("Area of Circle:" , c(10) )
# print("Area of Triangle:" , a(10 , 20) )

print("Circle Area = " , geomatry.circle_area(10))
print("Circle Circumference = " , geomatry.circumference(20))