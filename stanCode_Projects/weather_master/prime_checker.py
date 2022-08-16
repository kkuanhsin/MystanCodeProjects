"""
File: prime_checker.py
Name:官欣
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


EXIT = -100


def main():
	"""
	n: int, the number be entered
	This program will tell you the number you input is prime or not.
	"""
	print('Welcome to the prime checker!')
	while True:
		n = int(input('n: '))
		a = 2
		nn = n - 1
		if n == EXIT:
			print('Have a good one!')
			break
		elif n == 1 or n == 2 or n == 3:
			# Boundary conditions
			print(str(n) + ' is a prime number')
		elif n % a != 0:
			# if n is odd
			while a < n:
				# Test from 2 to the (number - 1)
				if n % a == 0:
					# there is one or more factor
					print(str(n) + ' is not a prime number')
					break
				else:
					# a will plus 1 and try again if no factor
					a += 1
				if a == nn:
					print(str(n) + ' is a prime number')
		elif n % a == 0:
			# if n is even
			print(str(n) + ' is not a prime number')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
