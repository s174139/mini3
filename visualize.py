import pandas as pd
import seaborn as sns

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
s = data.iloc[:,1:].values
#sns.jointplot(t,s,kind='kde');

print(s)

#commenthere




