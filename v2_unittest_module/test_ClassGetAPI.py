import unittest
import datetime
import time
import threading
from v2_unittest_module.ClassGetAPI import GetAPI


class TestGetAPI(unittest.TestCase):

    getapi = GetAPI(url="https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
                apikey='b0043f38-f970-404c-95f4-935f571a521c')

    def test_getapi_functional(self):
        result = self.getapi.get_api()
        date_json = datetime.datetime.strptime(result[1], "%Y-%m-%dT%H:%M:%S.%fZ")

        self.assertEqual(result[0], 200)
        self.assertEqual(date_json.date(), datetime.datetime.today().date())
        self.assertLessEqual(result[2], 10000)
        self.assertLessEqual(result[3], 0.9)

    def test_getapi_load(self):
        self.threads = []
        self.returns = []
        start_time = time.time()
        for i in range(8):
            self.create_thread(name=i+1)
        print("Waiting...")
        for thread in self.threads:
            thread.join()
        all_process_time = time.time() - start_time
        rps = round(len(self.returns) / all_process_time)
        percentil = (len([i[3] for i in self.returns if i[3] <= 0.45])/len(self.returns)) * 100

        for result in self.returns:
            self.assertEqual(result[0], 200)
        self.assertGreaterEqual(rps, 5, 'rps < 5')
        self.assertGreaterEqual(percentil, 80, f'{percentil}% < 450 ms')

    def create_thread(self, name):
        name = f"Thread №{name}"
        thread = threading.Thread(target=lambda l, arg1: l.append(GetAPI.get_api(arg1)),
                                  args=(self.returns, self.getapi,), name=name)
        print(thread.name + " is running")
        thread.start()
        self.threads.append(thread)


if __name__ == '__main__':
    unittest.main()


