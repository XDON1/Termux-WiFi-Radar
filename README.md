<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/github/stars/XDON1/Termux-WiFi-Radar?style=for-the-badge&color=8A2BE2" alt="Stars">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Android-3DDC84?style=flat-square&logo=android&logoColor=white" alt="Android">
  <img src="https://img.shields.io/badge/Termux-000000?style=flat-square&logo=termux&logoColor=white" alt="Termux">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
</p>

<p align="center">
  <a href="https://github.com/XDON1/Termux-WiFi-Radar">🔗 GitHub: XDON1/Termux-WiFi-Radar</a>
</p>

---

## Tentang Project

**GDT Wi‑Fi SIGNAL RADAR** adalah tools sederhana berbasis Python untuk Termux Android yang digunakan untuk melihat informasi jaringan Wi‑Fi di sekitar perangkat.  
Tools ini menggunakan Termux:API untuk membaca informasi yang disediakan oleh Android.

> **BUKAN** Wi‑Fi hacking tool.  
> Tools ini hanya membaca informasi jaringan yang tersedia melalui Android/Termux:API.  
> Tidak digunakan untuk mengambil password, membobol Wi‑Fi, atau menyerang jaringan.

---

## Cocok Untuk

- 🔰 Pemula yang ingin belajar jaringan  
- 📱 Pengguna Android dan Termux  
- 🌐 Monitoring jaringan Wi‑Fi  
- 📚 Pembelajaran dasar informasi jaringan  
- 📊 Melihat kekuatan sinyal Wi‑Fi  
- 🐍 Belajar Python dan Termux:API

---

## FITUR 

| Fitur | Keterangan |
|-------|------------|
| 📶 | Wi‑Fi yang sedang digunakan |
| 🔎 | Wi‑Fi yang berada di sekitar |
| 📊 | Kekuatan sinyal dalam **dBm** |
| 📈 | Persentase kekuatan sinyal |
| 🏷️ | Label kekuatan sinyal (SANGAT KUAT, KUAT, SEDANG, LEMAH, SANGAT LEMAH) |
| 📡 | BSSID |
| 🌐 | IP Address Wi‑Fi aktif |
| ⭐ | Penanda `[MAIN]` untuk Wi‑Fi yang sedang terhubung |
| 🎨 | Tampilan terminal berwarna |
| 🔄 | Pembaruan otomatis setiap **8 detik** |
| 📊 | Bar sinyal sederhana (`#` dan `-`) |

---

## TAMPILAN 

```bash
╔══════════════════════════════════════════════════════╗
║            GDT Wi-Fi SIGNAL RADAR                  ║
╚══════════════════════════════════════════════════════╝

  ● WIFI YANG SEDANG DIGUNAKAN
  ─────────────────────────────────────────
  SSID   : MyWiFi
  BSSID  : XX:XX:XX:XX:XX:XX
  IP     : 192.168.1.10

  SIGNAL : -45 dBm
           #################### 90%
           KUAT

  ◉ WIFI DI SEKITAR
  ─────────────────────────────────────────
[MAIN] 01  MyWiFi
    BSSID : XX:XX:XX:XX:XX:XX
    Signal: -45 dBm  ############### 90%  KUAT

  02  NeighborWiFi
    BSSID : XX:XX:XX:XX:XX:XX
    Signal: -67 dBm  ###########---- 66%  SEDANG

  03  AnotherWiFi
    BSSID : XX:XX:XX:XX:XX:XX
    Signal: -81 dBm  ######--------- 38%  LEMAH

  ─────────────────────────────────────────
  RADAR UPDATE SETIAP 8 DETIK
  CTRL+C untuk keluar
```

Keterangan: [MAIN] menandakan Wi‑Fi yang sedang digunakan oleh perangkat.
---

TUTORIAL 
Jangan khawatir kalau kamu baru pertama kali menggunakan Termux.
Ikuti langkah berikut dari atas sampai bawah.

## 1. Install Termux
Disarankan menggunakan Termux dari F‑Droid.
⚠️ Hindari menggunakan Termux versi lama dari Google Play karena beberapa versi lama tidak lagi mendapatkan pembaruan yang diperlukan.

1. Download F‑Droid: https://f-droid.org/
2. Buka F‑Droid
3. Cari Termux
4. Install Termux

## 2. Install Termux:API
Masih melalui F‑Droid, cari Termux:API kemudian install.

⚠️ Penting: Termux dan Termux:API sebaiknya berasal dari sumber yang sama.
Disarankan: Termux → F‑Droid, Termux:API → F‑Droid.
Jangan mencampur aplikasi Termux dari sumber berbeda karena dapat menyebabkan masalah signature atau kompatibilitas.

## 3. Update Termux
Buka aplikasi Termux, jalankan:
```bash
pkg update
pkg upgrade
```
Jika muncul Do you want to continue? [Y/n], ketik y lalu Enter.

## 4. Install Python
```bash
pkg install python
```

Cek versi Python:
```bash
python --version
```
Jika muncul Python 3.x.x berarti Python berhasil terinstall.

## 5. Install Termux:API Package

Install package Termux:API di dalam Termux:
```bash
pkg install termux-api
```

⚠️ Perhatikan: Ada dua hal yang berbeda:
• Aplikasi Android: Termux:API
• Package di Termux: termux-api
  Kamu membutuhkan keduanya.

## 6. Berikan Permission Lokasi

Android pada beberapa versi membutuhkan permission lokasi agar Wi‑Fi scanning dapat bekerja.

Buka:
```
Settings → Apps → Termux → Permissions → Location
```

Kemudian izinkan akses lokasi sesuai pilihan yang tersedia pada perangkat kamu.
Pastikan:
· Wi‑Fi = ON
· Location = ON
terutama jika perangkat kamu memerlukannya untuk melakukan Wi‑Fi scan.

---

## Cara Menjalankan
Clone Repository

Jika Git belum terinstall:
```bash
pkg install git
```

Clone project:
```bash
git clone https://github.com/XDON1/Termux-WiFi-Radar.git
```

Masuk ke folder project:
```bash
cd Termux-WiFi-Radar
```

Jalankan:
```bash
python gdtradar.py
```

Cara 2 — Download File Secara Manual
1. Buka https://github.com/XDON1/Termux-WiFi-Radar
2. Pilih Code → Download ZIP
3. Ekstrak file ZIP
4. Masuk ke folder project
5. Buka Termux pada folder tersebut
6. Jalankan program:

```bash
python gdtradar.py
```

---

## Test Termux:API
**Sebelum menjalankan program, sangat disarankan untuk memastikan Termux:API bekerja dengan baik.
Test Wi‑Fi yang Sedang Digunakan**
```bash
termux-wifi-connectioninfo
```
**Jika berhasil, akan muncul informasi dalam format JSON:**
```json
{
  "ssid": "MyWiFi",
  "bssid": "XX:XX:XX:XX:XX:XX",
  "ip": "192.168.1.10"
}
```

**Test Wi‑Fi Scan**
```bash
termux-wifi-scaninfo
```

**Jika berhasil, command akan menampilkan jaringan Wi‑Fi yang berhasil ditemukan.
Jika kedua command tersebut dapat berjalan, Termux:API sudah siap digunakan oleh script**

---

## Menjalankan Radar
Setelah semua kebutuhan terinstall:

```bash
cd Termux-WiFi-Radar
python gdtradar.py
```

Radar akan melakukan pembaruan secara otomatis setiap 8 detik.
Untuk menghentikan program:

```
CTRL + C
```

---

❗ Troubleshooting
termux-wifi-scaninfo: command not found
```bash
pkg install termux-api
```
Pastikan aplikasi Android Termux:API juga sudah terinstall.


🚨 Wi‑Fi yang Ditemukan Kosong
**Periksa hal berikut:
· Wi‑Fi Android aktif
· Location/GPS aktif jika diperlukan
· Termux memiliki permission Location
· Aplikasi Termux:API sudah terinstall
· Package termux-api sudah terinstall**

Kemudian test kembali:
```bash
termux-wifi-scaninfo
```

## Permission Denied
Buka:
```
Settings → Apps → Termux → Permissions → Location
```
Berikan permission lokasi.
Pada beberapa perangkat, aktifkan juga:
```
Settings → Location
```

## python: command not found
```bash
pkg install python
python --version
```

## Tidak Ada Wi‑Fi yang Sedang Terhubung
Pastikan perangkat Android memang sedang terhubung ke jaringan Wi‑Fi.
```bash
termux-wifi-connectioninfo
```

---

## Instalasi Cepat
Jika kamu sudah tahu apa yang harus dilakukan:
```bash
pkg update && pkg upgrade
pkg install python git termux-api
git clone https://github.com/XDON1/Termux-WiFi-Radar.git
cd Termux-WiFi-Radar
python gdtradar.py
```
⚠️ Jangan lupa: aplikasi Termux:API juga harus terinstall di Android.

---

## Menghapus Project
```bash
cd ..
rm -rf Termux-WiFi-Radar
```
## Perhatian: 
Perintah rm -rf akan menghapus folder beserta seluruh isinya. Pastikan kamu berada di lokasi yang benar sebelum menjalankan perintah tersebut.

---

## Menghentikan Program
Saat radar sedang berjalan:
```
CTRL + C
```
akan menghentikan program.

---

## Disclaimer
GDT Wi‑Fi SIGNAL RADAR dibuat untuk monitoring dan pembelajaran jaringan pada perangkat sendiri atau lingkungan yang memiliki izin.

Tools ini hanya membaca informasi jaringan yang tersedia melalui API Android/Termux

---

⭐ Support Project
Jika project ini membantu kamu belajar jangan lupa berikan ⭐ Star pada repository.

---

📄 License

Project ini menggunakan lisensi MIT License.
Lihat file LICENSE untuk informasi lengkap.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/XDON1">XDON1</a>
</p>
