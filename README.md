# SelecTra
>Bilgisayarınız herhangi bir yerinden(terminal,pdf,tarayıcı vs)
>seçitiğiniz en son kelimeyi Tureng.com dan en-tr arama yapıp 
>ilk 5 sonucu ekrana bildirim olarak dönderen program.

### Gerekli Paketler
* Pardus/Debian/Ubuntu/Mint Benzeri
```sh
apt install xsel python-bs4 python-gobject
```
* Fedora/Centos Benzeri
```sh
dnf install xsel python2-gobject python2-beautifulsoup4
```

Calistirmak için;

```sh
#kelimeyi sectikten sonra
python selectra.py
```

### Kullanılan Kütüphaneler
* os
* gi.repository
* BeautifulSoup
* urllib
* xsel

### Kurulum Ve Kullanım
>1- "selected.py" dosyasını bilgisayarınız herhangi bir yerine kopyalayın.
<br>
>2- Sisteminizin ayarlar bölümünden klaye kısayollarına giriniz.
<br>
>3- Özel Kısayol(Custom Shortcut) Ekle deyip Komut(Command) bölümüne
Aşağıdaki komutu girin Ve kendinize bir kısayol tuşu belirleyin. 
<br>
>4- Ingilizce bir kelime seçin ve belirlediğiniz kısayol tuşuna basın :) .
```sh
python /dosyamHerNeredeyse/selected.py
```
![örnek](http://i.hizliresim.com/oZBADm.png)

