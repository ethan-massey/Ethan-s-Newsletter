import requests

quote_data = {
    'quote': 'QUOTE_ERROR',
    'author': ''
}

def get_quote():
    try:
        response = requests.get("https://quotes.rest/qod.json")
        json_response = response.json()

        quote_data['quote'] = json_response['contents']['quotes'][0]['quote']
        quote_data['author'] = json_response['contents']['quotes'][0]['author']
    except:
        quote_data['quote'] = 'QUOTE_ERROR'
        quote_data['author'] = ''