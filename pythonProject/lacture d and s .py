
# sets = ["element1","element2","elwment3","element1"]
# print(sets)
# if "element1" in sets :
#      print("yes")

# countrylist = []
# for i in range(5):
#     country = input("please enter the country: ")
#     countrylist.append(country)
# countryset = set(countrylist)
# print(countrylist)
# print(countryset)
#
# if "nepal" in countryset:
#     print("attended")

# dictionary = ( "key":"value":,"key2":"value2":,"key3":"value3":)
countrylist = []
for i in range(5):
    country = input("please enter the country: ")
    countrylist.append(country)
countrydictionary = {}
for country in countrylist:
    if country in countrydictionary:
        countrydictionary[country] += 1
    else:
        countrydictionary[country] = 1
print(countrydictionary)
