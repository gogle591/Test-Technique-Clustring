import pandas as pd # Pandas data Frame
import numpy as np # Numpu for manimulating the matrices
from sklearn.cluster import KMeans # From SickitLearn, import the algorithm KMeans
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns # Plot library
import matplotlib.pyplot as plt # Plot library

#Loading the data from a json file into the dataframe
train_set = pd.read_json("../Brisbane_CityBike.json")

# Showing informations about the data
print(train_set.info())

# Showing the first five rows of the data:
print(train_set.head())

# Showing the descriptions of each column of our data: That shows only the column numerical:
print(train_set.describe())

#The number of the unique address
print("The number of the unique addresses is {} from 148".format(len(train_set.address.unique())))


# Applying the tranform of the categorical variable address :
label_encoder = LabelEncoder()
train_set["address"] = label_encoder.fit_transform(train_set["address"])

# Plot the pairplot to detect the relations between the variables:

sns.pairplot(train_set)
plt.show()


# Training the KMeans Model 

#The name of features that we gonna use
features = ['number','address','latitude','longitude']

#Extract the features with the pandas dataframe
X= pd.get_dummies(train_set[features])

#Choosing the number of cluster 
kmeans = KMeans(n_clusters=3) # You want cluster the stations into 3: Bad, Meduim, Good.

# Fit the model : 
kmeans.fit(X)

#The result of the clusturing 
print(kmeans.labels_)