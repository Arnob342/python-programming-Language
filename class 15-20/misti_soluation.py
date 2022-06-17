#You have a rectangle plate where height and width are user inputs.
# Then you have to calculate how many Misti can be kept on the plate.
"""
misti plate->height & width
output: total misty

"""
misti_plate_height = int(input("enter height"))
misti_plate_width = int(input("enter width"))
sum = misti_plate_height * misti_plate_width
issumIsNotzero = True


while issumIsNotzero:
    misti_plate_height -= 1
    misti_plate_width -= 1

    sum+=(misti_plate_height*misti_plate_width)
    #print(sum)
    #if sum.__eq__(0):
       issumIsNotzero = False
    ##
print(sum)
