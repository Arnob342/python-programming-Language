ans = []

total_nums_of_input = int(input("Total number of input: "))

# Input Data into list
while total_nums_of_input > 0:
    num = int(input())
    ans.append(num)
    total_nums_of_input = total_nums_of_input - 1

for index in range(len(ans)):
    ans.append(ans[index])

print(ans)
