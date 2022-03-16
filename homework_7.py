import requests
import os
import random
import csv


USER_URL = 'https://jsonplaceholder.typicode.com/users'
TASK_URL = 'https://jsonplaceholder.typicode.com/todos'
RESULT_FOLDER = 'result'


def get_json(pk: int ) -> list:    
    res = requests.get(
              TASK_URL,
              params={
                'userId': pk
            }
            )
    res_data = res.json()
    return res_data


def create_folder(folder_name: str) -> None:
    os.makedirs(folder_name, exist_ok=True)
    

def create_csv_file() -> None:
    create_folder(RESULT_FOLDER)
    response = requests.get(USER_URL)
    response_data = response.json()
    
    for username in response_data:
        json_id_list = get_json(username['id'])
        with open(os.path.join(RESULT_FOLDER, f'{username["username"]}.csv'), 'w') as csv_file:
            fieldnames = ['id', 'title', 'completed']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in json_id_list:
                row.pop('userId')
                writer.writerow(row)


if __name__ == '__main__':
    create_csv_file()
    print('Complete')








