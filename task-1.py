# Task 1A

print("Area of Circle -->")

PI = 3.14
print("")
radius = float(input("Enter the radius of circle : "))
area = PI * radius * radius

print("Area Of a Circle = %.2f" %area)
print("")
print("-----------------------------------------------------")
print("")

# Task 1B

name = input("Input the Filename: ")
ext = name.split(".")
i = repr(ext[-1])

print(i)

if (i == "'txt'"):
  j = "'text'"
elif (i == "'py'"):
  j = "'python'"
else:
  j = i

print ("The extension of the file is : " + j)
