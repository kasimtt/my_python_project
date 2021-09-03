#atanma similator
import random
def genelKulturSorulari():
    sayac=0
    with open("D:\\python vsc\\ogretmen_atamasi\\genelKulturSor.txt","r",encoding="utf-8") as dosya:   #genelKulturSor.txt'nin yolu güncellenebilir
        lines=dosya.readlines()                                          
        for i in range(5):
            a=random.choice(lines)                                   
            a=a.replace("\n","")
            a=a.split("?")                                         
            cevap=input(a[0]+" ? ")
            a[1]=a[1].strip(" ")
            
            if len(a)==2:
                if a[1].lower()==cevap.lower():
                    sayac+=1    
            elif len(a)==3:
                if a[1].lower()==cevap.lower() or a[2].lower()==cevap.lower():
                    sayac+1
    return sayac       

def puan_bulma(dogru_sayisi,puan):
    if dogru_sayisi ==5 :
        puan+=2
    elif dogru_sayisi ==4:
        puan+=1.5
    elif dogru_sayisi ==3:
        puan+=1
    elif dogru_sayisi ==2:
        puan+=0.5
    elif dogru_sayisi==1:
        puan-=0.5
    elif dogru_sayisi==0:
        puan-=1
    return puan

def bilgi(alan,puan,sıralama):
    
    if alan.lower()=="türkçe öğretmenliği" or alan.lower()=="türkçe":
        print("*******Türkce öğretmenliği atanma sistemine hosgeldiniz......*********\n")
        if puan >=75 and sıralama <=1600:
            print("bu aşamada size bes soru sorulacak.....")
            dogru_sayisi=genelKulturSorulari()
            puan=puan_bulma(dogru_sayisi,puan)
            print(puan)
            if puan>=80.0:
                print("atama ihtimaliniz çok yüksek olarak hesaplandi")
            else:
                print("sıkı çalış.Yeterli düzeyde değilsiniz")
        else:
            print("bu sonuclarla atanamazsınız...")
    if alan.lower()=="matematik öğretmenliği" or alan.lower()=="matematik":
        
        print("*******Matematik öğretmenliği atanma sistemine hosgeldiniz......*********\n")
        if puan >=75 and sıralama <=1600:
            print("bu aşamada size bes soru sorulacak.....")
            dogru_sayisi=genelKulturSorulari()
            puan=puan_bulma(dogru_sayisi,puan)
            print(puan)
            if puan>=77.5:
                print("atama ihtimaliniz çok yüksek olarak hesaplandi")
            else:
                print("sıkı çalış.Yeterli düzeyde değilsiniz")
        else:
            print("bu sonuclarla atanamazsınız...")
    if alan.lower()=="fizik öğretmenliği" or alan.lower()=="fizik":
        
        print("*******fizik öğretmenliği atanma sistemine hosgeldiniz......*********\n")
        if puan >=75 and sıralama <=1600:
            print("bu aşamada size bes soru sorulacak.....")
            dogru_sayisi=genelKulturSorulari()
            puan=puan_bulma(dogru_sayisi,puan)
            print(puan)
            if puan>=81.5:
                print("atama ihtimaliniz çok yüksek olarak hesaplandi")
            else:
                print("sıkı çalış.Yeterli düzeyde değilsiniz") 
        else:
            print("bu sonuclarla atanamazsınız...")
    if alan.lower()=="biyoloji öğretmenliği" or alan.lower()=="biyoloji":
        
        print("*******biyoloji öğretmenliği atanma sistemine hosgeldiniz......*********\n")
        if puan >=75 and sıralama <=1600:
            print("bu aşamada size bes soru sorulacak.....")
            dogru_sayisi=genelKulturSorulari()
            puan=puan_bulma(dogru_sayisi,puan)
            print(puan)
            if puan>=85.5:
                print("atama ihtimaliniz çok yüksek olarak hesaplandi")
            else:
                print("sıkı çalış.Yeterli düzeyde değilsiniz")
        else:
            print("bu sonuclarla atanamazsınız...")


alan=input("lütfen alanızı giriniz              : ")
puan=float(input("lutfen puanınızı küsüratıyla giriniz: "))
sıralama=int(input("lutfen sıralamanızı giriniz   :"))

bilgi(alan,puan,sıralama)




"""
alan=input("alanınızı giriniz")
puan=float(input("kpss sınavınızın sonucunu giriniz: "))
sıralama=int(input("kpss sıralamanızı giriniz: "))
"""
