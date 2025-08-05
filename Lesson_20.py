# real_madrid={"mbappe":10,"vini jr":8,"rodriygo":23,"ranaldo":7,"messi":10}
# print(real_madrid)
# del real_madrid ["messi"]
# print(real_madrid)


# username=["tohirbek","izzatbek","behruz"]
# login = input("Yangi login kiritin? ")

# if login.lower() in username:
    # print("Bu username bant boshqa login kiriting!")

# else:
    # print("Xush kelibsiz", login.title())
    
    
# son=1
# ismlar=[]
# while son<=5:
    # print(son,end='')
    # ism=input("Assalomu alaykum Ismingizzni kiritin:")
    # ismlar.append({"id":son, "ism":ism})
    # son=son+1
# print(ismlar)



print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
savol="Istalgan son kiritin :"
savol+="(dasturni toxtatish uchun 'exit'sozini kiriting)"
qiymat=''
while qiymat !='exit':
    qiymat=input(savol)
    if qiymat !='exit':
        print(float(qiymat)**2)