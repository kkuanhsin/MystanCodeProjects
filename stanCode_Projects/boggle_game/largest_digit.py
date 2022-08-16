"""
File: largest_digit.py
Name:官欣
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def helper_find_largest_digit(n, maxi):
	"""
	:param n: int, the number you want to find largest digit
	:param maxi: the start max number
	:return: max digital
	"""
	# change negative number to positive
	if n < 0:
		n *= -1

	# last digital
	if n == 0:

		# return the max digital
		return maxi

	else:
		# get the last digital of the number
		r = n % 10

		# find maxi
		if r > maxi:
			maxi = r

		# remove the last digital
		return helper_find_largest_digit(n//10, maxi)


def find_largest_digit(n):
	"""
	:param n: int, the number you want to find largest digit
	:return: helper function
	"""
	return helper_find_largest_digit(n, -float('inf'))


if __name__ == '__main__':
	main()
