# SelecTra
>Bilgisayarınız herhangi bir yerinden(terminal,pdf,tarayıcı vs)
>seçitiğiniz en son kelimeyi Tureng.com dan en-tr arama yapıp 
>ilk 5 sonucu ekrana bildirim olarak dönderen program.

### Gerekli Paketler
```sh
apt install xsel python3-bs4 python3-urllib3 libnotify-bin
```

### Calistirmak için;
```sh
#kelimeyi sectikten sonra
python3 selectra.py
```

### Kullanılan Kütüphaneler
* os
* gi.repository
* BeautifulSoup
* urllib
* xsel
* subprocess

### Aktif Kullanım
- Aşağıdaki komuta bir kısayol tuşu atayın. 
```sh
python /dosyamHerNeredeyse/selected.py
```
- Ingilizce bir kelime seçin ve atadığınız kısayol tuşuna basın
