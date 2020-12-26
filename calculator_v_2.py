#only use for import file 
def addition(d_add,e_add):
    c_add = int(d_add) + int(e_add)
    print(d_add,"+",e_add,"=",c_add)

def subtraction(d_sub,e_sub):
    c_sub = d_sub - e_sub
    print(d_sub,"+",e_sub,"=",c_sub)    

def multiplication(d_mulp,e_mulp):
    c_mulp = d_mulp * e_mulp
    print(d_mulp,"+",e_mulp,"=",c_mulp)

def division(d_div,e_div):
    c_div = d_div / e_div
    print(d_div,"+",e_div,"=",c_div)

#       Read how To use
#
#This is example of import in python.
#1. save this file to your computer
#2. create a new file
#       example.py
#2. in a new file write import <your file> 
#       import calculator_v_2.py
#3. if you want to acces the file write calculator_v_2.<the function>(number1,number2)
#       calculator_v_2.addition(4,5)
#
#the output of this file:
#3 + 5 = 9
#
#
