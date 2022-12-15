# SelecTra

ChatGPT3 source code analysis ;

This code is written in Python and uses the BeautifulSoup library to scrape the Tureng website for translations of a given word or phrase. The code uses the xsel command to get the selected text from the user's clipboard, and then uses the urllib3 library to send a GET request to the Tureng website. The response is parsed using BeautifulSoup, and the first five translations of the selected word or phrase are extracted and printed. The notify-send command is then used to display a notification containing the selected word or phrase and its translations.

>Bilgisayarınız herhangi bir yerinden(terminal,pdf,tarayıcı vs)
>seçitiğiniz en son kelimeyi Tureng.com dan en-tr arama yapıp 
>ilk 5 sonucu ekrana bildirim olarak gönderen program.

#### Bağımlılıklar
```sh
xsel python3-bs4 python3-urllib3 libnotify-bin
```

#### Calistirmak için;
```sh
#kelimeyi sectikten sonra
python3 selectra.py
```

#### Aktif Kullanım
- Aşağıdaki komuta bir kısayol tuşu atayın. 
```sh
python3 /dosyamHerNeredeyse/selected.py
```
- Ingilizce bir kelime seçin ve atadığınız kısayol tuşuna basın
