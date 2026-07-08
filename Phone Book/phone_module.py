"""
This module consist of the following functions according to the required main "phone_book" prgram:

	1- show_menu_options()
	2- input_phone_details()
	3- find_number_by_attribute(phone_list, attribute, attribute_searched):
	4- show_list(phone_list)
	5- duplicate_check

"""
###############################################33
def show_menu_options():

	print("\n1) Add contact\n2) Find by name\n3) Find by family\n4) Show phone list\n0) Exit\n ")

###############################################
def input_phone_details():

	name_new = input("Name: ").lower()
	family_new = input("Family: ").lower()
	phone_number_new = int(input("Phone #: "))
	information_new = input("Mobile number/work/home: ").lower()

	phone_new = {"name":name_new, "family":family_new, "number": phone_number_new, "info": information_new }
	print(phone_new)
	return (phone_new)

###############################################

def find_number_by_attribute(phone_list, attribute, attribute_searched):

	"""This function will search amonge the phone_list respect to two requested attributes of "name" or "family",
	i try to generalize the search in one function!"""

	searched_name_list = []
	searched_family_list = []

	if attribute == "name":
			for phone in phone_list:
				if phone["name"] == attribute_searched.lower():
					searched_name_list.append(phone)
			return searched_name_list	

	elif attribute == "family":
			for phone in phone_list:
				if phone["family"] == attribute_searched.lower():
					searched_family_list.append(phone)
			return searched_family_list
	else:
		return None
			
###############################################
def show_list(phone_list):
	print("Name      \tFamily   \tPhone     \tInformation")
	print("--------------------------------------------------------------")
	for phone in phone_list:
		print(f"{phone["name"]:10}\t{phone["family"]:10}\t{phone["number"]:<10}\t{phone["info"]:10}")
	print("--------------------------------------------------------------")

###############################################
def duplicate_check(phone_list, phone_new):

	"""first the function check the duplication of a new "number" which is obviously the first check point for a phone book,
	then it will go through check the remaining attributes of a person, which is the second check to not enter two idendical characteristics
	two different numbers with same info, if all of these steps pass, the function release a True boolean for the desired appending action in
    the main program!"""

	for phone in phone_list:

		if phone["number"] == phone_new["number"]:
			return False

		if  (phone["name"] == phone_new["name"]
			and phone["family"] == phone_new["family"]
			and phone["info"] == phone_new["info"]):
			return False
	else:
		return True


