###################################11111111111
print('Задание 1')
print()

n =  1003040660000
n_st = str(n)
count = 0
for i in n_st:
    if i == '0':
        count += 1
print(count)

print()
#####################################222222222222

print('Задание 2')
print()
count1 = 0
for i in reversed(n_st): # или срезом n_st[::-1]
    
    if i != '0':
        break
    
    count1 += 1
print(count1)

print()
##############################################3333333333333333

print('Задание 3')
print()


new_list = my_list_1[::2] + my_list_2[1::2]

print(new_list)

print()

#################################################444444444444

print('Задание 4')
print()

my_list  = [1,2,3,4]  
new_list = my_list[1:] + my_list[:1]       
print(new_list)

print()
###################################555555555555

print('Задание 5')
print()

my_list.append(my_list.pop(0))
print(my_list)

print() 
#####################################666666666666

print('задание 6')
print()

my_lst_2 ="43 больше чем 34 но меньше чем 56".split()
temp_lst =[]
for i in my_lst_2:
    if i.isdigit():
        temp_lst.append(int(i)) 
        
# или через генератор sum([int(i) for i in my_list_2 if i.isdigit()])

print(sum(temp_lst)
  
print()    
#################################################### 777777777
print('Задание 7')
print()
 
my_str_1 = "My long string"
l_limit = "o" 
r_limit = "g" 

l_id = 0
r_id = 0
for idx,el in enumerate(my_str_1):
    if el == l_limit and l_id == 0:
       l_id = idx
    if el == r_limit:
       r_id = idx
    
sub_str_1 = my_str_1[l_id+1:r_id]   
      
print(sub_str_1) 
print()      
#или через поиск 
l = my_str_1.find(l_limit)
r = my_str_1.rfind(r_limit)      
print(my_str_1[l+1:r])
print()
########################################################88888888888

print('Задание 8')
print()

my_str = "Documentation for Pythons"
k = 0
new_lst = []
while k < len(my_str):
    new_lst.append(my_str[k:k+2])
    k += 2
    
    if k > len(my_str):
        new_lst[(k-1)//2] = my_str[k-2] + '_'
print(new_lst)

print()
##############################################9999999999999999        

print('Задание 9')
print()

my_lst = [2,4,1,5,3,9,0,7]
k = 0
for i in range(1,len(my_lst)-1):
    if my_lst[i] >  my_lst[i-1] + my_lst[i+1]:
        k += 1
        
        print(my_lst[i] , end = ' ')
print()        
print (f'Кол_во элементов {k}')        
        
#####################################        
        
        

