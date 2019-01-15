import sys
import requests


def get_api():
    url_api = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    params = {
        'limit': 10,
        'convert': 'USD',
        'sort': "volume_24h",
        # 'CMC_PRO_API_KEY': # insert yor API key in string format
    }
    res = requests.get(url_api, params=params)
    data = res.json()

    return res.status_code, data['status']['timestamp'], sys.getsizeof(res)


if __name__ == "__main__":
    get_api()
