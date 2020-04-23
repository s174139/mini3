import pandas as pd
import seaborn as sns; sns.set(style="white", color_codes=True)

data = pd.read_csv("data_17.csv")

means = data.mean(axis=0)
variance = data.var(axis=0)
correlation = data.corr(method='pearson')

print(means)
print(variance)
print(correlation)

### --- plot ----
#ax = data.plot.hist(axis= 0, bins=12, alpha=0.5)
#density = data.plot.kde()
s = data.iloc[:,2]
t = data.iloc[:,3]
sns.jointplot("T", "S", data=data)

#print(s)

#commenthere




