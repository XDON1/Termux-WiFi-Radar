<p align="center">
  <img src="https://img.shields.io/badge/Status-v1.0%20Stable-brightgreen?style=for-the-badge" alt="Status">
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

## 📡 Tentang Project

**GDT Wi‑Fi SIGNAL RADAR** adalah tools sederhana berbasis Python untuk Termux Android yang digunakan untuk melihat informasi jaringan Wi‑Fi di sekitar perangkat.  
Tools ini menggunakan Termux:API untuk membaca informasi yang disediakan oleh Android.

> ⚠️ **BUKAN** Wi‑Fi hacking tool.  
> Tools ini hanya membaca informasi jaringan yang tersedia melalui Android/Termux:API.  
> Tidak digunakan untuk mengambil password, membobol Wi‑Fi, atau menyerang jaringan.

---

## 🎯 Cocok Untuk

- 🔰 Pemula yang ingin belajar jaringan  
- 📱 Pengguna Android dan Termux  
- 🌐 Monitoring jaringan Wi‑Fi  
- 📚 Pembelajaran dasar informasi jaringan  
- 📊 Melihat kekuatan sinyal Wi‑Fi  
- 🐍 Belajar Python dan Termux:API

---

## ✨ Fitur

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

## 🖥️ Preview

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

📱 Instalasi

Jangan khawatir kalau kamu baru pertama kali menggunakan Termux.
Ikuti langkah berikut dari atas sampai bawah.

1. 📲 Install Termux

Disarankan menggunakan Termux dari F‑Droid.
⚠️ Hindari menggunakan Termux versi lama dari Google Play karena beberapa versi lama tidak lagi mendapatkan pembaruan yang diperlukan.

1. Download F‑Droid: https://f-droid.org/
2. Buka F‑Droid
3. Cari Termux
4. Install Termux

2. 🔌 Install Termux:API

Masih melalui F‑Droid, cari Termux:API kemudian install.

⚠️ Penting: Termux dan Termux:API sebaiknya berasal dari sumber yang sama.
Disarankan: Termux → F‑Droid, Termux:API → F‑Droid.
Jangan mencampur aplikasi Termux dari sumber berbeda karena dapat menyebabkan masalah signature atau kompatibilitas.

3. 🔄 Update Termux

Buka aplikasi Termux, jalankan:

```bash
pkg update
pkg upgrade
```

Jika muncul Do you want to continue? [Y/n], ketik y lalu Enter.

4. 🐍 Install Python

```bash
pkg install python
```

Cek versi Python:

```bash
python --version
```

Jika muncul Python 3.x.x berarti Python berhasil terinstall.