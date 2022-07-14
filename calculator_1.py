

# calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
    
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer} ")

operation_symbol = input("Pick an operation from the line above: ")
num3 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]

# --------------- BUGGED Calculation ------------------
second_answer = calculation_function(calculation_function(num1, num2), num3)
# <---- bugged because here it uses num1 = 3, num2 = 2, calculation_function = "*", num3 = 3
print(f"{first_answer} {operation_symbol} {num3} = {second_answer} ")   
# why Gives -- 5 * 3 = 18 ^^^ above comment explain why
"""
# -----------It gives BUG in result-----------------
    What's the first number?: 3
+
-
*
/
Pick an operation from the line above: +
What's the second number?: 2
3 + 2 = 5 
Pick an operation from the line above: *
What's the next number?: 3
5 * 3 = 18 
"""

# # --------OR--------
# answer = calculation_function(answer, num3)

