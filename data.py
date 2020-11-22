import requests


url = 'https://opentdb.com/api.php'#?amount=10&type=boolean'


def get_questions():

    params = {'amount': 10,'type': 'boolean'}

    response = requests.get(url,params=params)

    response.raise_for_status()

    question_data = response.json()['results']

    return question_data




