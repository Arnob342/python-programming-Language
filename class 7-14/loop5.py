"""
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
-
-
-
2 x 10 = 20
"""
excepected_namta = int(input())  # 2
increment_num = 1
while increment_num <= 10:
    # print("----------------------")
    mult = excepected_namta * increment_num
    print("%d X %d = %d" % (excepected_namta, increment_num, mult))
    """
    %(excepected_namta,increment_num, mult)
    
    %d (int) - excepected_namta
    %d (int) - increment_num
    %d (int) - mult
    
    %f
    %s 
    \n 
    \t 
    """
    increment_num += 1
    # print("----------------------")

if 1 < 1:
    print("1")
    print("2")

else:
    print("3")
