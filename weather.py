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
    'mon_low': '',
    'mon_high': '',
    'tues_low': '',
    'tues_high': '',
    'tues_conditions': '',
    'wed_low': '',
    'wed_high': '',
    'wed_conditions': '',
    'thurs_low': '',
    'thurs_high': '',
    'thurs_conditions': '',
    'fri_low': '',
    'fri_high': '',
    'fri_conditions': '',
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
        weather_data['mon_low'] = json_response['DailyForecasts'][0]['Temperature']['Minimum']['Value']
        weather_data['mon_high'] = json_response['DailyForecasts'][0]['Temperature']['Maximum']['Value']
        # tuesday
        weather_data['tues_low'] = json_response['DailyForecasts'][1]['Temperature']['Minimum']['Value']
        weather_data['tues_high'] = json_response['DailyForecasts'][1]['Temperature']['Maximum']['Value']
        weather_data['tues_conditions'] = json_response['DailyForecasts'][1]['Day']['ShortPhrase']
        # wednesday
        weather_data['wed_low'] = json_response['DailyForecasts'][2]['Temperature']['Minimum']['Value']
        weather_data['wed_high'] = json_response['DailyForecasts'][2]['Temperature']['Maximum']['Value']
        weather_data['wed_conditions'] = json_response['DailyForecasts'][2]['Day']['ShortPhrase']
        # thursday
        weather_data['thurs_low'] = json_response['DailyForecasts'][3]['Temperature']['Minimum']['Value']
        weather_data['thues_high'] = json_response['DailyForecasts'][3]['Temperature']['Maximum']['Value']
        weather_data['thurs_conditions'] = json_response['DailyForecasts'][3]['Day']['ShortPhrase']
        # friday
        weather_data['fri_low'] = json_response['DailyForecasts'][4]['Temperature']['Minimum']['Value']
        weather_data['fri_high'] = json_response['DailyForecasts'][4]['Temperature']['Maximum']['Value']
        weather_data['fri_conditions'] = json_response['DailyForecasts'][4]['Day']['ShortPhrase']

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