# kun=input("Bugun qaysi kun>>")
# if kun.lower() == "shanba" or kun.lower() == "yakshanba": 
    # print("Bugun dam olish kuni!")


# else:
    # print("Bugun ish kuni")
    
    # 
# kun=input("Bugun qaysi kun>>")
# if kun.lower() != "shanba" and kun.lower() != "yakshanba": 
    # print("Bugun ish kuni  !")
    


# else:
    # print("Bugun dam olish kuni!")
    
    
    
# kun=input("Bugun qaysi kun? >>")
# harorat=int(input("Bugungi havo harorati qanday? >>"))

# if kun.lower() =="yakshanba" and harorat>=30:
    # print("Bugun havo issiq cho'milgani boramiz !")
    # 
# elif kun.lower() =="yakshanba" and harorat<30:
    # print("Bugun havo sovuq, uyda qolamiz !")    
# else:
    # print("Bugun ish kuni!")
    
# narx=15000
# choy=True
# salat=False

# if choy and salat:
    # narx=narx+1000
    
# elif choy or salat:
    # narx=narx+5000
    
# print(f"jami {narx} so'm")

narx=15000
choy=True
salat=False
non=True
kampot=True
asarti=False
if choy: 
    narx=narx+3000
if salat:
    narx=narx+5000
if non:
    narx=narx+2000
if kampot:
    narx=narx+5000
if asarti:
    narx=narx+15000
print(f"sizning hisobingiz  {narx} so'm")