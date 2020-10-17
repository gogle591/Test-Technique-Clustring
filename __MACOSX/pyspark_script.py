from pyspark.ml.clustering import KMeans # For building the model
from pyspark import SparkContext # For the connexion with spark
from pyspark.sql import SQLContext # For the connexion with spark
from pyspark.sql.functions import isnan, when, count, col # to verify if there empty or null values
from pyspark.ml.feature import StringIndexer # for the categoriciel transform variables.
import seaborn as sns # Plot library
import matplotlib.pyplot as plt # Plot library
from pyspark.ml.linalg import Vectors # to manipulate the vectors
from pyspark.ml.feature import VectorAssembler # to create the features vector


#Making the connexion in local with spark:
sc = SparkContext('local', 'Spark SQL') 
sqlc = SQLContext(sc)

#Reading the json file to recuperate the data:
path = "../Brisbane_CityBike.json"
train_set = sqlc.read.json(path)

#Showing the informations of our data from the pyspark dataframe: 
print(train_set.printSchema())

#Describe the data:
print(train_set.describe().show())

## Get count of both null and missing values in our data:
print("A table with the number ouf missing and null values in our data:")
train_set.select([count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in train_set.columns]).show()

## Count the number of distinct addresses : 
nbrDisctinAdress = train_set.select('address').distinct().count()
print("The number of distinct addresses is : {}".format(nbrDisctinAdress))

#Transforming the address from string values into numerical values:
indexer = StringIndexer(inputCol="address", outputCol="numericalAdr")
train_set = indexer.fit(train_set).transform(train_set)

#Showing the first 20 rows of our data : 
print(train_set.show())

# Plot the pairplot to detect the relations between the variables:
sns.pairplot(train_set.toPandas())
plt.show()

# Training the Kmeans Model: 

# Gettin the train values : 
#Making the features that we are gonna use
features =['latitude','longitude','number','numericalAdr']

# regroup the features in one vector called features 
assembler = VectorAssembler(inputCols= features,outputCol="features")
Xtrain = assembler.transform(train_set)


#Initsializing the K of Kmeans into 3
kmeans = KMeans().setK(3).setSeed(1) # You want cluster the stations into 3: Bad, Meduim, Good.


#Fitting the algorithme with the data (train the model):
model =  kmeans.fit(Xtrain)

#Predict the resut of the application of KMeans.
predictions = model.transform(Xtrain)

#Show the result of the 10 first rows.
print(predictions.head(10))
