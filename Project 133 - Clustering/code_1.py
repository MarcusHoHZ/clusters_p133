import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

f = pd.read_csv("star_with_gravity(p132).csv")

mass = f["Mass"].to_list()
radius = f["Radius"].to_list()
gravity = f["Gravity"].to_list()



plt.figure(figsize = (10,5))
sns.lineplot(x= radius, y = mass, data = f)
plt.title("Clusters")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()