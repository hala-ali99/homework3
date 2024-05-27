
# Online Python - IDE, Editor, Compiler, Interpreter

flag = True 
b_num = list(input("Input a binary number:"))
while flag:
    for i in range(len(b_num)):
        digit = b_num.pop()
        cond=(digit=='1' or digit == '0')
        if not(cond):
            flag = True
            b_num = list(input("Input a binary number:"))
        else:
            flag = False
            
    value = 0
    for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
               value = value + pow (2,i)
               print("The decimal value of the number is",value)