# What is variable?
# Variables are the containers for storing data values.
# Example
name='mansi nikhade'#here name is the variable and mansi nikhade is the value stored in the name variable
print(name)

age = 23
print(age)

weight=50.5
print(weight)

# Python Data Types
# There are multiple data types in python :
# int :An integer is a whole number.
print(type(age)) #output : <class 'int'>

# float:A float represents a number containing a decimal component.
print(type(weight))#output : <class 'float'>

# str :A string is text or we can say sequence of characters
print(type(name))#output : <class 'str'>

# bool : Boolean has only two values: either true or false 
adult=True
print(type(adult))#output : <class 'bool'>

# none :None means there is no value.
semister=None
print(type(semister))#output : <class 'NoneType'>

customer_id = 101
customer_name = "Mansi"
order_amount = 2500.75
is_paid = True
refund_amount = None

print(type(customer_id))
print(type(customer_name))
print(type(order_amount))
print(type(is_paid))
print(type(refund_amount))

quantity=int("5")*100
print(quantity)

price = float("1499.99")+500
print(price)

order_id =int( "5001")
amount = float("2499.50")
quantity =int( "3")
is_refunded = bool("False")#it will give true because python always evaluate non empty string as a true
#it only evaluate empty string as false so be careful while using this conversion with strings 
#So never blindly use bool() to convert API strings like "True" and "False".

#This is a very useful lesson for Data Engineering.

print(is_refunded)
print(type(order_id))
print(type(amount))
print(type(quantity))
print(type(is_refunded))
print(quantity*amount)
