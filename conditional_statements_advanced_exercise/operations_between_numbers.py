number_one = int(input())
number_two = int(input())
operator = input()

result = 0
even_or_odd = ""

if operator == "+":
    result = number_one + number_two

    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    print(f"{number_one} {operator} {number_two} = {result} - {even_or_odd}")

if operator == "-":
    result = number_one - number_two

    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    print(f"{number_one} {operator} {number_two} = {result} - {even_or_odd}")

if operator == "*":
    result = number_one * number_two

    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    print(f"{number_one} {operator} {number_two} = {result} - {even_or_odd}")

if operator == "/" and number_two != 0:
    result = number_one / number_two
    print(f"{number_one} / {number_two} = {result:.2f}")
elif operator == "/" and number_two == 0:
    print(f"Cannot divide {number_one} by zero")
if operator == "%" and number_two != 0:
    result = number_one % number_two
    print(f"{number_one} % {number_two} = {result}")
elif operator == "%" and number_two == 0:
    print(f"Cannot divide {number_one} by zero")
