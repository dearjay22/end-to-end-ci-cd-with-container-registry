# Calculator.py
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero not allowed")
    return a / b

def main():
    print("Welcome to the Advanced Calculator (CLI)")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit")

    while True:
        op = input("Enter operation: ").strip().lower()
        if op == 'exit':
            print("Goodbye!")
            break
        if op not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if op == 'add':
                print("Result:", add(a, b))
            elif op == 'subtract':
                print("Result:", subtract(a, b))
            elif op == 'multiply':
                print("Result:", multiply(a, b))
            elif op == 'divide':
                print("Result:", divide(a, b))
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
