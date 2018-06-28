customer_orders_file = open("customer-orders.txt","r")
new_customer_orders_file = open("new_customer_orders_file.txt","w")

for line in customer_orders_file:
	if line == "":
		break
	customer = line.split("|")
	zeroes = 6 - len(customer[0]) 
	customer[0] =  (zeroes * "0")+ customer[0]
	new_line = "|".join(customer)
	new_customer_orders_file.write(new_line)