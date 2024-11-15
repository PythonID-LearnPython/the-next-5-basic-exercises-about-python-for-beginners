# s = (a+b+c)/2
# area = √(s(s-a)*(s-b)*(s-c))

# Python Program to find the area of triangle

a = 3
b = 4
c = 5

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
