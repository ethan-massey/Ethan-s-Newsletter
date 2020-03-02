import requests
import json
import os

# open weather map
# http://api.openweathermap.org/data/2.5/forecast?q=blacksburg,virginia&units=imperial&appid=<apikey>
OPEN_WEATHER_KEY = os.environ.get('OPEN_WEATHER_KEY')

# Accu Weather
# http://dataservice.accuweather.com/forecasts/v1/daily/5day/331254?apikey=<apikey>&language=en-us&details=true&metric=false
ACCU_KEY = os.environ.get('ACCU_KEY')


# Weather data
weather_data = {
    'summary': '',
    'day1_low': '',
    'day1_high': '',
    'day2_low': '',
    'day2_high': '',
    'day2_conditions': '',
    'day3_low': '',
    'day3_high': '',
    'day3_conditions': '',
    'day4_low': '',
    'day4_high': '',
    'day4_conditions': '',
    'day5_low': '',
    'day5_high': '',
    'day5_conditions': '',
    'sunrise': '',
    'sunset': '',
    'wind': '',
    'precip': ''
}


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def get_time(accu_time):
    time = accu_time[11:16]
    if time[0] == '0':
        time = time[1:]  # delete leading 0's
    return time
def get_weather():

    try:
        response = requests.get(
            "http://dataservice.accuweather.com/forecasts/v1/daily/5day/331254?apikey=" + ACCU_KEY + "&language=en-us&details=true&metric=false")

        json_response = response.json()

        # summary for today
        weather_data['summary'] = json_response['DailyForecasts'][0]['Day']['LongPhrase']

        # monday
        weather_data['day1_low'] = json_response['DailyForecasts'][0]['Temperature']['Minimum']['Value']
        weather_data['day1_high'] = json_response['DailyForecasts'][0]['Temperature']['Maximum']['Value']
        # tuesday
        weather_data['day2_low'] = json_response['DailyForecasts'][1]['Temperature']['Minimum']['Value']
        weather_data['day2_high'] = json_response['DailyForecasts'][1]['Temperature']['Maximum']['Value']
        weather_data['day2_conditions'] = json_response['DailyForecasts'][1]['Day']['ShortPhrase']
        # wednesday
        weather_data['day3_low'] = json_response['DailyForecasts'][2]['Temperature']['Minimum']['Value']
        weather_data['day3_high'] = json_response['DailyForecasts'][2]['Temperature']['Maximum']['Value']
        weather_data['day3_conditions'] = json_response['DailyForecasts'][2]['Day']['ShortPhrase']
        # thursday
        weather_data['day4_low'] = json_response['DailyForecasts'][3]['Temperature']['Minimum']['Value']
        weather_data['day4_high'] = json_response['DailyForecasts'][3]['Temperature']['Maximum']['Value']
        weather_data['day4_conditions'] = json_response['DailyForecasts'][3]['Day']['ShortPhrase']
        # friday
        weather_data['day5_low'] = json_response['DailyForecasts'][4]['Temperature']['Minimum']['Value']
        weather_data['day5_high'] = json_response['DailyForecasts'][4]['Temperature']['Maximum']['Value']
        weather_data['day5_conditions'] = json_response['DailyForecasts'][4]['Day']['ShortPhrase']

        # sunrise
        weather_data['sunrise'] = get_time(json_response['DailyForecasts'][0]['Sun']['Rise']) + 'am'
        # sunset
        sunset = get_time(json_response['DailyForecasts'][0]['Sun']['Set']).split(':')
        weather_data['sunset'] = str(int(sunset[0]) - 12) + ':' + sunset[1] + 'pm'
        # wind
        weather_data['wind'] = str(json_response['DailyForecasts'][0]['Day']['Wind']['Speed']['Value']) + 'mph ' + \
               json_response['DailyForecasts'][0]['Day']['Wind']['Direction']['Localized']
        # precipitation
        weather_data['precip'] = str(json_response['DailyForecasts'][0]['Day']['PrecipitationProbability']) + '%'


    except:
        print("ERROR: AccuWeather API could not be contacted. Check call limit. Or, check JSON parsing.")