from phone_class import Phone


phone_list = []


while True:

    print()
    print("1) Add contact")
    print("2) Find by name")
    print("3) Find by family")
    print("4) Show phone list")
    print("0) Exit")

    option = int(input("\nChoose an option: "))

    if option == 0:
        break

    elif option == 1:

        name = input("Name: ")
        family = input("Family: ")
        number = int(input("Phone #: "))
        information = input("Information: ")

        phone = Phone(name, family, number, information)

        duplicate = False

        for person in phone_list:

            if person.number == phone.number:
                duplicate = True

            elif (
                person.name == phone.name
                and person.family == phone.family
                and person.information == phone.information
            ):
                duplicate = True

        if duplicate:
            print("Duplicate contact!")

        else:
            phone_list.append(phone)
            print("Saved!")

    elif option == 2:

        name = input("Enter name: ").lower()

        print("\nName      Family      Number      Information")
        print("-----------------------------------------------")

        for person in phone_list:
            if person.name == name:
                print(person)

    elif option == 3:

        family = input("Enter family: ").lower()

        print("\nName      Family      Number      Information")
        print("-----------------------------------------------")

        for person in phone_list:
            if person.family == family:
                print(person)

    elif option == 4:

        print("\nName      Family      Number      Information")
        print("-----------------------------------------------")

        for person in phone_list:
            print(person)