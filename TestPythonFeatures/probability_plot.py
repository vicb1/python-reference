import numpy
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = numpy.random.random((100,1))
data.sort(0)
data_standardized = (data - data.mean())/data.std()  # already sorted

# alternatively, can use zscore function, does the same standardization
data_standardized_zscore = stats.zscore(data)  # already sorted

df = pd.DataFrame({'data': data[:,0], 'data_standardized': data_standardized[:,0]})

plt.close("all")
ax = sns.lineplot(x='data_standardized', y='data', data=df)
plt.show()

