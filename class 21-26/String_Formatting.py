country = "Bangladesh"
print(country)

print("My Country is ", country)

print("Country name is %s" % country)


studentName = "Hasan"
studentAge = 20
studentContactNumber = "0144114"

studentDetails = f"Student name is {studentName}, age {studentAge}" \
                 f" contactNumber {studentContactNumber}".format(studentName, studentAge, studentContactNumber)

print(studentDetails)

