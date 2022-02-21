# 1. В текстовый файл построчно записаны имя и фамилия учащихся класса и их оценки.
#Вывести на экран всех учащихся, чей средний балл меньше 5, также посчитать и вывести средний балл по классу. Так же,
#записать в новый файл всех учащихся в формате "Фамилия И.       Ср. балл":
import os

def get_person_marks_list_from_file(file_path: str) -> list:
    '''читает файл по адресу file_path'''
    with open(file_path, 'r') as f:
        data = f.readlines()
    result = [{"name": ' '.join(k[:2]), 'assessment': [int(v) for v in k[2:]]}
              for k in [i.split() for i in data]
              ]
    return result


def aver_perf(marks_list: list) -> float:
    '''вычисляет среднее арифметическое списка с округление до сотых'''
    return round(sum(marks_list) / len(marks_list), 2)


def aver_marks_list(person_marks_list: list) -> list:
    '''создает список средних оценок '''
    return [aver_perf(i['assessment']) for i in person_marks_list]


def less_than_5_perf(person_marks_list: list) -> None:
    '''вывод на экран тех, у кого средний балл меньше 5,а также среднего балла всей группы'''
    for i in person_marks_list:
        if aver_perf(i['assessment']) < 5:
            print(f"{i['name']}".ljust(30), aver_perf(i['assessment']))
    print('Средний балл группы:'.ljust(30), aver_perf(aver_marks_list(person_marks_list)))


def create_aver_marks_dict(person_marks_list: list) -> dict:
    '''создает словарь в формате "Фамилия И": "Ср. балл"'''
    aver_mark_dict = {}
    for idx, val in enumerate(person_marks_list):
        last_n, first_n = val['name'].split()
        aver_mark_dict[' '.join((first_n, last_n[0] + '.'))] = aver_marks_list(person_marks_list)[idx]
    return aver_mark_dict


def create_file_for_person(aver_mark_dict: dict, res_folder: str) -> None:
    '''записываем построчно в файл из словаря в формате  "Фамилия И.       Ср. балл" с созданием папки'''
    os.makedirs(res_folder, exist_ok=True)
    with open(os.path.join(res_folder, 'pers_aver_marks.txt'), 'w') as f:
        f.writelines(f'{k}'.ljust(18) + f'{v}\n' for k, v in aver_mark_dict.items())


person_marks_list = get_person_marks_list_from_file('test\educ_perf.txt')

less_than_5_perf(person_marks_list)

aver_mark_dict = create_aver_marks_dict(person_marks_list)

create_file_for_person(aver_mark_dict, 'test\pers_aver_marks')


# 2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь. Окончанием ввода пусть служит
# пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.


def create_input_str_file(file_path: str) -> None:
    st = input()
    with open(file_path, 'w') as f:
        while st:
            f.writelines(st + "\n")
            st = input()


create_input_str_file('test\input.txt')


