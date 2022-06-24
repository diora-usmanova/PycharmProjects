# CALCULATE TIPS

subtotal, gratuityRate = eval(input("Enter the subtotal and gratuity rate : "))
gratuity = subtotal * (gratuityRate / 100)
total = subtotal + gratuity
print ("The gratuity is ", gratuity, " and the total is ", total)
