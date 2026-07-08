'''
Phone-book project:

This program is a phone-book, written in the format of "main body" and "phone module"
consist of the follwoing functions:

	1- show_menu_options()
	2- input_phone_details()
	3- find_by_attribute(phone_list, attribute)
	4- show_list(phone_list)
	5- duplicate_check(phone_list, phone_new)

also following menu options, details, and logics:

#######################
Phone detailes:
	1- Name
	2- Family
	3- Phone number
	4- Information (Mobile number/work/home etc.)

#######################
Menu options:
	1- Add contact
	2- Find by family
	3- Find by name
	4- Show phone list
	0- Exit

#######################
Logics:
	1- The user could enter names both in lower and upper case for registration, also in serach!

#######################
Format of phone-book report:

Name(10)	Family(10)		Number(10)		Information(10)
------------------------------------------------------------
.
.
.
------------------------------------------------------------

#######################
'''

phone_list = []
searched_name_list = []
searched_family_list = []

from phone_module import *

'''
or this way to show more clearly the functions involves:

from phone_module import (
    show_menu_options,
    input_phone_details,
    find_number_by_attribute,
    show_list,
)
'''


while True:

	show_menu_options()

	option =int(input("Please enter the option:...\n "))

	match option:

		case 0:
			break

		case 1:

			phone = input_phone_details()

			if duplicate_check(phone_list, phone):
				phone_list.append(phone)
				print("Saved!\n")
			else:
				print("Duplicate input!\n")

			print(phone_list)

		case 2:

			attribute = "name"
			name_searched = input("Enter NAME to be searched: ")
			show_list(find_number_by_attribute(phone_list, attribute, name_searched))
			
		case 3:

			attribute = "family"
			family_searched = input("Enter FAMILY to be searched: ")
			show_list(find_number_by_attribute(phone_list, attribute, family_searched))

		case 4:
			show_list(phone_list)

