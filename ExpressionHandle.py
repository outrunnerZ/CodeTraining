class ExpressionHandle:
    # ^ > (* or /) > (+ or -)
    # Postfix Expression convert to the Infix Expression
    def convertPostfix2Infix(self,postfix):
        if (postfix==''):
            return 'invalid'
        stack = Stack()
        for char in postfix:

            if(not self.isValiableCharacter(char)):
                return 'invalid'
            else:
                if (char == '+' or char == '-'):
                    if(stack.size()<2):
                        return 'invalid'
                    rightIntermediate = stack.pop()
                    leftIntermediate = stack.pop()
                    newExpr = leftIntermediate.expr + char + rightIntermediate.expr
                    stack.push(Intermediate(newExpr,char))
                elif(char =='*' or char =='/'):
                    if (stack.size() < 2):
                        return 'invalid'
                    leftExpr=''
                    rightExpr=''
                    rightIntermediate = stack.pop()
                    leftIntermediate = stack.pop()
                    if (rightIntermediate.oper == "+" or rightIntermediate.oper == "-"):
                        rightExpr = "(" + rightIntermediate.expr + ")"
                    else:
                        rightExpr = rightIntermediate.expr

                    if (leftIntermediate.oper == "+" or leftIntermediate.oper == "-"):
                        leftExpr = "(" + leftIntermediate.expr + ")"
                    else:
                        leftExpr = leftIntermediate.expr


                    newExpr = leftExpr + char + rightExpr;
                    stack.push(Intermediate(newExpr, char))
                # AB+AB+^=(A+B)^(A+B)
                elif(char == '^'):
                    if (stack.size() < 2):
                        return 'invalid'
                    leftExpr = ''
                    rightExpr = ''
                    rightIntermediate = stack.pop()
                    leftIntermediate = stack.pop()

                    if (leftIntermediate.oper == ""):
                        leftExpr = leftIntermediate.expr
                    else:
                        leftExpr = "(" + leftIntermediate.expr + ")"

                    if (rightIntermediate.oper == "" ):
                        rightExpr = rightIntermediate.expr
                    else:
                        rightExpr = "(" + rightIntermediate.expr + ")"
                    newExpr = leftExpr + char + rightExpr;
                    stack.push(Intermediate(newExpr, char))
                else:
                    stack.push(Intermediate(char, ''))

        return stack.peek().expr




    def isValiableCharacter(self, char ):
        if(char.isdigit()):
            return True
        elif(char.isalpha()):
            return True
        elif (char == '+'):
            return True

        elif (char == '-'):
            return True

        elif (char == '*'):
            return True
        elif (char == '/'):
            return True
        elif (char == '^'):
            return True
        else:
            return False

class Intermediate:
    expr=''
    oper=''
    def __init__(self,expr,oper):
        self.expr = expr
        self.oper = oper

class Stack(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

#Test
if __name__ == '__main__':
    expressionHandle = ExpressionHandle()
    res = expressionHandle.convertPostfix2Infix('')
    print(res)
    res = expressionHandle.convertPostfix2Infix('AB*CD*^')
    print(res)
    res = expressionHandle.convertPostfix2Infix('AB*CD*^-')
    print(res)
    res = expressionHandle.convertPostfix2Infix('AB*CD*^')
    print(res)
    res = expressionHandle.convertPostfix2Infix('AB*CD*^=')
    print(res)

    res = expressionHandle.convertPostfix2Infix('AB3+^')
    print(res)


