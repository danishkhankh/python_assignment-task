########################################################
#Task 1: Calculate Area with Conditions
########################################################


def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        area = length * width
        return area

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

result = calculate_area(length, width)

print(result)







