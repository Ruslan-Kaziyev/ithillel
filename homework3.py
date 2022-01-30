#################################1 пример

my_list = [1,2,45,555,674,23,345,34,567,89,876,4545,44,5,7]

for i in my_list:
     if i > 100:    # число 100 не включаем
         print(i,end = ' ')
print()  #добавил что бы следующий вывод был с новой строки

################################# через индексы

my_list = [1,2,45,555,674,23,345,34,567,89,876,4545,44,5,7]

for i in range(len(my_list)):
    if my_list[i] > 100:
        print(my_list[i],end = ' ')
print()        
        
#################################2 пример

my_list = [1,2,45,555,674,23,345,34,567,89,876,4545,44,5,7]
my_results = []

for i in my_list:
    if i > 100:
        my_results.append(i)
print(my_results)
print()
print(*my_results)   #или без скобок

#################################3 пример

my_list = [2,4,6]

if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1]+my_list[-2])
print(my_list)
print()
    
##################################4 пример

my_string = '0123456789'
my_lst = []
for i in my_string:
    for j in my_string:
        my_lst.append(int(i+j))
print(my_lst)
print()


##################################  добавил для выводы в виде матрицы

my_string1 = '0123456789'
my_lst1 = []
k = 0
for i in my_string1:
    for j in my_string1:
        my_lst1.append(int(i+j))
        k += 1  
        if k%10 == 0:
            print(*my_lst1)
            my_lst1 = []








