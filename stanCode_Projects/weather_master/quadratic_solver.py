"""
File: quadratic_solver.py
Name:官欣
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


import math


def main():
	"""
	a: int, the number be entered
	b: int, the number be entered
	c: int, the number be entered
	Give me a,b,and c of ax^2 + bx + c = 0,it will solve the answer of x,
	and tell you how many roots it have.
	"""
	print('stanCode Quadratic Solver!')
	print("ax*x+bx+c=0 Let's find x!")
	a = int(input('Enter a= '))
	b = int(input('Enter b= '))
	c = int(input('Enter c= '))
	dis = b*b-4*a*c
	# discriminant will know how many roots
	if dis >= 0:
		sqr = math.sqrt(dis)
		x1 = (-b+sqr)/(2*a)
		x2 = (-b-sqr)/(2*a)
		# x1 and x2 is the formula of x
		if dis > 0:
			print('Two roots: ', end='')
			print(str(x1) + "," + str(x2))
		else:
			print('One root: ', end='')
			print(str(x1))
	else:
		print('No real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
