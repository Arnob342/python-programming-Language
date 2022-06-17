class Mother:
    motherName = ""

    def printMotherName(self):
        print(self.motherName)


class Father:
    fatherName = ""

    def printFatherName(self):
        print(self.fatherName)


class Child(Mother, Father):
    def parents(self):
        print("Father : ", self.fatherName)
        print("Monther : ", self.motherName)


child1 = Child()

child1.fatherName = "MR. ABM Mohit"
child1.motherName = "MRS. ABM Mohit"

child1.parents()

"""
Father :  MR. ABM Mohit
Monther :  MRS. ABM Mohit
"""
