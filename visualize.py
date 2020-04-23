import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="white", color_codes=True)

data = pd.read_csv("data_32.csv")
data = data.loc[:, data.columns != 'Unnamed: 0']
means = data.mean(axis=0)
variance = data.var(axis=0)
correlation = data.corr(method='pearson')

print(means)
print(variance)
print(correlation)

### --- plot ----
#ax = data.plot.hist(axis= 0, bins=12, alpha=0.5)
#density = data.plot.kde()
#sns.pairplot(data, height=2.5);

data.hist(bins=20, range=[-10,10])
plt.show()

g = sns.PairGrid(data, palette='RdBu_r')
g.map(plt.scatter, alpha=0.8)

plt.show()
#s = data.iloc[:,1:].values
#sns.jointplot(t,s,kind='kde');

#density

plt.subplots(2, 2)
data['Q'].plot(kind='kde')
plt.title('Q density')
plt.show()


data['R'].plot(kind='kde')
plt.title('R density')
plt.show()


data['S'].plot(kind='kde')
plt.title('S density')
plt.show()


data['T'].plot(kind='kde')
plt.title('T density')
plt.show()

#histogram
data['T'].plot(kind='hist')
plt.title('T Histogram')
plt.show()


s = data.iloc[:,2]
t = data.iloc[:,3]
sns.jointplot("T", "S", data=data)

#print(s)

#commenthere




