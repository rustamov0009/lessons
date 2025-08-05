# menyu=["osh","somsa","shashlik","sho'rva","lag'mon"]
# ovqat=input("Nima ovqot yeysiz? ")
# if ovqat.lower() in menyu:
    # print("Buyurtma qabul qilindi")
    
# else:
    # print("Kechirasiz bizda bunday ovqat yo'q")
    
    
# menyu=["osh","somsa","shashlik","lag'mon","pepsi","fanta","choy","salat","sezr salat","qozon kabob"]
# buyurtma=["shashlik","somsa","pepsi", "norin"]

# for taom in buyurtma:
    # if taom in menyu:
        # print(f"Buyurtmangiz {taom} qabul qilndi")
    
    # else:
        # print(f"Afsuski bizda {taom} yo'q")



# menyu=["osh","somsa","shashlik","lag'mon","pepsi","fanta","choy","salat","sezr salat","qozon kabob"]
# ovqat=input("Nima ovqat yeysiz? ")
# if ovqat.lower() not in menyu:
    # print("Afsuski bizda bunday ovqat yoq")
     
# else:
    # print("Buyurtma qabul qilindi")
    
    
# son=int(input("Istalgan son kiritin ? "))
# for n in range(2,11):
    # if not (son%n):
        # print(f"{son} soni {n} soniga qoldiqsiz bo'linadi ? ")
        
        
username=["tohirbek","izzatbek","behruz"]
login = input("Yangi login kiritin? ")

if login.lower() in username:
    print("Bu username bant boshqa login kiriting!")

else:
    print("Xush kelibsiz", login.title())