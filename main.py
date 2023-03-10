import urllib3
import seaborn as sns
import fredapi as fa
import pandas as pd

import matplotlib.pyplot as plt
import json

http = urllib3.PoolManager()
sns.set_theme(style="darkgrid")

fred = fa.Fred("b4a7d4f07a04381d20dc6002f4d15178")

r = http.request('GET', 'https://api.stlouisfed.org/fred/series?series_id=GDP&api_key'
                        '=b4a7d4f07a04381d20dc6002f4d15178&file_type=json')

gdp = fred.get_series('GDP')

gdpData= r.data

if __name__ == '__main__':
    print(gdpData)
    # print(gdp)
    sns.lineplot(
        data=gdp,
    )
    plt.show()


