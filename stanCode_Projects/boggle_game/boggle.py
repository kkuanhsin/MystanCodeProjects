"""
File: boggle.py
Name:官欣
----------------------------------------

"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	# a list to store the letter you input
	letter_lst = []

	# ask user to input four times and each time 4 letters and 3 blocks
	for i in range(4):
		word = input(f'{i+1} row of letters: ').lower()

		if len(word) != 7 or word[1] != ' ' or word[3] != ' ' or word[5] != ' ':
			print('Illegal input')
			break

		# make the letter you input 4*4
		word_lst = []
		for j in range(len(word)):
			if word[j].isalpha():
				word_lst.append(word[j])

		letter_lst.append(word_lst)

	start = time.time()

	check_lst = read_dictionary(letter_lst)
	count = boggle(letter_lst, check_lst)

	end = time.time()
	print(f"There are {count} words in total.")

	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(letter_lst, check_lst):
	"""
	:param letter_lst: 16 letters you input
	:param check_lst: the word in dictionary
	:return: the len of the ans
	"""
	ans_lst = []
	# choose starting point
	for x in range(4):
		for y in range(4):
			path = [(x, y)]
			ans = letter_lst[x][y]
			cur_pos = (x, y)
			boggle_helper(letter_lst, ans_lst, check_lst, ans, path, cur_pos)

	return len(ans_lst)


def boggle_helper(letter_lst, ans_lst, check_lst, ans, path, cur_pos):
	# base case
	if len(ans) >= 4:
		if ans in check_lst:
			if ans not in ans_lst:
				ans_lst.append(ans)
				print(f'found: {ans}')

	# find neighbor
	cur_x, cur_y = cur_pos
	for i in range(-1, 2, 1):
		for j in range(-1, 2, 1):
			# next x
			next_x = cur_x + i
			# next y
			next_y = cur_y + j

			# check if next_x and next_y and use or not
			if (next_x, next_y) not in path:
				if 0 <= next_x < 4 and 0 <= next_y < 4:
					ans += letter_lst[next_x][next_y]
					cur_pos = (next_x, next_y)
					path.append(cur_pos)

					# explore
					if has_prefix(ans, check_lst):
						boggle_helper(letter_lst, ans_lst, check_lst, ans, path, cur_pos)

					# un-choose
					ans = ans[:-1]
					path.pop()


def read_dictionary(letter_lst):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	check_lst = []
	with open(FILE, 'r') as f:
		for line in f:
			if len(line.strip()) >= 4:
				check_lst.append(line.strip())

	return check_lst


def has_prefix(sub_ans, check_lst):
	"""
	:param sub_ans: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param check_lst : words in dict to check
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in check_lst:
		if word.startswith(sub_ans):
			return True


if __name__ == '__main__':
	main()
