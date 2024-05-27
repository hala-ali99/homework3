
# Online Python - IDE, Editor, Compiler, Interpreter
def factorial (n):
    fact = 1
 
    for i in range(1, n+1):
     fact = fact * i
    return fact
print("Enter your number : ")
while True:
    try: 
        number = int(input())
    except ValueError:
        print ("Please enter a number")
    else:
        break

print(factorial(number))