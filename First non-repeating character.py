def first_non_repeating_letter(string):
	for i in range(len(string)):
		if string.lower().count(string[i].lower()) == 1:
			return string[i]
	else: return ("")	