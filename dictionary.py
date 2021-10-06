# car1 = {
#     "name": "AUDI",
#     "speed": 250,
#     "cost": 80000,
#     "year": 2020,
#     "new": True,
# }
#
# #quyidagilar bir xil ish qiladi
# # new = car1.copy()
# new = dict(car1)
# print(new)













# del car1
# car1.clear()







# # car1.pop("cost")      #o'chirib qo'ish
# car1.popitem()          #oxiridai qiymatni o'cjirish
# for key, value in car1.items():
#     print(f"{key} \t {value}")






# car1.update({"cost": 50000, "new": False})
# for key, value in car1.items():
#     print(f"{key} \t {value}")







# if "cost" in car1:
#     print("bor")
# else:
#     print("no")










# car2 = {
#     "name": "Tesla",
#     "speed": 270,
#     "cost": 120000,
#     "year": 2021,
#     "new": True,
# }
#
# car3 = {
#     "name": input("Name:"),
#     "speed": int(input("Speed:")),
#     "cost": int(input("Cost:")),
#     "year": int(input("Year:")),
#     "new": input("New? [yes/no]: ").lower().strip() == "yes",
# }
#
# for key in car1.keys():
#     print(f"{key} \t {car1[key]} \t {car2[key]} \t {car3[key]}")




















































# player1 = {
#     "name": "Kroos",
#     "number": 8,
#     "age": 31,
#     "position": "CM",
#     "market_value": 40,
#     "country": "Germany",
#     "club": "Real Madrid",
# }
# player2 = {
#     "name": "Messi",
#     "number": 30,
#     "age": 34,
#     "position": "RW",
#     "market_value": 40,
#     "country": "Argentin",
#     "club": "PSG",
# }
# for key in player1.keys():
#     print(f"{key} \t {player1[key]}\t {player2[key]}")








# for key in kroos.keys():
#     print(f"{key}: \t {kroos[key]}")







# values = list(kroos.values())
# print(values)







# keys = kroos.keys()
# print(keys)
#
# kroos["leg"] = "right"
# print(kroos.keys())
# print(keys)











# # keys = list(kroos)
# keys = list(kroos.keys())       #dictionaryni listga o'tkazish
# print(keys)







# age = kroos["age"]
# club = kroos.get("club")
#
# print(age)
# print(club)











# print(type(kroos))
# zet ={}     #bo'sh dictionary ochish
# print(type(zet))




























# car = {
#     "brand": "Tesla",
#     "price": 60000,
#     "color": "black",
#     "speed": 300,
#     "year": 2021,
#     "new": True,
#     "zet": [1, 2, 3],
#     "no": (5, 5, 5),
#     "yes": {6, 8, 9},
#     1:555,
#     True: False,
#     5.5: "neee",
#     (5, 5): [5, 6, 7],
#     "konkret": {
#         "nima": "o'sha",
#     }
#
# }
# print(car)








# print(len(car))

# print(car["brand"], car["price"], car["color"])

# print(car["brand"])
# print(car["price"])
# print(car["color"])
# print(car["speed"])
# print(car["year"])
# print(car["new"])
