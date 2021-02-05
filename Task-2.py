num = int(input("Enter the number in sequence : "))
num1, num2 = 0, 1
count = 0

if num <= 0:
   print("Invalid Number")
elif num == 1:
   print("Fibonacci sequence for limit of ",num,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   while count < num:
       print(num1)
       nth = num1 + num2
       num1 = num2
       num2 = nth
       count += 1
