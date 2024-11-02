# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(group_1, group_2, razdel = ','):
    common_participants = set(group_1.split(razdel)).intersection(set(group_2.split(razdel)))
    return list(common_participants)

group = find_common_participants(participants_first_group, participants_second_group, razdel= '|')
print(sorted(group))