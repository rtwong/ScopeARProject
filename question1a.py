def print_x(height):
	# check if input is an int, a float, or garbage data
	# use int, ignore float and garbage data, careful not to use a float as an int, easy to do in python
	try:
		float_check = float(height)
		int_check = int(height)
		if float_check == int_check:
			height = int_check
	except:
		print("Invalid, input is not an integer.")
		return


	# check if it is tall enough and odd, so we can draw an X
	if height <= 2 or height%2 == 0:
		print("Invalid input, height is 2 or negative, or an even number.")
		return

	# create a list to hold spaces and stars, and move stars according to their height
	# one moves up an index every loop, one moves back every loop. 
	for i in range(height):
		line = [" "] * height
		line[i] = "*"
		line[height - 1 - i] = "*"
		print("".join(line))


user_input = input("Input a height, positive, odd integers only: ")
print_x(user_input)
