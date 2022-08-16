"""
File: extension1_factorial.py
Name:官欣
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	n: int , the number be entered
	This program will multiply the number you enter to 1
	"""
	print('Welcome to stanCode factorial master!')
	while True:
		n = int(input('Give me a number, and I will list the answer of factorial: '))
		ans = n
		if n == EXIT:
			break
		print('Answer: ' + str(factorial(n, ans)))
	print('- - - - - - See ya! - - - - - -')


def factorial(n, ans):
	"""
	This will be like n(n-1)(n-2)...*1
	return ans : int , the ans of the factorial
	"""
	while n != 1:
		a = n - 1
		ans *= a
		n -= 1
	return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()