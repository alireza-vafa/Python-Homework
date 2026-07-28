"""
Phone-book functions for phone_book_gui
"""


def create_contact(name, family, number, info):
    """Normalize input values and return a contact dictionary."""
    return {
        "name": name.strip().lower(),
        "family": family.strip().lower(),
        "number": int(number),
        "info": info.strip().lower(),
    }


def find_number_by_attribute(phone_list, attribute, attribute_searched):
    """
    Return contacts whose name or family matches the search value.
    """
    search_value = attribute_searched.strip().lower()

    if attribute not in {"name", "family"}:
        return None

    result = []
    for phone in phone_list:
        if phone[attribute] == search_value:
            result.append(phone)

    return result


def duplicate_check(phone_list, phone_new):
    """
    Return False if the contact duplicates an existing number or identity.
    """
    for phone in phone_list:
        if phone["number"] == phone_new["number"]:
            return False

        if (
            phone["name"] == phone_new["name"]
            and phone["family"] == phone_new["family"]
            and phone["info"] == phone_new["info"]
        ):
            return False

    return True


def show_list(phone_list):
    """Print contacts as a formatted table."""
    print("-----------------------------------------------------------")
    print(f"{'Name':10}\t{'Family':10}\t{'Number':10}\t{'Info':10}")
    print("-----------------------------------------------------------")

    for phone in phone_list:
        print(
            f"{phone['name']:10}\t"
            f"{phone['family']:10}\t"
            f"{phone['number']:<10}\t"
            f"{phone['info']:10}"
        )

    print("-----------------------------------------------------------")