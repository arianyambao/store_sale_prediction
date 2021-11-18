# store_sale_prediction
Sample Predictive ML Deployment

This project utilises the use of Tensorflow's Keras prediction model callable via Flask in an API manner.

## Install the dependencies
```
pip install -r requirements.txt
```

## Run the app using flask

```
python main.py
```
or

```
python3 main.py
```

## Run the app using gunicorn
```
gunicorn main:app
```

## Sample API Inference Call:
Parameters:
  - `store` (int): store number
  - `day_of_week` (int): the day of the week
  - `date` (string): date of the input (dd mm yyyy)
  - `customers` (int): the number of customers
  - `open` (int): information regarding whether the store is open (0 or 1)
  - `promo` (int): information regarding whether there is a promo in the store (0 or 1)
  - `state_holiday` (string): information regarding which state holiday there is (0, "a", "b", "c")
  - `school_holiday` (int): information regarding whether there is a school holiday or none (0 or 1)
```
curl --location --request POST 'http://127.0.0.1:5000/api/sales/predictions' --header 'Content-Type: application/json' --data-raw '{
    "store": 1,
    "day_of_week": 4,
    "date": "4 30 2015",
    "customers": 650,
    "open": 1,
    "promo": 1,
    "state_holiday": "0",
    "school_holiday": 0
}'
```

## The model predictor's accessible in Heroku!
```
curl --location --request POST 'https://sample-sale-prediction.herokuapp.com/api/sales/predictions' \
--header 'Content-Type: application/json' \
--data-raw '{
    "store": 1,
    "day_of_week": 4,
    "date": "4 30 2015",
    "customers": 650,
    "open": 1,
    "promo": 1,
    "state_holiday": "0",
    "school_holiday": 0
}'
```
