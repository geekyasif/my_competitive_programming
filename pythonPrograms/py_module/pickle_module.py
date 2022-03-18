import pickle
import requests

# iris_data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# iris_text_data = (iris_data.text)
# formated_iris_list_data = iris_text_data.split()
# list = [ i.split(',') for i in formated_iris_list_data]
# iris_file = open("iris.pkl",'wb')
# pickle.dump(list,iris_file)

iris_open_file = open("iris.pkl", 'rb')
file_read_iris = pickle.load(iris_open_file)
print(file_read_iris)