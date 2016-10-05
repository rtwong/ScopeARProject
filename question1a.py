def print_x(height):
	"""
	Answer to question 1a, prints an X using stars with a given height, (height >= 3, and height is odd) 
	"""
	# check if input is an int, a float, or garbage data
	# use int, ignore float and garbage data, careful not to use a float as an int, easy to do in python
	try:
		height = int(height)
	except:
		raise ValueError("Invalid, input is not an integer.")



	# check if it is tall enough and odd, so we can draw an X
	if height <= 2 or height%2 == 0:
		raise ValueError("Invalid input, height is 2 or negative, or an even number.")


	# create a list to hold spaces and stars, and move stars according to their height
	# one moves up an index every loop, one moves back every loop. 
	for i in range(height):
		line = [" "] * height
		line[i] = "*"
		line[height - 1 - i] = "*"
		print("".join(line))

	return 1


user_input = input("Input a height, positive, odd integers only: ")
print_x(user_input)
