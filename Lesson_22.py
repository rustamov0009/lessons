# # cars0={
# #     "model":"nexia 3",
# #     "rang":"qora",
# #     "yil":2025,
# #     "narx":99000,
# #     "km":1,
# #     "karobka":"aftmat"
# #     }

# # cars1={
# #     "model":"volvo",
# #     "rang":"qora",
# #     "yil":2025,
# #     "narx":123000,
# #     "km":1,
# #     "karobka":"mehanika"
# #     }

# # cars2=mehanika"{
# #     "model":"bwm",
# #     "rang":"qora",
# #     "yil":2025,
# #     "narx":12000,
# #     "km":1,
# #     "karobka":"
# #     }

# # cars=[cars0,cars1,cars2]
# # for car in cars:
# #     print(f"{car['model'].title()},"
# #           f"{car['rang']} rang,"
# #           f"{car['yil']}-yil, {car['narx']}$")

# cars=[]

# for n in range(10):
#     new_car={
#     "model":"malibu",
#     "rang":"none",
#     "yil":2025,
#     "narx":123000,
#     "km":0,
#     "karobka":"avto"
#     }
#     cars.append(new_car)

# for car in cars[:3]:
#     car['rang'] = 'qizil'
#     car['narx'] = 15000
    
# for car in cars[3:6]:
#     car['rang'] = 'oq'
#     car['narx'] = 20000
# for car in cars[6:]:
#     car['rang'] = 'qora'
#     car['narx'] = 25000
# print(cars)



dasturchilar={
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#'],
    'sardor':['java','go'],
    }
print(dasturchilar.keys())
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quydagi dasturlash tillari biladi:", end='')
    for til in tillar:
        print(f'{til.upper()}',end='')