# Aloysius Gonzaga Ardhian Krisna Aji
# 71180298

# Kira diminta untuk membuat sebuah program yang bisa merekap jumlah gender(P,L) pada dictionary yang diberikan secara random(datanya itu random)
# sebagai temannya kira kamu wajib membantunya data di ambil berdasarkan random(import random)

import random

gender = [random.choice("L""P") for i in range(100)]

rekapGender = {}

for data in gender:
    if data in rekapGender:
        rekapGender[data] += 1
    else:
        rekapGender[data] = 1
        
print(rekapGender)