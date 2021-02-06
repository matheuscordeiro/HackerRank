#!/usr/local/bin/python3

# The Time in Words


def timeInWords(h, m):
	numbers = {
		1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine",
		10: "ten",
		11: "eleven",
		12: "twelve",
		13: "thirteen",
		14: "fourteen",
		16: "sixteen",
		17: "seventeen",
		18: "eighteen",
		19: "nineteen",
		20: "twenty"
	}
	hour_past = numbers[h]
	hour_to = numbers[h+1]
	if m == 0:
		return f"{hour_past} o' clock"
	elif 1 <= m <= 30:
		if m == 15:
			return f"quarter past {hour_past}"
		elif m == 30:
			return f"half past {hour_past}"
		elif numbers.get(m):
			minutes = numbers[m]
			if m > 1:
				return f"{minutes} minutes past {hour_past}" 
			else:
				return f"{minutes} minute past {hour_past}"
		else: 
			second_part = m % 10
			first_part = m - second_part
			return f"{numbers[first_part]} {numbers[second_part]} minutes past {hour_past}" 
	else:
		if m == 45:
			return f"quarter to {hour_to}"
		else:
			m = 60 - m
			if numbers.get(m):
				minutes = numbers[m]
				if m > 1:
					return f"{minutes} minutes to {hour_to}" 
				else:
					return f"{minutes} minute to {hour_to}"
			else:
				second_part = m % 10
				first_part = m - second_part
				return f"{numbers[first_part]} {numbers[second_part]} minutes to {hour_to}"

print(timeInWords(5, 47))
