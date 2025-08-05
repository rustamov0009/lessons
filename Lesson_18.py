# cars={"model": "ferarri","rangi": "qizil"}
# print(cars["rangi"])


# talaba={"ism":"tohirbek","yosh":"16"}
# talaba["kurs"]=4
# talaba["fakultet"]="informatika"
# print(f"Assalomu alekum   {talaba["ism"].title()},\n{talaba["yosh"]}-yoshda,\n{talaba["kurs"]}-kurs,\n{talaba["fakultet"]}-fakultetida o'qiydi")





talaba={"ism":"tohirbek","yosh":"16"}
talaba["kurs"]=4
talaba["fakultet"]="informatika"
print(f"Assalomu alekum   {talaba["ism"].title()},\n{talaba["yosh"]}-yoshda,\n{talaba["kurs"]}-kurs,\n{talaba["fakultet"]}-fakultetida o'qiydi")
print(talaba)
del talaba["ism"]
print(talaba)