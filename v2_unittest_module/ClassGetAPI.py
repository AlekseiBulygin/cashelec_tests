import sys
import requests
import time


class GetAPI:

    def __init__(self, url, apikey):
        self.url = url
        self.params = {
            'limit': 10,
            'convert': 'USD',
            'sort': "volume_24h",
            'CMC_PRO_API_KEY': apikey
        }

    def get_api(self):
        start_time = time.time()
        res = requests.get(self.url, params=self.params)
        process_time = time.time() - start_time
        date = res.json()['status']['timestamp']
        return (res.status_code, date, sys.getsizeof(res), process_time)


if __name__ == '__main__':

    getapi = GetAPI(url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
                    apikey='b0043f38-f970-404c-95f4-935f571a521c')
