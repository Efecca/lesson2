firstpriorityoperation="*/"
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
        return 3
    elif s in operations:
        return 2
    else:
        return 1

def parse(ex_str):
    operand=''
    for index, s in enumerate(ex_str):
        if s.isdigit() or s=='.':
            operand = operand+s
        elif s in operations:
            #Укладываем в стек поочередно операнды и операции
            #Если вновь пришедшая операция имеет такой же или ниже приоритет чем предыдущая - вытаскиваем все и вычисляем
            #Пока не упремся в результат или операцию какого же приоритета
            while(stack!=[] and priority(s)<=priority(stack[-1])):
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

    #если в стеке еще что-то осталось, вытащим и вычислим
    while stack:
        op2 = stack.pop()
        #ну может там только результат и есть
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
    try:
        return parse(ex_str)
    except SyntaxError as e:
        return("В выражении {} допущена синтаксическая ошибка".format(ex_str))
    except IndexError as e:
        return("В выражении {} допущена синтаксическая ошибка".format(ex_str))
    except ArithmeticError as e:
        return("При вычислении {} допущена арифметическая ошибка {}".format(ex_str, e))
    except ValueError as e:
        return("При вычислении {} что-то пошло не так {}".format(ex_str, e))

#ааааа, здесь нет многострочных комментариев!
'''
print('1={}'.format(str(calculator("1="))))
print('2+2={}'.format(str(calculator("2+2="))))
print('2+2+2+2+2+2={}'.format(str(calculator("2+2+2+2+2+2="))))
print('2*10+1={}'.format(str(calculator("2*10+1="))))
print('2+10*1={}'.format(str(calculator("2+10*1="))))
print('2+10*1*2+9={}'.format(str(calculator("2+10*1*2+9="))))
print('6/3*2={}'.format(str(calculator("6/3*2="))))
print('2+10*1/2+9={}'.format(str(calculator("2+10*1/2+9="))))
print('2-2-2-2-2-2={}'.format(str(calculator("2-2-2-2-2-2="))))
print('2-2*12={}'.format(str(calculator("2-2*12="))))
'''