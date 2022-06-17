"""
kwargs - keywords Arguments
"""


def my_class_room(**student_details):
    print(type(student_details))
    # for key, value in student_details.items(): #[key=value]
    #     print("%s ==  %s" % (key, value))
    for key in student_details:  # [key=value]
        value = student_details[key]
        print(key + " == " + value)


# powOf = 5 ** 5

my_class_room(student1="A", student2="B", student3="C", student4="D")
