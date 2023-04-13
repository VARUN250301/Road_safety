import numpy as np
import pickle
loaded_model = pickle.load(open('C:/Users/Shree/Desktop/even acc pred/trained_model.sav', 'rb'))

input_data = (1, 0, 0, 7, 4, 5, 1, 0, 3, 2, 2, 1, 0, 1, 2, 1, 5, 0)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)