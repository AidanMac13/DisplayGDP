import urllib3
import seaborn as sns
import matplotlib.pyplot as plt
import json

http = urllib3.PoolManager()
sns.set_theme()

r = http.request('GET', 'https://api.stlouisfed.org/fred/series?series_id=GDP&api_key=b4a7d4f07a04381d20dc6002f4d15178')

tips = sns.load_dataset("tips")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(r.data)
    # print(tips)
    sns.relplot(
        data=tips,
        x="total_bill", y="tip", col="time",
        hue="smoker", style="smoker", size="size",
    )
    plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
