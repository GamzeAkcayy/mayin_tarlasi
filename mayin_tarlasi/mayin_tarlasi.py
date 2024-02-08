
import random

oyun_kontrol=1

while oyun_kontrol:

    mayin_sayisi=0
    oyun_alani=[]
    puan=0
    gizli_alan=[]
    kontrol=1

    boyut=int(input("En az 10 olacak şekilde boyut bilgisi giriniz:"))
    if boyut<10:
        print("10 veya ustunde bir boyut belirleyiniz.")
        continue

    mayin_sayisi=int((boyut*boyut)*0.3)

    mayin_alt=random.randint(0,boyut-1)
    mayin_ust=random.randint(0,boyut-1)

    for i in range(boyut):
        oyun_alani.append(["?"] * boyut)

    for i in range(boyut+2):
        gizli_alan.append(["?"] * (boyut+2))

    for i in range(mayin_sayisi):

        while oyun_alani[mayin_alt][mayin_ust] == "X":
            mayin_alt = random.randint(0, boyut - 1)    #Mayınlar rastgele yerleşir
            mayin_ust = random.randint(0, boyut - 1)

        if oyun_alani[mayin_alt][mayin_ust]=="?":
            gizli_alan[mayin_alt+1][mayin_ust+1]="X"
            oyun_alani[mayin_alt][mayin_ust]="X"
    while True:
        oyun_modu=int(input("1-Açık Mod \n2-Gizli Mod \nOynamak istediginiz modu seciniz:"))
        if oyun_modu==1:
                                                        #Oyun modu belirlenir
            break
        elif oyun_modu==2:

            break
        else:
            print("Lutfen gecerli bir mod seciniz")

    while True:
        mayin_kontrol = 0
        print("\n"*5)
        for i in oyun_alani:                    #oyun alanı oluşturulur
            print(" ".join(i))
        satir=int(input("Satir giriniz:"))
        sutun=int(input("Sutun giriniz:"))

        if oyun_alani[satir][sutun]=="X":        #X'ya basarsa oyun biter
            print("Maalesef Kaybettiniz!!")
            print("Puan:",puan)
            oyun_kontrol=0
            break

        elif oyun_alani[satir][sutun]!="?" and oyun_alani[satir][sutun]!="X":
            print("Başka bir konum belirleyiniz!!")

        else:                                       #Secilen noktanın etrafındaki mayınların sayısı burada belirlenir
            if gizli_alan[satir+1][sutun] == "X":
                mayin_kontrol += 1
            if gizli_alan[satir+1][sutun + 2] == "X":
                mayin_kontrol += 1
            if gizli_alan[satir][sutun] == "X":
                mayin_kontrol += 1
            if gizli_alan[satir][sutun+1] == "X":
                mayin_kontrol += 1
            if gizli_alan[satir][sutun + 2] == "X":
                mayin_kontrol += 1
            if gizli_alan[satir + 2][sutun] == "X":
                mayin_kontrol += 1
            if gizli_alan[satir + 2][sutun+1] == "X":
                mayin_kontrol += 1
            if gizli_alan[satir + 2][sutun + 2] == "X":
                mayin_kontrol += 1

        oyun_alani[satir][sutun] = str(mayin_kontrol)       #Toplam mayın sayısı hesaplanıp burada secilen nokta yerine yazılır
        gizli_alan[satir+1][sutun+1] = str(mayin_kontrol)
        puan += 1

        for i in range(len(oyun_alani)):
            for j in range(len(oyun_alani)):
                if oyun_alani[i][j]=="?":                   #Soru işareti var mı diye kontrol edilir
                    kontrol=1                               #bitirmek ya da devam etmek için
                    break
                else:
                    kontrol=0
        if kontrol==0:

            print("\n" * 5)
            for i in oyun_alani:
                print(" ".join(i))
            print("Tebrikler kazandiniz!! Puan:", puan)
            break