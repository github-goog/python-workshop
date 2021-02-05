lst = []  
n = int(input("Enter number of elements in list : ")) 

# Taking input 
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele) 

print("")
print("The list : ", lst)

new_lst = []

for i in lst:
  if (i > 0):
    new_lst.append(i)
    
print("The new list : ", new_lst)
