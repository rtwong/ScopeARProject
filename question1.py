def print_tree(height):
	"""
	Answer to question 1, prints a christmas tree of stars with a given height.
	"""
	# check if input is an int, a float, or garbage data
	# use int, ignore float and garbage data, careful not to use a float as an int, easy to do in python
	try:
		height = int(height)
	except:
		raise ValueError("Invalid, input is not an integer.")


	# check if we can even draw a tree
	if height <= 0:
		raise ValueError("Invalid input, height is 0 or negative.")

	for current_height in range(height):
		# print leading spaces
		print(" " * (height - current_height - 1), end="")
		# print stars
		print("*" * (current_height*2 + 1))

	return 1


user_input = input("Input a height, positive integers only: ")
print_tree(user_input)
