# about_me={"ism":"Tohirbek","t_yil": 2009,"Viloyat":"Farg'ona"}
# print(f"Mening ismim  {about_me["ism"]}, {about_me['t_yil']}-yil {about_me['Viloyat']}da tug'ilganman.")



# taomlar={"izzatbek":"osh","muhhamadyusuf":"girl","behruz":"pizza","xusan":"sho'rva"}
# print(f"Izzatbek suyukli taomi {taomlar['izzatbek']}\nMuhammadyusufning sevimli taomi {taomlar["muhhamadyusuf"]}\nXusaning sevimli taiomi{taomlar["xusan"]}\nBehruzning sevimli taomi {taomlar["behruz"]} ")


telefonlar={"izzatbek":"redmi",
            "tohirbek":"samsung",
            "muhammad yusuf":"samsung",
            "bexruz":"iphone x"}
telofon=telefonlar.get("Sayfulloh","Bunday ism mavjud emas")
print(telofon)