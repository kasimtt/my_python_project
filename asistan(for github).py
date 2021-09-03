from re import search
from sys import audit
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import time
from datetime import datetime
import webbrowser

r=sr.Recognizer()  #ses tanıyıcı

def konustur(metin):  #text dosyasını sese cevirir
    tts=gTTS(text=metin,lang="tr")
    file="metin.mp3"
    tts.save(file)  #mp3 dosyasini kaydettik
    playsound(file)  #mp3 dosyasini ses olarak calıştırdık
    os.remove(file)  #mp3 dosyasını kaldırdık

def kayıt():
    with sr.Microphone() as source:
        audio=r.listen(source)   #global olarak tanınan r değerini listen methodu ile dinleme işlemi yapılır 
        voice=""     #voice tanımlandi
        try:
            voice=r.recognize_google(audio,language="tr") #ses tanımlandı
        except sr.UnknownValueError:
            konustur("anlayamadım.") 
        return voice

def işlem(voice):   #sohbet kısmından sonra istenen komutlar burada değerlendirilir
    if "nasılsın" in voice:
        konustur("iyidir senden naber")
    if "saat kaç" in voice or "saat" in voice:
        konustur(datetime.now().strftime("%H:%M:%S"))
    if "arama yap" in voice or "arama motoru" in voice:
        konustur("ne arama yapmak istiyorsunuz?")
        search=kayıt()
        url="https://www.google.com/search?q="+search
        webbrowser.get().open(url)
        konustur(search+"için bulduklarım")
    if "kapat" in voice:
        konustur("görüşürüz pampa")
        exit()
    





def baslangıc():   #ses asistanının başlangıc kısmı...
    baslangıc_metin="merhaba ben kasımın asistanıyım.Siz kimsiniz"
    konustur(baslangıc_metin)
    voice=kayıt()
    print(voice)
    
    if "kasım" in voice:
        isim="kasım"
        sohbet_metin="hoşgeldin patron,ne yapabilirim ?"
        konustur(sohbet_metin)
        time.sleep(1)
    elif "kasım" not in voice:
        isim="dostum"
        konustur("seni tanımıyorum yabancı , benden ne istiyorsun")
        time.sleep(1)
    konustur(f"mesela canın sıkıldıysa sohbet edelim diyebilirsin başka bir şey istiyorsan söyleyebilirsin.")
    voice2=kayıt()
    if "sohbet" in voice2:
        sohbet(isim)
    else:
        işlem(voice2)




def sohbet(isim):  #sohbet kısmı ve işleme gecis
    sohbet_metin=f"naber {isim}"
    konustur(sohbet_metin)
    cevap=kayıt()
    if "iyi" in cevap:
        sohbet_metin2="iyi olmana sevindim, yapmamı istediğin bişey var mı?"
        konustur(sohbet_metin2)
        cevap=kayıt()
        if "evet" in cevap:
            konustur("nasıl yardımcı olabilirim?")
            cevap=kayıt()
            işlem(cevap)
        elif "hayır" in cevap:
            konustur("tamam, yardımcı olabileceğim bir şey olursa her zaman buradayım.")
            exit()

        
    elif "kötü" in cevap or "idare" in cevap:
        sohbet_metin3="neden bir şey mi oldu .Yapmamı istediğiniz bişey var mi efendim?"
        konustur(sohbet_metin3)
        cevap=kayıt()
        if "hayır" in cevap or "yok" in cevap:
            konustur("tamam efendim, ihtiyacınız olursa buradayım.")
            exit()
        elif "evet" in cevap:
            konustur("sana nasıl yardımcı olabilirim")
            cevap=kayıt()
            işlem(cevap)
             

baslangıc()
while True:
    konustur("istediğiniz başka bir şey var mı?")
