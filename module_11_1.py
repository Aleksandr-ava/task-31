from requests import get, ConnectionError
import pandas as pd

params = {"ll": "37.679008,55.790393",
          "spn": "0.016457,0.00619",
          "l": "map"}
try:
    response = get("https://static-maps.yandex.ru/1.x/", params=params)
except ConnectionError:
    print("Проверьте подключение к сети.")
else:
    with open("map.png", "wb") as file:
        file.write(response.content)


city = {'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'],
        'Год основания': [1147, 1703, 1893, 1723],
        'Население': [11.9, 4.9, 1.5, 1.4]}

df = pd.DataFrame(city)

print(df)
print()


df = pd.DataFrame([[1, 'Лена', '34', 'Менеджер'],
                   [2, 'Дима', '25', 'Строитель'],
                   [3, 'Оксана', '42', 'Авто заправщица']],
                  columns=['№', 'Имя', 'Возраст', 'Профессия'])
print(df)
print()


file_name = 'Pandas.txt'
file = open(file_name, mode='w', encoding='utf8')
file_content = 'С pandas удобно составлять таблицы и импортировать файлы.'
file.write(file_content)
file.close()


df = pd.read_csv('Pandas.txt')
out = str(list(df))
out = out.replace("[", "")
out = out.replace("]", "")
out = out.replace("'", "")
print(out)
