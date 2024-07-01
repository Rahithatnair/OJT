
#python for loop

list={'apple','guava','banana','grapes'}
print('this is our list',list)

for i in list:
    print(i)

#for loop with tuple
tuple=('carrot','tomato','pototo','eggplant','onion')
print('this is our tuple',tuple)
for i in tuple:
    print(i)
    
#for loop with string
string='India'
for i in string:
    print(i)
    

#range([start],[end],[step])

for i in range(11):
    print(i)
    
    
for i in range(2,11):
    print(i)
    
for i in range(2,10,2):
    print(i)


#for loop with else condition
#here we are checking whether the given number is prime or not
num=int(input("enter a number : "))
for i in range(2,num):
    if (num%i!=0):
        print('%d is not a prime number'%num)
        break
else:
        print('%d is a prime number'%num)
        
        

# Nested Loop
# Define the size of the pattern
size = 7
# Nested loops to iterate through rows and columns
for row in range(size):
    for col in range(size):
        # Conditions to determine whether to print '*' or ' '
        if (col == 1 or col == 5) and row != 0:
            print("*", end="")
        elif (row == 0 or row == 3) and (1 < col < 5):
            print("*", end="")
        else:
            print(" ", end="")
    
    # Move to the next line after each row is printed
    print()