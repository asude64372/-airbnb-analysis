import pandas as pd  
import os  
import matplotlib.pyplot as plt
import seaborn as sns

# Airbnb Fiyat Analizi

Bu proje, Avrupa genelindeki Airbnb fiyatlarını analiz etmek için oluşturulmuştur. Veri seti Kaggle'dan alınmış olup, şehir bazında fiyat dağılımı ve oda tiplerine göre fiyat farklarını incelemektedir.

## 📌 Proje İçeriği

- **Veri İşleme:** CSV dosyaları okunmuş, gereksiz sütunlar kaldırılmış ve eksik veriler temizlenmiştir.
- **Analizler:**
  - Şehir bazında ortalama fiyat analizi
  - Oda tiplerine göre fiyat dağılımı
- **Görselleştirme:** Matplotlib ve Seaborn kullanılarak fiyat analizleri için grafikler oluşturulmuştur.

## 📂 Kullanılan Teknolojiler
- **Python**
- **Pandas**
- **Matplotlib & Seaborn**

## 🚀 Çalıştırma Talimatları
1. Projeyi klonlayın:
   ```bash
   git clone https://github.com/asude64372/airbnb-analysis.git
   ```
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Python betiğini çalıştırın:
   ```bash
   python pythonproject1.py
   ```

## 📊 Örnek Çıktılar
Aşağıda projede oluşturulan bazı görselleştirmeler örneklenmiştir:

**Şehir Bazında Ortalama Airbnb Fiyatları:**
![Şehir Fiyatları](docs/city_prices.png)

**Oda Tiplerine Göre Fiyat Dağılımı:**
![Oda Tipleri](docs/room_prices.png)

## 📝 Lisans
Bu proje MIT lisansı altında paylaşılmıştır.

---

Bu README dosyasını ekledikten sonra projeyi GitHub'a yükleyelim:

### **📌 GitHub'a Yükleme Adımları**
```bash
git add .
git commit -m "Airbnb fiyat analizi projesi eklendi"
git push origin main
```

🚀 **Proje şimdi GitHub'da!**