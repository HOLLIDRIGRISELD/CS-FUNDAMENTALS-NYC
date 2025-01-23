#inputs of user
invoice = input('give me your invoice amount please : ')
vat =input('give me your VAT percentage please : ')

#calculation of total payment

Total_pay = int(invoice) + (int(invoice)*int(vat)/100)
print("Your total payment should be : " , Total_pay)