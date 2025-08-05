# davlatlar=["Rassiya","Uzbekistan","Qozogiston","Turkmaniston"]
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar,reverse=True))

# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

juft_sonlar=list(range(120, 1201, 2))
print(juft_sonlar)
jami=sum(juft_sonlar)
print(jami)

eng_katta_son=max(juft_sonlar)
eng_kichik_son=min(juft_sonlar)
yigindi = eng_katta_son + eng_kichik_son

print(f"Eng katta son {eng_katta_son} va eng kichik {eng_kichik_son} son yig'indisi {yigindi}")