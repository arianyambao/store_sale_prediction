# Import necessary packages
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Load the model
model = keras.models.load_model('store_sale_predictor')

def predict_sale(store, 
				  day_of_week, 
				  customers, 
				  open, 
				  promo, 
				  state_holiday, 
				  school_holiday, 
				  month, 
				  day):
	
	# Transform the inputs to np array
	new_input = np.array([store, 
						  day_of_week, 
						  customers, 
						  open, 
						  promo, 
						  state_holiday, 
						  school_holiday, 
						  month, 
						  day]).reshape(1, -1)

	# Reshape to (batch_size, timesteps, input_dim)
	new_input = np.reshape(new_input, (new_input.shape[0], 1, new_input.shape[1]))

	# Predict the new input
	prediction = model.predict(new_input)

	# Return the predicted sale
	return prediction[0][0]