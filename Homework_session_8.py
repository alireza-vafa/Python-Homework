lesson_list = [{"id":1, "name":"python", "unit":2},
               {"id":2, "name":"java", "unit":3},
               {"id":3, "name":"c++", "unit":5}
               ]

new_lesson = {"id":4, "name":"c#", "unit":2}


# Without using for loop
# Max. 17 creedits
# No duplicate name
# Sort by course names

# Show course list as:
# id{3} - name{10} - unit{3}
# --------------------------
# Total: Sum(course_credits)


name_list = list(map(lambda lesson: lesson["name"], lesson_list))

unit_list = list(map(lambda lesson: lesson["unit"], lesson_list))

total_units = sum(unit_list)

# Max. 17 creedits
# No duplicate name
def duplicate(new_lesson):
    return new_lesson["name"] in name_list


def check_max_17(new_lesson):
    return total_units + new_lesson["unit"] > 17


if duplicate(new_lesson):
    print("The new lesson is already chosen, duplicate lesson not allowed!\n")

if check_max_17(new_lesson):
    print("Maximum total credits will exceed 17, not allowed!\n")

def validation_check(new_lesson):
    return not(duplicate(new_lesson)) and not(check_max_17(new_lesson))


if validation_check(new_lesson):
    lesson_list.append(new_lesson)
    print("New lesson successfully added!\n")
else:
    print("New lesson is not added!\n")

# Sort by course names

name_list = list(map(lambda lesson: lesson["name"], lesson_list))
name_list.sort()
print("Sorted lesson's names:")
print(name_list)
sorted_lesson_list = sorted(lesson_list, key = lambda lesson: lesson["name"])
print("\nThe complete lesson lists sortd based on names:")
print(sorted_lesson_list)

    

# Show list
print("\nid  - name       - unit")
print("-"*23)
for lesson in lesson_list:
    print(f"{lesson["id"]:<3} - {lesson["name"]:10} - {lesson["unit"]:<3}")
print("-"*23)
print(f"Total:             {sum(list(map(lambda lesson:lesson["unit"],lesson_list)))}")
