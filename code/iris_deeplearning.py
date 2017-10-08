import h2o
h2o.init()

datasets = "https://raw.githubusercontent.com/DarrenCook/h2o/bk/datasets/"
data = h2o.import_file(datasets + "iris_wheader.csv")
y = "class"
x = data.names
x.remove(y)
train, test = data.split_frame([0.8])

m = h2o.estimators.deeplearning.H2ODeepLearningEstimator()
m.train(x, y, train)
p = m.predict(test)
print(p.as_data_frame())
