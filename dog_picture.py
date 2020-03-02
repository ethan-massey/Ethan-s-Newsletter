import requests

dog_data = {
    'url': 'NULL'
}


def get_dog_picture():
    try:
        response = requests.get("https://dog.ceo/api/breed/labrador/images/random")
        json_response = response.json()
        dog_data['url'] = json_response['message']

    except:
        print("ERROR: Trouble contacting dog.ceo API.")