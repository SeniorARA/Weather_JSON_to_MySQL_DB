import requests
import json


def get_data(city):
        api_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=043b2302061297d7c60e6940d26776d5&units=metric'.format(city)

        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                json_data = response.text

                data = json.loads(json_data)

                return data

        except requests.ConnectionError as err:
             return(err)



