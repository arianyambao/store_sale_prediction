def preprocess_input(date, state_holiday):
	day, month = (int(date.split(" ")[0]), int(date.split(" ")[1]))

	if state_holiday == 'a':
		state_holiday = 1
	elif state_holiday == 'b':
		state_holiday = 2
	elif state_holiday == 'c':
		state_holiday = 3
	else:
		state_holiday = 0

	return day, month, state_holiday