class Oyun():
    def __init__(self) -> None:
        self.tahta=[["[]","[]","[]"],["[]","[]","[]"],["[]","[]","[]"]]
        self.durum=True
        self.hamle=0
    
    def oyna(self):
        if self.hamle % 2 ==0:
            self.p1_secim()
        else:
            self.p2_secim()
        self.hamle +=1
        self.durum=self.oyun_kontrol()

        if not self.durum:
            self.tahta_göster()
            if self.hamle % 2 == 0:
                print("oyun sonlandı, kazanan ikinci oyuncu ")
            else:
                print("oyun sonlandı, kazanan birinci oyuncu")
    def p1_secim(self):
        self.tahta_göster()
        print("Birinci oyuncu ")
        satir=int(input("Satırı giriniz: "))
        
        while satir<1 or satir >3:
            satir=int(input("lütfen 1 ve 3 arası değer giriniz: "))
        satir-=1
        sutun=int(input("Sutunu giriniz: "))
        
        while sutun<1 or sutun >3:
            sutun=int(input("lutfen 1 ve 3 arası değer giriniz: "))
        sutun-=1
        
        if self.dolu_mu(satir,sutun):
            self.p1_secim()
        else:
            self.tahta[satir][sutun]="[X]"

    def p2_secim(self):
        self.tahta_göster()
        print("İkinci oyuncu ")
        satir=int(input("Satırı giriniz: "))
        while satir<1 or satir >3:
            satir=int(input("lütfen 1 ve 3 arası değer giriniz: "))
        satir-=1
        sutun=int(input("Sutunu giriniz: "))
        while sutun<1 or sutun >3:
            sutun=int(input("lutfen 1 ve 3 arası değer giriniz: "))
        sutun-=1
        if self.dolu_mu(satir,sutun):
            self.p2_secim()
        else:
            self.tahta[satir][sutun]="[O]"
    def dolu_mu(self,satir,sutun):
        if self.tahta[satir][sutun] !="[]":
            return True
        else:
            return False
    def tahta_göster(self):
        for i in self.tahta:
            for j in i:
               print(j,end=" ") 
            print("\n")
    def oyun_kontrol(self):
        if [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]]==["X","X","X"] or [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]]==["O","O","O"]:
            return False

        if [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]]==["X","X","X"] or [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]]==["O","O","O"]:
            return False

        if [self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]]==["X","X","X"] or [self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]]==["O","O","O"]:
            return False


        if [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]]==["[X]","[X]","[X]"] or [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]]==["[O]","[O]","[O]"]:
            return False

        if [self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]]==["[X]","[X]","[X]"] or [self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]]==["[O]","[O]","[O]"]:
            return False

        if [self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]]==["[X]","[X]","[X]"] or [self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]]==["[O]","[O]","[O]"]:
            return False

        if [self.tahta[0][0],self.tahta[1][1],self.tahta[2][2]]==["[X]","[X]","[X]"] or [self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]]==["[O]","[O]","[O]"]:
            return False
        if [self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]]==["[X]","[X]","[X]"] or [self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]]==["[O]","[O]","[O]"]:
            return False
        return True

oyun=Oyun()

while oyun.durum:
    oyun.oyna()