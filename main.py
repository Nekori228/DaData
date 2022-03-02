# https://github.com/hflabs/dadata-py

from dadata import Dadata
token = "7c6d0539ad0f102c392688afa71c46f629cbc8ea"
dadata = Dadata(token)
result = dadata.find_by_id("party", "7812014560")
print(result[0]["value"]) #Наименование
if "management" in result[0]["data"]:
    print("ООО")
    print(result[0]["data"]["management"]["name"], result[0]["data"]["management"]["post"])#Руководитель и должность (большой) (7812014560)
else:
    print("ИП")
    print(result[0]["data"]["fio"]["surname"], result[0]["data"]["fio"]["name"], result[0]["data"]["fio"]["patronymic"]) #Руководитель и должность (малый) (644802061247)
print(result[0]["data"]["address"]["value"])
