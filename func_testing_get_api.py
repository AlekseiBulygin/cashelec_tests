import datetime
import time
import get_api


def test_get_api():
    today = datetime.datetime.today().date()
    start_time = time.time()
    result = get_api.get_api()
    proc_time = time.time() - start_time
    data_json = datetime.datetime.strptime(result[1], "%Y-%m-%dT%H:%M:%S.%fZ")
    if result[0] == 200 and data_json.date() == today and result[2] <= 10000 and proc_time < 0.5:
        print("Test is ok", f"Time for process {round(proc_time * 100)} ms", f"File size {result[2]} B", sep='\n')
    else:
        print("Test is fail", [i for i in result])


if __name__ == "__main__":
    test_get_api()
