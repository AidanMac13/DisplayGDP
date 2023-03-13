import urllib3
import seaborn as sns
import fredapi as fa
import matplotlib.pyplot as plt


http = urllib3.PoolManager()
sns.set_theme(style="darkgrid")

fred = fa.Fred("b4a7d4f07a04381d20dc6002f4d15178")


gdp = fred.get_series('GDP')

print(gdp)
sns.lineplot(
    data=gdp,
)
plt.show()


