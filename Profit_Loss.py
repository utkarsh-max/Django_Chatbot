cost_price = int(input("Enter The Cost Price :"))
selling_price = int(input("Enter The Selling Price :"))
if(cost_price > selling_price):
    Loss = cost_price - selling_price
    print("The Shopkeepar is in Loss")
    print("The Loss is in the Rupees :",Loss)
else:
    Profit = selling_price - cost_price
    print("The Shopkeepar is in Profit")
    print("The Profit is in the Rupees :",Profit)