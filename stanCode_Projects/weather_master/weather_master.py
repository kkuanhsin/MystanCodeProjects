"""
File: weather_master.py
Name:官欣
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	temp: int , the number of the temperature
	It will tell you the temperature you enter,which one is the highest and lowest,
	the average temperature, and how many cold days it have.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	d = 0
	n = 0
	if temp < 16:   # the day of cold days
		d += 1
	if temp == EXIT:
		print('No temperatures were entered!')
	else:
		maxi = temp
		mini = temp
		total = temp
		while True:
			temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			n += 1   # calculate how many temperatures were entered
			if temp == EXIT:
				break
			elif maxi <= temp:
				maxi = temp
			elif maxi > temp:
				maxi = maxi
			if mini <= temp:
				mini = mini
			elif mini > temp:
				mini = temp
			if temp < 16:
				d += 1
			total += temp   # plus every new temperature
		average = total/n
		print('Highest temperature =  ' + str(maxi))
		print('Lowest temperature =  ' + str(mini))
		print('Average = ' + str(average))
		print(str(d) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
