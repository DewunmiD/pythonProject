class Goods:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def cost(self):
        return self.price * self.quantity



    def quantity_goods(self):
        return self.quantity



class Customer:
    def __init__(self, name, password, phone_number, email, address):
        self.name = name
        self.password = password
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def residence(self):
      return self.address

    def telephone(self):
        return self.phone_number

    def pass_word(self):
        return self.password

class Items:
    def __init__(self, customers_name, goods_name, date, amount, item_list):
        self.customers_name = customers_name
        self.goods_name = goods_name
        self.date = date
        self.amount = amount
        self.item_list = item_list

    def add_goods(self, item):
        self.item_list.append(item)

    def remove_goods(self, item):
        self.item_list.remove(item)

    def total_amount(self):
        total = 0
        for item in self.item_list:
            total += self.amount()
        return total


class Cart:
    def __init__(self):
        self.goods_item = {}

    def add_goods(self, goods_name, quantity, price):
        if goods_name in self.goods_item:
            self.goods_item[goods_name]["quantity"] += quantity
        else:
            self.goods_item[goods_name] = {"quantity": quantity, "price": price}

    def remove_goods(self, goods_name):
        if goods_name in self.goods_item:
            del self.goods_item[goods_name]
        else:
            print("Goods not found")

    def buy_now(self):
        total_cost = sum([item["quantity"] * item["price"] for item in self.goods_item()])
        print(f"Total cost: {total_cost}")

    def view_cart(self):
        print("Your Cart:")
        for goods_name, item in self.goods_item.items():
            print(f"{goods_name}: {item['quantity']} x {item['price']} = {item['quantity'] * item['price']}")

    def checkout(self):
        self.view_cart()
        self.buy_now()
        print("Thank you for shopping with us!")
        self.goods_item = {}


class Discount:
    def __init__(self, order_name, discount_type, discount_value):
        self.order_name = order_name
        self.discount_type = discount_type
        self.discount_value = discount_value

    def calculate_discount(self, total_amount):
        if self.discount_type == "percentage":
            discount_amount = total_amount * (self.discount_value / 100)
        elif self.discount_type == "fixed":
            discount_amount = self.discount_value
        else:
            discount_amount = 0
        return discount_amount


class Payment:
    def __init__(self, order_name, payment_method, payment_date):
        self.order_name = order_name
        self.payment_method = payment_method
        self.payment_date = payment_date


    def payment_process(self):
        if self.payment_method == "credit_card":
            print("Processing credit card payment")
        elif self.payment_method == "bank_transfer":
            print("Processing bank transfer payment")
        else:
            print("Invalid payment method.")


class Delivery:
    def __init__(self, order_name, delivery_date, delivery_address, delivery_status):
        self.order_name = order_name
        self.delivery_date = delivery_date
        self.delivery_address = delivery_address
        self.delivery_status = delivery_status

    def calculate_delivery(self):
        return 10000

class Review:
    def __init__(self, good_name, buyer_name, rating, comment):
        self.goods_name = good_name
        self.buyer_name = buyer_name
        self.rating = rating
        self.comment = comment

    def get_rating(self):
        return self.rating


    def get_comment(self):
        return self.comment

goods = Goods("wig", "blonde wig", 200000, 1)
customer = Customer("dewunmi daniel", "password0000", "+2347082488365", "daewoorazor992@yahoo.com", "2,prince adeoye adeosun street,akala estate,akobo")
items = Items("dewunmi daniel", "wig", "2024-08-21", 200000, 1)
cart = Cart()
discount = Discount("wig", "percentage", 10,)
payment = Payment("wig", "credit card", "2024-08-21")
delivery = Delivery("wig", "2024-08-21", "2,prince adeoye adeosun street,akala estate,akobo", "pending")
review = Review("wig", "dewunmi daniel", 5, "Excellent!")

print("Goods Details:")
print(f"Name: {goods.name}")
print(f"Description: {goods.description}")
print(f"Price: {goods.price}")
print(f"Quantity: {goods.quantity}")

print("\nCustomer Details:")
print(f"Name: {customer.name}")
print(f"Password: {customer.password}")
print(f"Phone Number: {customer.phone_number}")
print(f"Email: {customer.email}")
print(f"Address: {customer.address}")

print("\nItems Details:")
print(f"Customer Name: {items.customers_name}")
print(f"Goods Name: {items.goods_name}")
print(f"Date: {items.date}")
print(f"Amount: {items.amount}")
print(f"Item List: {items.item_list}")

print("\nCart Details:")
print(cart.goods_item)

print("\nDiscount Details:")
print(f"Order Name: {discount.order_name}")
print(f"Discount Type: {discount.discount_type}")
print(f"Discount Value: {discount.discount_value}")

print("\nPayment Details:")
print(f"Order Name: {payment.order_name}")
print(f"Payment Method: {payment.payment_method}")
print(f"Payment Date: {payment.payment_date}")

print("\nDelivery Details:")
print(f"Order Name: {delivery.order_name}")
print(f"Delivery Date: {delivery.delivery_date}")
print(f"Delivery Address: {delivery.delivery_address}")
print(f"Delivery Status: {delivery.delivery_status}")

print("\nReview Details:")
print(f"Goods Name: {review.goods_name}")
print(f"Buyer Name: {review.buyer_name}")
print(f"Rating: {review.rating}")
print(f"Comment: {review.comment}")