nums_inner_items = int(input())

items = []

while nums_inner_items > 0:
    inner_item_list = []

    type = input()
    color = input()
    name = input()

    inner_item_list.append(type)
    inner_item_list.append(color)
    inner_item_list.append(name)

    items.append(inner_item_list)
    nums_inner_items -= 1

ruleKey = input()
ruleValue = input()


def check_rule_value(key, value, check_list=[]):
    for i in range(len(check_list)):
        if i == key:
            if check_list[i] == value:
                return True
    return False


total_match = 0
for inner_list in items:
    index = 0
    if ruleKey == "type":
        index = 0
    elif ruleKey == "color":
        index = 1
    elif ruleKey == "name":
        index = 2
    isExistRuleValue = check_rule_value(index, ruleValue, inner_list)
    if isExistRuleValue:
        total_match += 1

print(total_match)
