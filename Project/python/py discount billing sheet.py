# for amount with discount 10%.

p= int(input("enter the price of the product"))
q = int(input("enter the product qauntity"))
a = p*q

print("total amount of the prduct is",a)
if a > 100 :
    d = a*10/100
    a = a-d
    print("amount payable after discount :",a)

#over
