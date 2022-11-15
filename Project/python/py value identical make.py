# for amount with discount.
item = input("Enter your mobile model")
price = int(input("Enter Price: "))
qty = int(input("Enter Quantity:"))
amount = (price*qty)
discount=0

if amt>10000:
    print ("10% discount is applicable")
    discount = (amt*10)/100
    amt=amt-discount
    print ("Amount yable: ",amt)

#program is over
