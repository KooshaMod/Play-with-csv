from csv import DictReader, DictWriter, writer

FILE_PATH = 'users.csv'

def menu():
	'''show menu and return the selected one'''
	while(True):
		print("---------Menu--------------")
		print("1 - add new user")
		print("2 - remove user")
		print("3 - edit user")
		print("4 - find user")
		print("5 - list of users")
		print("6 - exit")
		try:
			choice = int(input("Select ur choice via it's number: "))
			if choice < 7 and choice > 0:
				return choice
		except:
			print("enter a valid choice")


def add_new_user(name, password,des):
	# with open('users.csv', 'a') as f:
	#     csvfile = writer(f)
	#     csvfile.writerow([name, password,des])
	# print('----------user added--------')
	with open('users.csv', 'a') as f:
		csvfile = writer(f)
		csvfile.writerow([name, password,des])       
	print('----------user added--------')

def remove_user(name, password):
	'''open the file in read mode and add data to new variable and then open again in write mode and write data'''

	with open(FILE_PATH) as f:
		data = DictReader(f)
		new_data = []
		for i in data:
			if not (i['Name'] == name and i['password'] == password):
				new_data.append(i)
			else:
				print("----user has been removed---")

	with open(FILE_PATH,'w') as f:
		headers = ['Name','password','description']
		csv_writer = DictWriter(f,fieldnames=headers)
		csv_writer.writeheader()
		for i in new_data:
			csv_writer.writerow(i)

def edit_user(name, password, new_name, new_password,new_des):
	'''open file and read data and save it in a list and edit the one and write it again'''
	with open(FILE_PATH) as f:
		data = DictReader(f)
		new_data = []
		for i in data:
			if i['Name'] == name and i['password'] == password:
				new_data.append({
					'Name' : new_name,
					'password' : new_password,
					'description' : new_des
					})
				print("-----------user has been edited-----------")
			else:
				new_data.append(i)
	with open(FILE_PATH,'w') as f:
		headers = ['Name','password','description']
		csv_writer = DictWriter(f,fieldnames=headers)
		csv_writer.writeheader()
		for i in new_data:
			csv_writer.writerow(i)


def find_user(name):
	'''open the file in read mode and iterate over it and find the user and return one's description '''
	with open(FILE_PATH) as f:
		data = DictReader(f)
		for i in data:
			if i['Name'] == name:
				return i['description']
		return f"Couldn't find {name}"

def list_users():
	'''open file and print all the users'''
	with open(FILE_PATH) as f:
		csvreader = DictReader(f)
		for i in csvreader:
			print(i['Name'], i['password'], i['description'])


if __name__ == "__main__":
	choice = 0
	while(choice != 6):
		choice = menu()
		if choice == 1:
			name = input("Enter user name: ")
			p = input("Enter your password: ")
			des = input("Enter a short desctiption: ")
			add_new_user(name,p,des)
		elif choice == 2:
			name = input("Enter the username u want to remove :")
			password = input("the the password :")
			remove_user(name,password)
		elif choice == 3:
			name = input("Enter username: ")
			password = input("Enter the password: ")
			new_name = input("Enter the new user name: ")
			new_pass = input("Enter the new password: ")
			new_des = input("Enter the description: ")
			edit_user(name, password,new_name,new_pass,new_des)
		elif choice == 4:

			name = input("Enter username: ")
			print(find_user(name))
			pass
		elif choice ==5:
			list_users()

