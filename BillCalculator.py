def calculate_tip(bill, percentage):
	tip = bill * (float(percentage)/100)
	return tip

def calculate_total(tip, bill):
	total_bill = tip + bill
	return total_bill

def calculate_everything(bill, percentage):
	tip = calculate_tip(bill,percentage)
	total_bill = calculate_total(tip, bill)
	return total_bill

def bill_splitter(total_bill,num_people):
	split_bill = total_bill/num_people
	return split_bill

def main():
	response = int(raw_input("What would you like to do? 1-calculate tip or 2-split the bill"))
	if response == 1:
		# print "1"
		bill = float(raw_input("How much was the bill?"))
		percentage = float(raw_input("What percentage would you like to tip (in %)?"))
		total_bill = calculate_everything(bill, percentage)
		tip = calculate_tip(bill, percentage)
		print "The tip is " + str(tip) + "."
		print "The total bill is " + str(total_bill) + "."
		print "Would you like to split the bill as well?"
	else:
		print "2"	

		#calculate and print out the tip amount and bill total
		# split_response = int(raw_input("Would you like to split the bill? 1-Yes or 2-No"))
		# if (split_response == 1):
		# 	num_split_response = int(raw_input("How many ways would you like to split the bill?"))
		# 	bill_splitter(total_bill,num_split_response)

if __name__ == '__main__':
	main()

