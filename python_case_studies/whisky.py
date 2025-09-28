import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import SpectralCoclustering

whisky = pd.read_csv("C:/Users/User/OneDrive/Desktop/python_for_research/data/whiskies.txt")
whisky["Regions"] = pd.read_csv("C:/Users/User/OneDrive/Desktop/python_for_research/data/regions.txt")

flavors = whisky.iloc[:, 2:14]

corr_flavors = pd.DataFrame.corr(flavors)

plt.pcolor(corr_flavors)
plt.colorbar()
plt.show()

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
plt.show()

model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
print(model.rows_)

np.sum(model.rows_, axis=1) # the number of whiskies for each cluster
model.row_labels_ 

whisky["Group"] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.iloc[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)

correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlations)

plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.show()
