#!/usr/bin/env python
# encoding: utf-8
import json

from flask import Flask, request, jsonify
from utils.preprocess import preprocess_input
from api.model_inference import predict_sale

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
	return jsonify({'message': 'success',
					'status_code': '200'})

@app.route('/api/sales/predictions', methods=['POST'])
def sale_prediction():
	inputs = json.loads(request.data)
	
	store = inputs['store']
	day_of_week = inputs['day_of_week']
	customers = inputs['customers']
	store_open = inputs['open']
	promo = inputs['promo']
	school_holiday = inputs['school_holiday']
	month, day, state_holiday = preprocess_input(inputs['date'], inputs['state_holiday'])

	prediction = predict_sale(store, 
							  day_of_week, 
							  customers, 
							  store_open, 
							  promo, 
							  state_holiday, 
							  school_holiday, 
							  month, 
							  day)

	return jsonify({'store': inputs['store'],
					'day_of_week': inputs['day_of_week'],
					'date': inputs['date'],
					'customers': inputs['customers'],
					'open': inputs['open'],
					'promo': inputs['promo'],
					'state_holiday': inputs['state_holiday'],
					'school_holiday': inputs['school_holiday'],
					'sale': float(prediction),
					'message': "success",
					'status_code': 200})

app.run()