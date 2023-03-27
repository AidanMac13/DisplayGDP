import config

import urllib3
import seaborn as sns
import fredapi as fa
import matplotlib.pyplot as plt


http = urllib3.PoolManager()
sns.set_theme(style="darkgrid")

fred = fa.Fred(config.fred_key)


gdp = fred.get_series('GDP')

print(gdp)
sns.lineplot(
    data=gdp,
)
plt.show()


