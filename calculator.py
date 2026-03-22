history= "history.txt"

def show():
    file = open(history, "r")
    lines = file.readlines()
    if len(lines) == 0 : 
        print("No histary found ...")
    else :
        for line in reversed(lines):
            print(line.strip())
    file.close()


def clear_history():
    with open(history,"w") as file :
        file.write("")
    print("file is cleared !!!!")

def stor(equation, result):
    file = open(history,"a")
    file.write(equation + "=" + str(result)+"\n")
    file.close()

def calculation(equation):
    parts = equation.split()
    if len(parts) != 3:
        print("Invalid equation format. Please use 'number operator number' format.")
        return None
    
    num1 = float(parts[0])
    opp = (parts[1])
    num2 = float(parts[2])

    if opp =="+" :
        return num1+num2
    elif opp == "-":
        return num1-num2
    elif opp == "*" :
        return num2*num1 
    elif opp == "/":
        if num1== 0 or num2 == 0 :
            return None
        return num1/num2
    else :
        print("invalid operater use only (+,-,*,/)")
        return 
    
    if int(result) ==  result :
        result = int(result)
    print("result =",result)
    stor(user_input,result)

def main():
    print("<-------------welcome to calculator type (history,clearor exit ) ---------------->")
    while True :
        user_input= input("enter calcutation (+,-,*,/) or (history,clear,exit) : ").strip()
        if user_input.lower() == "history":
            show()
        elif user_input.lower() == "clear":
            clear_history()
        elif user_input.lower() == "exit":
            print("thank you for using calculator")
            break
        else :
            result = calculation(user_input)
            if result is not None :
                print("result =",result)
                stor(user_input,result)

main()
