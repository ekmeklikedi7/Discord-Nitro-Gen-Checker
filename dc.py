import requests
import random
import string
import time
import colorama

from colorama import Fore, Back, Style

colorama.init()

print(Fore.BLUE)
print("""Yardım Veya Destek İçin Discord Sunucum: https://discord.gg/8cjRb3Kn
""")

print(Fore.GREEN)
print("""Discord Nitro Generator + Checker

CrackForum.xyz / Ekmeklikedi7
""")

time.sleep(4)
print("""Çalışan Kodlar Klasörde Çalışan Kod Olarak Ayırılacaktır.
""")
time.sleep(4)

num = int(input('Ne kadar nitro kodu üretilip checklensin?: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("""
Nitro kodunuz oluşturuluyor..
""")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(Fore.BLUE)
            print(f" Çalışıyorrrrrr | {nitro} ")
            break
        
        else:
            print(Fore.MAGENTA)
            print(f" Çalışmıyor | {nitro} ")

input("\nKodlar Üretildi. Çıkış Yapmak İçin Enter'e Basınız..")
