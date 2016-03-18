# Run the script to start using it
# Put new things into the list, one at a time
# Enter the word DONe - in all caps - to quit the program
# And, once I quit, I want the app to show me everythign that's on my list

shopping_list = []


def print_list():
	for item in shopping_list:
		print("* {}".format(item))

def quit():
	print_list()
	exit()

def get_user_input():
	user_input = input("Enter a new item: ")
	if user_input == "DONE":
		quit()
	elif user_input == "SHOW":
		print_list()
		get_user_input()
	elif user_input == "HELP":
		print("instructions for idiots:")
		print("SHOW: Shows the shit (duhh)")
		get_user_input()
	elif user_input.startswith("DEL "):
		item_to_delete = user_input[4:]
		shopping_list.remove(item_to_delete)
		# print_list()
		get_user_input()
	else:
		shopping_list.append(user_input)
		# print_list()
		get_user_input()

get_user_input()
