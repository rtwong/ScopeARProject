def print_tree(height):
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


	# check if we can even draw a tree
	if height <= 0:
		print("Invalid input, height is 0 or negative.")
		return

	if height == 1:
		print("What a sad tree.")

	for current_height in range(height):
		# print leading spaces
		print(" " * (height - current_height - 1), end="")
		# print stars
		print("*" * (current_height*2 + 1))


user_input = input("Input a height, positive integers only: ")
print_tree(user_input)
