modelYear = eval(input("Enter a model year"))

recalled = modelYear in range(1999, 2007)
if modelYear <=2004:
    model_name = 'Extravagent'
    print(recalled)
    print(model_name)
elif modelYear >= 2004 and modelYear <= 2007:
    model_name = 'Guzzler'
    print(model_name)
    print(recalled)

else:
    print(recalled)



