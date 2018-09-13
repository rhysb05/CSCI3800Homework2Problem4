# This function will allow the user to enter a binary number


class InputChecker:
	def input_integer(self):
		print("Please enter a number of any length composed for 0's and 1's only")

		# Declare a variable to store the user's input
		bin_number = ""

		# Allow the user to enter in a binary number of their choice
		input(bin_number)

		# Check to see that number entered is actually a binary number

		# We use this as a boolean variable as a flag to exit
		# a while loop
		bin_num_check = 0

		while bin_num_check == 0:
			bin_number.__len__()
			print(bin_number.__len__())





print("Welcome!!")
print("This program calculates the value of any binary number that you enter")

# Declare an object with which to run my function
myCheck = InputChecker()

# Call function that will execute the assigned task
myCheck.input_integer()




