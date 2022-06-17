list = ['A', "B", "C", "D"]

initial_index = 0
list_size = len(list)  # 4 (0-3)

while initial_index < list_size:
    print("Initial Index value - ", initial_index)
    print(list[initial_index])
    initial_index += 1
    print("After Increment Initial Index ", initial_index)
    print("------------------------------")
