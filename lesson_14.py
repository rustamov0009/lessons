# yosh=int(input ("yoshiz nechida"))
# if yosh<=4:
#     print("Siz uchun bepul")
# elif yosh<=12:
#     print("Siz uchun 5 ming")
# elif yosh>=100:
#     print("Siz uchun bepul")
# else:
#     print("Siz uchun 10 ming")
yosh=int(input ("Yoshiz nechida? ")) 

if yosh <=4:
    narx=0
    
elif yosh <=12:
    narx=5000
    
elif yosh <=65:
    narx=10000
    
else:
    narx=8000
    
print(f"Siz uchun chipta {narx} so'm")