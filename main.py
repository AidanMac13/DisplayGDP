import urllib3
import seaborn as sns
import json

http = urllib3.PoolManager()
sns.set_theme()

r = http.request('GET', 'https://api.stlouisfed.org/fred/series?series_id=GDP&api_key=b4a7d4f07a04381d20dc6002f4d15178')


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(r.data)
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
