import Weather_JSON_Data
import MySQL
import schedule
import time

def task():
    # city = input("Input a city name : ")

    json_data = Weather_JSON_Data.get_data('Almaty')


    id = json_data['id']
    name = json_data['name']
    temp = json_data['main']['temp']
    wind_speed = json_data['wind']['speed']
    weather_id = []
    description = []

    for i in json_data['weather']:
        weather_id = i['id']
        description = i['description']

    print(id,"   ", name,"   ", temp)
    # MySQL.insert('python_test_db', id, weather_id, name, description, temp, wind_speed)



# for i in MySQL.select('python_test_db'):
#     print(i)

# MySQL.cursor.close()

schedule.every(1).days.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)