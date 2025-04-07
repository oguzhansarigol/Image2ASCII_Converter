# Image to ASCII Converter

Image to ASCII Converter, görselleri ASCII sanatı haline dönüştüren basit bir Python uygulamasıdır. Uygulama, bir görselin gri tonlamasını alarak her pikseli karakter ile temsil eder ve ortaya görselin metinsel bir versiyonu çıkar.

ASCII çıktısı, WhatsApp gibi platformlarda düzgün görünecek şekilde kod bloğu formatına uygun olarak hazırlanmıştır.

## Özellikler

- Görselleri ASCII karakterlere dönüştürür  
- Terminalden kolayca kullanılabilir  
- Çıktıyı `.txt` dosyasına kaydeder  
- WhatsApp veya benzeri mesajlaşma platformlarına yapıştırmaya uygun  
- Python ile yazılmış, açık kaynak

## Kullanılan Kütüphaneler

- Pillow  
- NumPy

## Kurulum

Gerekli kütüphaneleri yüklemek için:

```bash
pip install pillow numpy
```

## Kullanım

```bash
python script.py
```

Program çalıştıktan sonra görsel dosyasının yolunu girmeniz istenir.  
ASCII çıktısı aynı klasöre `ascii_output.txt` olarak kaydedilir.

## Örnek

Girdi: `image.jpg`  
Çıktı: `ascii_output.txt` (içeriği kod bloğu halinde ASCII karakterlerle)

## Katkı

Her türlü katkıya açıktır. Hataları bildirebilir veya geliştirme için pull request gönderebilirsiniz.

---
