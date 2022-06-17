
#You have a rectangle plate where height and width are user inputs.
#Then you have to calculate how many Misti can be kept on the plate.

"""
misti plate->height & width
output: total misty

"""
print("Arnob Reduan")
print('--------------------------------------')
misti_plate_height = int(input("Enter Height: "))  # 2
misti_plate_width = int(input("Enter Width: "))  # 2
sum = misti_plate_height * misti_plate_width  # 4
isSumIsNotZero = True


while isSumIsNotZero:
    misti_plate_width = 1
    misti_plate_height -=1


    #isSumIsNotZero = False
    sum +=misti_plate_width * misti_plate_height
    isSumIsNotZero = False
# #
print(sum)
