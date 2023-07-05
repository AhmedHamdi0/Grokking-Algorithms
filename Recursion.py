# Sudo code using while loop approach
# def look_for_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("Found the Key")


# sudo code using recursion approach
# def look_for_key(main_box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)
#         elif item.is_a_key():
#             print("Found the Key")


def countdown(number):
    print(number)
    if number <= 0:
        return
    else:
        countdown(number - 1)


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

