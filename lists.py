#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 31st, 2022.
# This program calculates the average of the elements in the list. It then
# displays it to the user and the elements in the list.


# this function calculates the average marks of the elements in the list.
def calc_average(list_of_marks):
    if len(list_of_marks) == 0:
        return -1
    else:
        sum = 0
        for a_num in list_of_marks:
            sum = sum + a_num
            average = sum / len(list_of_marks)
    return average


def main():
    # create a list
    list_of_float = []
    mark_num = None

    while mark_num != "-1":

        # gets user input
        mark_num = input("Please enter a mark, or -1 to stop: ")

        try:
            # convert from a string to a float
            mark_int = float(mark_num)

            # sets a range to check for valid entry
            if mark_int < -1:
                print("Please enter a positive integer.")
                continue
            list_of_float.append(mark_int)

        # handles error case
        except Exception:
            print("{} is not a valid mark.".format(mark_num))

    # removes the last element
    list_of_float.pop()

    # calls function
    average_mark = calc_average(list_of_float)

    # displays results to user
    print("For the lists of marks: {}".format(list_of_float))
    print("The average is: {:,.1f}".format(average_mark))


if __name__ == "__main__":
    main()
