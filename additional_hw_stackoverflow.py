import requests 


def get_news():
    url = 'https://api.stackexchange.com/2.3/questions?fromdate=1662508800&todate=1662681600&order=desc&sort=activity&tagged=python&site=stackoverflow'
    response = requests.get(url).json()
    res = response['items']
    for i, item in enumerate(res):
        print(i + 1, item['title'])

get_news()