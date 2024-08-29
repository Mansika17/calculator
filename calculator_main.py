from calculator_operations import add , sub , mul , div , exp , mod
print("\n Simple Calculator")
def calculator():
    while True:
        print("Select Operation")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiplication")
        print("4.Division")
        print("5.Expotential /Power")
        print("6.Modulo")
        print("7.Exit")

        c = input("Enter Operation To Be Performed(1/2/3/4/5/6/7):")
        if c == '7':
            print("Exiting !! GoodBye")
            break 
        if c in ['1','2','3','4', '5','6'] :
            x = float(input("Enter first number:"))
            y = float(input("Enter second number:"))

            if c == '1' :
                print(f"Result : {x} + {y} = {add(x,y)}")
            elif c == '2':
                print(f"Result : {x} - {y} = {sub(x,y)}")
            elif c == '3' :
                print(f"Result : {x} * {y} = {mul(x,y)}")
            elif c == '4' :
                print(f"Result : {x} / {y} = {div(x,y)}")
            elif c == '5':
                print(f"Result : {x} ^ {y} = {exp(x,y)}")
            elif c == '6':
                print(f"Result : {x} % {y} = {mod(x,y)}")

        else :
            print("Invalid Number. Enter A Number Between 1 To 7")


if __name__ == "__main__":
    calculator()






