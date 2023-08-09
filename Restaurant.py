class Restaurant:
	restaurantName = "Restaurant.py"
	address = "4072 339 Communipaw Ave, Jersey City, NJ 07304, United States"
	phoneNumber = "4495820032"

	def bookTable(self, tableNumber, busy, waiter, tableClientName):
		table1 = Table(tableNumber, busy, waiter, tableClientName)
		print(table1.tableNumber, table1.waiter, table1.tableClientName)

	def takeOrder(self):
		print("Select what you wanna order")
		billCost = 0
		qty = 0
		while True:
			item = int(input("1.- Hotdog....$1.50\n2.- Pizza.....$1.25\n3.- Soda......$1.00\nYour selection: "))
			if(item==1):
				billCost += 1.5
				qty += 1
			elif(item==2):
				billCost += 1.25
				qty += 1
			elif(item==2):
				billCost += 1
				qty += 1
			else:
				print("Wrong selection")
			yn = input("Do you wanna add one more item? y/n")
			if(yn != "y"):
				break
		print("You'll pay: ", billCost)	

class Client:
	clientName = ""
	clientPhone = ""

	def __init__(self, clientName, clientPhone):
		self.clientName = clientName
		self.clientPhone = clientPhone

	def payBill():
		Restaurant.billCost = 0
		print("The bill was paid")

class Waiter:
	waiterName = ""
	waiterID = ""

	def __init__(self, waiterName, waiterID):
		self.waiterName = waiterName
		self.waiterID = waiterID

	def deliverOrder():
		print("Order delivered")

class Chef:
	chefName = "Arthur"
	chefID = "102"

	def cookDish():
		print(chefName, " is cooking the dishes")

class Table:
	tableNumber = ""
	busy = False
	waiter = ""
	tableClientName = ""

	def __init__(self, tableNumber, busy, waiter, tableClientName):
		self.tableNumber = tableNumber
		self.busy = busy
		self.waiter = waiter
		self.tableClientName = tableClientName

	def occupyTable():
		return 1

	def vacateTable():
		return -1

class Order:
	orderID = ""
	articles = ""
	delivery = ""

	def __init__(self, orderID, articles, delivery):
		self.orderID = orderID
		self.articles = articles
		self.delivery = delivery

	def prepareOrder():
		print("Order was taken by the chef")

	def deliverOrder():
		print("The order was taken by the waiter and is on delivering")


def main():
	restaurant = Restaurant()
	print("Welcome to: ", restaurant.restaurantName)

	tableNumber = 0

	client1name = input("Write the client name: ")
	client1phone = input("Write the client phone: ")
	waiter1name = input("Write the waiter name: ")
	waiter1ID = input("Write the waiter ID: ")

	client1 = Client(client1name, client1phone)
	waiter1 = Waiter(waiter1name, waiter1ID)

	print(client1.clientName, client1phone)

	print("Waiter ", waiter1.waiterName, " is going to take the order")
	restaurant.takeOrder()
	
	Client.payBill()

	n = Table.occupyTable()
	print("Tables occupied ", (tableNumber+n))
	restaurant.bookTable(n, True, waiter1name, client1.clientName)

	Order.prepareOrder()
	Order.deliverOrder()

	Waiter.deliverOrder()

	n = Table.vacateTable()
	print("Tables occupied ", (tableNumber+n))

main()