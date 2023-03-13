import urllib3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

http = urllib3.PoolManager()

response = http.request("GET", "https://fred.stlouisfed.org/data/GDP.txt")

data_str = response.data.decode("utf-8")
data_lines = data_str.splitlines()

# Remove the header lines and extra information
data_lines = data_lines[19:]

data = pd.DataFrame([line.split() for line in data_lines], columns=["DATE", "GDP"])


data["GDP"] = data["GDP"].astype(float)

data["DATE"] = pd.to_datetime(data["DATE"])

data.set_index("DATE", inplace=True)

sns.lineplot(data=data, x=data.index, y="GDP")

plt.show()
