import time
kullanici_adi=str(input("kullanıcı adı giriniz :"))
kullanici_id=str(input("kullanıcı id giriniz :"))
time.sleep(3.2)
onay=str(input("saldırı baslayacak onaylıyormusunuz evet/hayır :"))
time.sleep(3)
if onay=="evet":
    clear
    print("SALDIRI İÇİN ONAY ALINDI ATTACK BAŞLATILIYOR...")
    cat install attack.txt
    time.sleep(5)
    print("ATTACK BİTTİ SONUCLAR GELİYOR LÜTFEN BEKLEYİNİZ...")
    time.sleep(3.2)
    print("ATTACK BİTTİ... SONUÇ BASARILI TELEGRAM ADRESİNİZE SONUÇLAR GÖNDERİLİYOR...")
    
else:
    clear
    print ("SALDIRI İÇİN ONAY ALINAMADI ATTACK BAŞLATILMIYOR...")

    
