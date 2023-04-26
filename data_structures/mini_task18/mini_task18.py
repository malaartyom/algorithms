from mini_task20 import stack
possible_signs = [("**", 1, 0), ("*", 2, 1), ("/", 2, 1), ("%", 2, 1), ("+", 3, 1), ("-", 3, 1), ("<<", 4, 1), (">>", 4, 1), ("&", 5, 1), \
                  ("^", 6, 1), ("|", 7, 1), ("!", 8, 0), ("&&", 9, 1), ("||", 10, 1)]
signs = []
priority = []
associativity = []
for i in possible_signs:
    priority.append(i[1])
    signs.append(i[0])
    associativity.append(i[2])

def is_sign(char):
    return char in signs


def parse(expression):
    expression = list(expression)
    return_array = []
    string = ""

    for i in range(len(expression)):
        if i > 0:
            prev = expression[i - 1]
        if expression[i].isdigit():
            string += expression[i]
        else:
            if len(string) != 0:
                return_array.append(string)

            string = ""

            if expression[i] == "&" and prev == "&":
                return_array.pop()
                return_array.append(expression[i] + prev)

            elif expression[i] == "|" and prev == "|":
                return_array.pop()
                return_array.append(expression[i] + prev)

            elif expression[i] == "<" and prev == "<":
                return_array.pop()
                return_array.append(expression[i] + prev)

            elif expression[i] == ">" and prev == ">":
                return_array.pop()
                return_array.append(expression[i] + prev)
                
            elif expression[i] == "*" and prev == "*":
                return_array.pop()
                return_array.append(expression[i] + prev)

            else:
                return_array.append(expression[i])
    
    if len(string) != 0:
        return_array.append(string)
    return return_array
        

def polish(expression):
    a = stack()
    output_string = ""
    for i in expression:
        if i.isdigit():
            output_string += i + " "
        elif is_sign(i):
            index = signs.index(i)
            if a.empty() or a.peek() == "(":
                a.push(i)
            else:
                if (priority[signs.index(a.peek())] < priority[index]) or ((priority[signs.index(a.peek())] == priority[index]) and associativity[index] == 1):
                    top = a.pop()
                    output_string += top + " "
                    a.push(i)
                else:
                    a.push(i)
        elif i == "(":
            a.push(i)
        elif i == ")":
            while a.peek() != "(":
                top = a.pop()
                output_string += top + " "
            a.pop()

    while not(a.empty()):
        top = a.pop()
        output_string += top + " "

    return output_string
                    

def main(expression):
    a = parse(expression)
    b = polish(a)
    return b





        
