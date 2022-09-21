# Messages
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

messages = ["Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]

# Operations
operations = ["+", "-", "*", "/"]

# Result
result = 0

# Memory
memory = 0

# States
to_continue = True
to_store = True

# Message index
msg_index = 0


def ask_question():
    global msg_index
    global result
    global memory

    msg_index = 0
    while True:
        print(messages[msg_index])
        answer = input()
        if answer == "y":
            if msg_index < 2:
                msg_index += 1
            else:
                memory = result
                break
        elif answer != "n":
            continue
        else:
            break


def is_one_digit(value):
    if -10 < value < 10 and value.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6

    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


while to_continue:
    to_store = True

    print(msg_0)
    calc = input()
    x, oper, y = calc.split()

    if x == "M" and y == "M":
        x = memory
        y = memory
    elif x == "M":
        x = memory
    elif y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
    else:
        if oper in operations:
            check(x, y, oper)
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            elif oper == "/" and y != 0:
                result = x / y
            else:
                print(msg_3)
                continue

            print(result)
            while to_store:
                print(msg_4)
                answer_store = input()
                if answer_store == "y":
                    if not is_one_digit(result):
                        memory = result
                    else:
                        ask_question()

                elif answer_store != "n":
                    continue

                to_store = False
                while True:
                    print(msg_5)
                    answer_continue = input()
                    if answer_continue == "y":
                        break
                    elif answer_continue != "n":
                        continue
                    else:
                        to_continue = False
                        break

        else:
            print(msg_2)
