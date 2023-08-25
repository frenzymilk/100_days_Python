import art



def add(n1, n2):
	return n1 + n2

def substract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

operations = {
	"+": add,
	"*": multiply,
	"/": divide,
	"-": substract
}

def calculator():
	print(art.logo)
	num1 = float(input("What is the first number? "))
	for key in operations:
		print(key)

	continue_calculation = True

	while continue_calculation:
		operation = input("Pick an operation : ")
		num2 = float(input("What is the next number? "))
		answer = operations[operation](num1, num2)
		print(f"{num1} {operation} {num2} = {answer}")

		user_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart calculation.:")
		if user_input == "y":
			num1 = answer
		else:
			continue_calculation = False
			calculator()

calculator()