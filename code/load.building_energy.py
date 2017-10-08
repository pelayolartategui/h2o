import os

import h2o
import matplotlib.pyplot as plt

h2o.init()

#If next line fails, instead set path to location of datasets.
path = os.path.dirname(__file__)
fname = os.path.join(path, "../datasets/ENB2012_data.csv")
data = h2o.import_file(fname)
x = data.names
predictions = ["Heating_Load", "Cooling_Load"]
factorsList = ["Orientation", "Glazing_Area_Dist"]
data[factorsList] = data[factorsList].asfactor()
x.remove(predictions[0])
x.remove(predictions[1])
train, test = data.split_frame([0.8])

train.describe()

print(train.cor().round(2))

res = train[x].cor(train[predictions[0]]).as_data_frame()
res.index = x
res.plot.barh()
plt.show()
