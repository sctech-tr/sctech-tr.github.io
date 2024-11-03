print("Welcome to the Calculator!")
try:
    expr = input("Enter expression (e.g., 2 + 2): ")
    result = eval(expr)
    print("Result:", result)
except Exception as e:
    print("Error:", e)