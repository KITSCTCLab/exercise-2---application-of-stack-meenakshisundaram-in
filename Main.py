import operator
stack = []
expression = input("Enter the expression : ")
for x in expression:
    if x=="+" or x=="-" or x=="/" or x=="*" or x=="%" or x=="**":
        value1=stack.pop()
        value2=stack.pop()
        operators_dictionary = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv,"%":operator.mod,"**":operator.pow}
        stack.append(operators_dictionary[x](value2,value1))
    else:
        stack.append(int(x))
for x in stack:
    print(x)
