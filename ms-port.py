#! /bin/python3

import datetime
import os

bugun = (datetime.datetime.now().today())

print("""
█   █ █   █ █   █  ███  █   █ █   █  ███ ████      ████ █████  ████  ████ ███  ███  █   █ 
██ ██ █   █ █   █ █   █ █   █ █   █   █  █   █    █     █     █     █      █  █   █ ██  █ 
█ █ █ █   █ █   █ █████ █████ █████   █  █   █     ███  ████   ███   ███   █  █   █ █ █ █ 
█   █ █   █  █ █  █   █ █   █ █   █   █  █   █        █ █         █     █  █  █   █ █  ██ 
█   █  ███    █   █   █ █   █ █   █  ███ ████     ████  █████ ████  ████  ███  ███  █   █ """
)
print("                                          ")
print("██████████████████████████████████████████")
print(f"\nBugün : {bugun} \n")
print("0- Terminal")
print("1- Ağ Tarama")
print("2- Ağ Bilgilerim")
print("3- Çıkış")
print("██████████████████████████████████████████")

while True:
    

    def PortScan():

        print("1- Güvenli Tarama \n2- Orta Derece \n3- Agresif Tarama (!) \n4- Tam Tarama (!)")
        print("\n[*] Uygulamayı 'sudo' Yetkisinde Kullanmanızı Öneririz.")
        Lvl = int(input(f"{inp} Güvenlik Seviyesi (1-4) : "))

        L1 = "-sS"
        L2 = "-sT -sV -O"
        L3 = "-sT -sV -p-"
        L4 = "-v -O -A -p-"

        hiz = input(f"{inp} Hız (y|o|h) : ")
        
        cmnd = ""

        if Lvl == 1:
            cmnd = L1
        elif Lvl == 2:
            cmnd = L2
        elif Lvl == 3:
            cmnd = L3
        elif Lvl == 4:
            cmnd = L4
        else:
            pass

        if hiz == "y":
            cmnd + "T2"
        elif hiz == "o":
            cmnd + "T4"
        elif hiz == "h":
            cmnd + "T5"
        else:
            pass



        ip = input(f"{inp} İp Adresi: ")

        kayit = input(f"{inp} Sonucu Kaydetmek İster Misiniz? (e/h) :"
        ).lower()

        k = ""
        if kayit == "e":
            docN = input(f"{inp} Kaydedilecek Dosyanın İsmi: ")
            k = "-oG " + docN
        else:
            None

        try:

           
            islem = os.system(f"sudo nmap {cmnd} {ip} {k}")

        except:
            print("Yanlış Giden Birşeyler Var..")
        


    def NeTİnf():
        print(f"Siz Kimsiniz? : {os.system("whoami")}")
        print("********************************************************")
        print(f"Dizininiz : {os.system("pwd")}")
        print("********************************************************")
        print(f"Ağ Bilgileriniz : {os.system("ip a")}")
        print("********************************************************")

    inp = """
┌──(Tevhid㉿Muvahhid)-[~]
└─# """
    x = input(inp)
    

    if x == "0":
        print("Çıkış İçin /exit")
        while True:
            
            komt = input(f"{inp}") 
            if komt == "/exit":
                break
            else:
                os.system(komt)
            
    elif x == "1":
        PortScan()

    elif x == "2":
        NeTİnf()

    elif x == "3":
        print("Selametle Kalın..")
        break
