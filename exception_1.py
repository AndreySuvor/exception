import json

def get_information(x):
    try:
        with open(x) as file:
            try:
                data = json.load(file)
                print(data)
            except:
                print('Ошибка при десериализации')
    except:
        print('Файл не найден')

get_information(input()) 