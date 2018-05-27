firstpriorityoperation="*/"
secondpriorityoperation="+-"
operations="+-*/"
stack=[]

def calc(op1,op2,operation):
    if(operation == '+'):
        return float(op1)+float(op2)
    elif (operation == '-'):
        return float(op1)-float(op2)
    elif (operation == '*'):
        return float(op1)*float(op2)
    elif (operation == '/'):
        return float(op1)/float(op2)
    else :
        raise ArithmeticError("Unknown operation")

def priority(s):
    if s in firstpriorityoperation:
        return 1
    elif s in firstpriorityoperation:
        return 2
    else:
        return 3

def parse(ex_str):
    print(ex_str)
    operand=''
    for index, s in enumerate(ex_str):
        if s.isdigit() or s=='.':
            operand = operand+s
        elif s in operations:
            while(stack!=[] and priority(s)>=priority(stack[-1])):
                operation=stack.pop()
                previous_operand=stack.pop()
                operand=str(calc(previous_operand,operand,operation))
            stack.append(operand)    
            stack.append(s)
            operand=''
        else :
            raise SyntaxError("Unknown symbol")
    
    if operand:
        stack.append(operand)

    while stack:
        op2 = stack.pop()
        if not stack:
            return float(op2)

        operation = stack.pop()
        op1 = stack.pop()
        res = str(calc(op1,op2,operation))
        stack.append(res)

    raise ArithmeticError('Something bad happend')

def calculator(ex_str):
    if not ex_str.endswith("="):
        return "Not valid string"
    ex_str = ex_str.replace("\"","")
    ex_str = ex_str.replace("=","")
    return parse(ex_str)
'''
print('1={}'.format(str(calculator("\"1=\""))))
print('2+2={}'.format(str(calculator("\"2+2=\""))))
print('2+2+2+2+2+2={}'.format(str(calculator("\"2+2+2+2+2+2=\""))))
print('2*10+1={}'.format(str(calculator("\"2*10+1=\""))))
print('2+10*1={}'.format(str(calculator("\"2+10*1=\""))))
print('2+10*1*2+9={}'.format(str(calculator("\"2+10*1*2+9=\""))))
print('6/3*2={}'.format(str(calculator("\"6/3*2=\""))))
print('2+10*1/2+9={}'.format(str(calculator("\"2+10*1/2+9=\""))))
print('2-2-2-2-2-2={}'.format(str(calculator("\"2-2-2-2-2-2=\""))))
print('2-2*12={}'.format(str(calculator("\"2-2*12=\""))))
'''

#str=input("Enter test ex: ")
#print(calculator(str))