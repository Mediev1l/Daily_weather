import json
from urllib.request import urlopen


class WeatherApi:

    def __init__(self):
        self.__api_id = 'gkUe3dhAeZkLA021DHZmcVcJZjJmobwg'
        self.__city_id = '274340'
        self.__source = None
        self.__data = None

        self.open()
        self.load()

    @property
    def url(self):
        return 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{}?apikey=' \
               '{}%20&language=pl-pl&details=True&metric=True'.format(self.__city_id, self.__api_id)

    @property
    def api_id(self):
        return self.__api_id

    @api_id.setter
    def api_id(self, id):
        self.__api_id = id

    @property
    def city_id(self):
        return self.__city_id

    @city_id.setter
    def city_id(self, id):
        self.__city_id = id

    @api_id.setter
    def api_id(self, id):
        self.__api_id = id

    def open(self):
        try:
            with urlopen(self.url) as request:
                self.__source = request.read()
        except:
            print('HTTP Error')

    def load(self):
        self.__data = json.loads(self.__source)

    def print(self):
        print(json.dumps(self.__data, indent=2, sort_keys=True))

    def temp_min(self):
        return self.__data['DailyForecasts'][0]['Temperature']['Minimum']['Value']

    def temp_max(self):
        return self.__data['DailyForecasts'][0]['Temperature']['Maximum']['Value']

    def real_feel_min(self):
        return self.__data['DailyForecasts'][0]['RealFeelTemperature']['Minimum']['Value']

    def real_feel_max(self):
        return self.__data['DailyForecasts'][0]['RealFeelTemperature']['Maximum']['Value']

    def day_forecast(self):
        return self.__data['DailyForecasts'][0]['Day']['LongPhrase']

    def night_forecast(self):
        return self.__data['DailyForecasts'][0]['Night']['LongPhrase']
