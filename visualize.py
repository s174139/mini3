import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="white", color_codes=True)

data = pd.read_csv("data_21.csv")
data = data.loc[:, data.columns != 'Unnamed: 0']
cond = "S"
dataC0 = data.where(data[cond] == 0).dropna()
dataC1 = data.where(data[cond] == 1).dropna()
print("Amount of data points: {}".format(len(data["S"])))

means = data.mean(axis=0)
variance = data.var(axis=0)
correlation = data.corr(method='pearson')

meansC0 = dataC0.mean(axis=0)
varianceC0 = dataC0.var(axis=0)
correlationC0 = dataC0.corr(method='pearson')

meansC1 = dataC1.mean(axis=0)
varianceC1 = dataC1.var(axis=0)
correlationC1 = dataC1.corr(method='pearson')

print("Means of every column:\n{}".format(means))
print("Variance of every column:\n{}".format(variance))
print("Correlation of every column:\n{}".format(correlation))

print("Amount of data points: {}".format(len(dataC0)))
print("Means of every column with conditioning on {} = 0:\n{}".format(cond, meansC0))
print("Variance of every column with conditioning on {} = 0:\n{}".format(cond, varianceC0))
print("Correlation of every column with conditioning on {} = 0:\n{}".format(cond, correlationC0))

print("Amount of data points: {}".format(len(dataC1)))
print("Means of every column with conditioning on {} = 1:\n{}".format(cond, meansC1))
print("Variance of every column with conditioning on {} = 1:\n{}".format(cond, varianceC1))
print("Correlation of every column with conditioning on {} = 1:\n{}".format(cond, correlationC1))

### --- plot ----

data.hist(bins=20, range=[-10,10])
plt.show()

g = sns.PairGrid(data, palette='RdBu_r')
g.map(plt.scatter, alpha=0.8)

#s = pd.Series(data["A"])
#fig = pd.plotting.bootstrap_plot(s, samples=500)

plt.show()







