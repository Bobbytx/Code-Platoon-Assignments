import sys

def calculate(num1, num2, operation):
    ret = 0
    if operation == "add":
        ret = num1 + num2
    elif operation == "subtract":
        ret = num1 - num2
    elif operation == "multiply":
        ret = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            ret = num1 / num2
        else:
            raise ValueError("Cannot divide by zero")
    print('Result:',ret)
    return ret

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: calculator.py <num1> <num2> <operation>")
        sys.exit(1)

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    operation = sys.argv[3]

    result = calculate(num1, num2, operation)
    print(f"Result: {result}")