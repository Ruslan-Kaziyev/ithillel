# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,
#                                           {"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
# 
#############################################    первоначальный вариант
lst = [{"name": "John", "age": 34},
       {"name": "Thomas", "age": 27},
       {"name": "Kate", "age": 45},
       {"name": "Clayton", "age": 23},
       {"name": "Tom", "age": 17},
       {"name": "Charley", "age": 51},
       {"name": "Scott", "age": 17}]
min_old = lst[0]['age']                    # инициализ. начальных значений,      
ln_name = len(lst[0]['name'])              # далее будем менять в цикле      
for i in lst:
        if min_old > i['age']:
            min_old = i['age']                   #будет хранить мин. возраст
        if ln_name < len(i['name']):
            ln_name = len(i['name'])             #будет хранить маск. длину имени

d = {key: [] for key in ['Самый молодой:','Самое длинное имя:','Средний возраст:']}#создаем словарь
sum_ = 0
 
for i in lst:
    if i['age'] == min_old:
        d['Самый молодой:'] += [i['name']]     #   добавляем всех самых молодых
            
    if len(i['name']) == ln_name:
        d['Самое длинное имя:'] += [i['name']] #   добавляем всех с самым длинным именем
        
    sum_ += i['age']
d['Средний возраст:'] = [round(sum_/len(lst),2)]  #добавляем средний возраст в словарь,округляем до сотых

for i in d:                                        #выводим на экран
    print(i,*d[i])
print()
######################################################
#######################      Добавил после занятия ,которое было 12.02.22
def out_min_old(pers):
    sort_list_old = sorted(pers, key=lambda item: item['age'])
    min = sort_list_old[0]['age']
    for i in sort_list_old:
       if i['age'] == min:
           print(i['name'],':',i['age'])

def out_max_name(pers):
    sort_list_name = sorted(pers, key=lambda item: len(item['name']),reverse = True)
    max_len = len(sort_list_name[0]['name'])
    for i in sort_list_name:
        if len(i['name'])== max_len:
            print(i['name'])
            
def average_old(pers):
    old_lst = sum([i['age'] for i in pers])/len(pers)
    return print(round(old_lst,2))     # округлил до сотых
        
out_min_old(lst)
print()
out_max_name(lst)
print()
average_old(lst)

# 2. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.    
            
a = 'abcdeioozgyyqwerty123456'
b = 'abcddeeiiooklyqwerty67890'

def com_elm_func(str1,str2):
    return list(set(str1) & set(str2)) # пересечение множеств даст символы которые есть
                                 # в обеих строках хотя бы раз
print(com_elm_func(a,b)) # вывод списка
print()

# 3. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

def com_elm_1_func(str1,str2):     
     return [j for j in                                                 #в генераторе списка используем
            [i for i in com_elm_func(str1,str2) if str1.count(i)== 1]   # функцию из предыдущего примера
             if str2.count(j)==1]                                      
   
print(com_elm_1_func(a,b))                            # передаваемые строки из предыдущего примера
print()

# 4. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.

from random import randint,choice
import string 

n = ["king", "miller", "kean","lion","coffee"]
d = ["net", "com", "ua","site"]

def email_gen(name,domains):
     return(f"""{name[randint(0,len(name)-1)]}.{randint(100,999)}@\
{''.join(choice(string.ascii_lowercase) for i in range(randint(5,7)))}.\
{domains[randint(0,len(domains)-1)]}""")

print(email_gen(n,d))


  
  
  
  
  
