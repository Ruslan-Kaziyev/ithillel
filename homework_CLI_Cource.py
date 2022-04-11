import requests
from bs4 import BeautifulSoup
from datetime import date,datetime,timedelta
import sys
import json


cur = sys.argv[1].upper()
EXC_PROV = 'Курсы конвертации платежной системы Visa'

def get_print(val_1,val_2=None) -> None:
    print('-------------')
    print(val_1)
    if val_2 == None:
        print('===============')
    else:
        print()
        print(val_2)
        print('===============')

#функция поиска номера таблицы соотв. курсу банка или платеж системы 
def get_num_table(EXC_PROV: str) -> int:
    for i in range(len(tables)):    
        for table in tables[i].find('caption'):
            if EXC_PROV in table.text: 
                return i
    return 0

#создание словаря с наим валют и средним курсом покупка_продажа
def get_rate_dict(lst) -> dict:
    d={}
    for st_r in lst[1:]:
       for j,el in enumerate(st_r):
            if el.isdigit():
                rate1 = float(st_r[j:j+6].replace(',','.'))
                idx = st_r.find('%')
                rate2 = float(st_r[idx+1:idx+7].replace(',','.'))
                d[st_r[:3]] = round((rate1+rate2)/2,4)
                break
    return d

def print_res(cur,rate_dict):
    if rate_dict .get(cur,-1) == -1:
        get_print(f'Invalid currency name: {cur}')
    else:
        get_print(cur,rate_dict[cur])
               
#проверка первого аргумента(название валюты)        
if len(cur) != 3 or not cur.isalpha():
    get_print('System Error')
    sys.exit()

#проверка наличия второго аргумента(при отсутствии подставляется текущая дата)
try:
    date = sys.argv[2]
except IndexError:
    date = str(date.today())
    
#проверка даты на корректность 
try:
    datetime.strptime(date, '%Y-%m-%d')
except ValueError :
    get_print(f'Invalid date {date}')
    sys.exit()


if __name__ == '__main__':
    
    # если имеется json файл с нужной датой читаем с него данные
    try:
        with open(f'{date}.json', 'r') as in_file:
            data = json.load(in_file)
            print_res(cur,data)
            
    # в противном случае читаем данные с сайта        
    except:        
        for i in range(3):
            URL ='https://index.minfin.com.ua/exchange/archive/'+ date
            session = requests.Session()
            session.headers.update({})
            response = session.get(URL)
            soup = BeautifulSoup(response.text, 'html.parser')
            tables = soup.find_all("table",{"class":"zebra"})
            num_table = get_num_table(EXC_PROV)
            if num_table:
                break
            else:
                # если не находит на текущую дату то ищет на день назад (и так 3* попытки)
                date1 = datetime.strptime(date, '%Y-%m-%d') - timedelta(days=1)
                date = str(date1)[:10]
                
        
        if num_table:
            headers = []
            for table in tables[num_table].find_all('tr'):
                title = table.text
                headers.append(title)
                
        # при отсутствии таблицы с нужным курсом
        else:
            get_print('No exchange rate')
            sys.exit()
        
        #создание словаря с курсами валют
        rate_dict = get_rate_dict(headers)
       
        # запись в json файл с нужной датой для последущего более быстрого доступа
        with open(f'{date}.json', 'w') as out_file:
            json.dump(rate_dict, out_file)
            
        print_res(cur,rate_dict)

  

