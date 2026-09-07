<div align="center"> <img src="Logo.svg" alt="Termux WiFi Radar Logo" width="120" />
📡 Termux WiFi Radar

Wi-Fi Scanner & Signal Monitor untuk Termux Android

<p align="center"> <img src="https://img.shields.io/badge/Status-v1.0%20Stable-brightgreen?style=for-the-badge" alt="Status" /> <a href="https://github.com/XDON1/Termux-WiFi-Radar/stargazers"> <img src="https://img.shields.io/github/stars/XDON1/Termux-WiFi-Radar?style=for-the-badge&color=8A2BE2" alt="Stars" /> </a> <a href="LICENSE"> <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" /> </a> </p> <p align="center"> <img src="https://img.shields.io/badge/Platform-Android-3DDC84?style=flat-square&logo=android&logoColor=white" alt="Android" /> <img src="https://img.shields.io/badge/Termux-000000?style=flat-square&logo=termux&logoColor=white" alt="Termux" /> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" /> </p> <p align="center"> 🔗 <b>GitHub:</b> <a href="https://github.com/XDON1/Termux-WiFi-Radar"> XDON1/Termux-WiFi-Radar </a> </p> </div>
📡 Tentang Project
Wi-Fi Scanner & Signal Monitor untuk Termux Android

Termux WiFi Radar adalah tools sederhana berbasis Python untuk Termux Android yang digunakan untuk melihat informasi jaringan Wi-Fi di sekitar perangkat.

Tools ini menggunakan Termux:API untuk membaca informasi yang disediakan oleh Android.

⚠️ Termux WiFi Radar bukan Wi-Fi hacking tool.

Tools ini hanya membaca informasi jaringan yang tersedia melalui Android/Termux:API. Tools ini tidak digunakan untuk mengambil password, membobol Wi-Fi, atau menyerang jaringan.

🔗 Repository

GitHub: XDON1/Termux-WiFi-Radar

📡 Tentang Project

Termux WiFi Radar dibuat untuk membantu pengguna melihat informasi jaringan Wi-Fi secara sederhana langsung dari terminal Android.

Project ini cocok untuk:

🔰 Pemula yang ingin belajar jaringan
📱 Pengguna Android dan Termux
🌐 Monitoring jaringan Wi-Fi
📚 Pembelajaran dasar informasi jaringan
📊 Melihat kekuatan sinyal Wi-Fi
🐍 Belajar Python dan Termux:API
✨ Fitur

Termux WiFi Radar menampilkan:

📶 Wi-Fi yang sedang digunakan
🔎 Wi-Fi yang berada di sekitar
📊 Kekuatan sinyal dalam dBm
📈 Persentase kekuatan sinyal
📡 BSSID
🌐 IP Address Wi-Fi aktif
📻 Frequency
📺 Channel
⭐ Penanda Wi-Fi yang sedang terhubung
🎨 Tampilan terminal berwarna
🔄 Pembaruan otomatis setiap 3 detik
🖥️ Preview

Contoh tampilan terminal:

╔══════════════════════════════════════════════════════╗
║              GDT Termux Wi-Fi Radar                 ║
╚══════════════════════════════════════════════════════╝

● WIFI YANG SEDANG DIGUNAKAN
────────────────────────────────────────────────────────

SSID : MyWiFi
BSSID: XX:XX:XX:XX:XX:XX
IP   : 192.168.1.10

SIGNAL : -45 dBm
██████████████████░░ 90%

◉ WIFI DI SEKITAR
────────────────────────────────────────────────────────

★ 01  MyWiFi
   BSSID   : XX:XX:XX:XX:XX:XX
   Signal  : -45 dBm
   ██████████████████░░ 90%
   Freq    : 2437 MHz
   Channel : 6

02  NeighborWiFi
    BSSID   : XX:XX:XX:XX:XX:XX
    Signal  : -67 dBm
    █████████████░░░░░░ 66%
    Freq    : 2462 MHz
    Channel : 11

03  AnotherWiFi
    BSSID   : XX:XX:XX:XX:XX:XX
    Signal  : -81 dBm
    ███████░░░░░░░░░░░░ 38%

↻ Update setiap 3 detik...

Keterangan

Simbol:

★


menunjukkan Wi-Fi yang sedang digunakan oleh perangkat.

📱 Instalasi

Jangan khawatir kalau kamu baru pertama kali menggunakan Termux.

Ikuti langkah berikut dari atas sampai bawah.

1. 📲 Install Termux

Disarankan menggunakan Termux dari F-Droid.

⚠️ Hindari menggunakan Termux versi lama dari Google Play karena beberapa versi lama tidak lagi mendapatkan pembaruan yang diperlukan.

Download F-Droid:

https://f-droid.org/

Setelah F-Droid terinstall:

Buka F-Droid
Cari Termux
Install Termux
2. 🔌 Install Termux:API

Masih melalui F-Droid, cari:

Termux:API


Kemudian install aplikasinya.

⚠️ Penting

Termux dan Termux:API sebaiknya berasal dari sumber yang sama.

Disarankan:

Termux      → F-Droid
Termux:API  → F-Droid


Jangan mencampur aplikasi Termux dari sumber berbeda karena dapat menyebabkan masalah signature atau kompatibilitas.

3. 🔄 Update Termux

Buka aplikasi Termux.

Jalankan:

pkg update


Kemudian:

pkg upgrade


Jika muncul:

Do you want to continue? [Y/n]


ketik:

y


kemudian tekan Enter.

4. 🐍 Install Python

Install Python:

pkg install python


Setelah selesai, cek versi Python:

python --version


Jika muncul sesuatu seperti:

Python 3.x.x


berarti Python sudah berhasil terinstall.

5. 📡 Install Termux:API Package

Sekarang install package Termux:API di dalam Termux:

pkg install termux-api

⚠️ Perhatikan

Ada dua hal yang berbeda:

Aplikasi Android:

Termux:API


dan

Package di Termux:

termux-api


Kamu membutuhkan keduanya.

6. 📍 Berikan Permission Lokasi

Android pada beberapa versi membutuhkan permission lokasi agar Wi-Fi scanning dapat bekerja.

Buka:

Settings → Apps → Termux → Permissions → Location


Kemudian izinkan akses lokasi sesuai pilihan yang tersedia pada perangkat kamu.

Pastikan:

Wi-Fi       = ON
Location    = ON


terutama jika perangkat kamu memerlukannya untuk melakukan Wi-Fi scan.

🚀 Cara Menjalankan
Cara 1 — Clone Repository

Jika Git belum terinstall:

pkg install git


Kemudian clone project:

git clone https://github.com/XDON1/Termux-WiFi-Radar.git


Masuk ke folder project:

cd Termux-WiFi-Radar


Lihat isi folder:

ls


Kemudian jalankan:

python gdtradar.py

Cara 2 — Download File Secara Manual

Kalau kamu tidak ingin menggunakan Git, kamu juga bisa mendownload repository dari GitHub.

Buka:

https://github.com/XDON1/Termux-WiFi-Radar

Kemudian pilih:

Code → Download ZIP


Setelah itu:

Ekstrak file ZIP
Masuk ke folder project
Buka Termux pada folder tersebut
Jalankan program
python gdtradar.py

🧪 Test Termux:API

Sebelum menjalankan program, sangat disarankan untuk memastikan Termux:API bekerja dengan baik.

Test Wi-Fi yang Sedang Digunakan

Jalankan:

termux-wifi-connectioninfo


Jika berhasil, akan muncul informasi dalam format JSON.

Contoh:

{
  "ssid": "MyWiFi",
  "bssid": "XX:XX:XX:XX:XX:XX",
  "ip": "192.168.1.10"
}

Test Wi-Fi Scan

Jalankan:

termux-wifi-scaninfo


Jika berhasil, command akan menampilkan jaringan Wi-Fi yang berhasil ditemukan.

Jika kedua command tersebut dapat berjalan, biasanya Termux:API sudah siap digunakan oleh script.

▶️ Menjalankan Radar

Setelah semua kebutuhan terinstall:

cd Termux-WiFi-Radar


Kemudian:

python gdtradar.py


Radar akan melakukan pembaruan secara otomatis:

↻ Update setiap 3 detik...


Untuk menghentikan program:

CTRL + C

❗ Troubleshooting
termux-wifi-scaninfo: command not found

Jalankan:

pkg install termux-api


Kemudian pastikan aplikasi Android:

Termux:API


juga sudah terinstall.

🔎 Wi-Fi yang Ditemukan Kosong

Coba periksa:

Wi-Fi Android aktif
Location/GPS aktif jika diperlukan
Termux memiliki permission Location
Aplikasi Termux:API sudah terinstall
Package termux-api sudah terinstall

Kemudian test kembali:

termux-wifi-scaninfo

🔐 Permission Denied

Buka:

Settings → Apps → Termux → Permissions → Location


Kemudian berikan permission lokasi.

Pada beberapa perangkat, kamu juga mungkin perlu mengaktifkan:

Settings → Location

🐍 python: command not found

Install Python:

pkg install python


Kemudian cek:

python --version

📡 Tidak Ada Wi-Fi yang Sedang Terhubung

Pastikan perangkat Android memang sedang terhubung ke jaringan Wi-Fi.

Kemudian coba:

termux-wifi-connectioninfo

📦 Instalasi Cepat

Jika kamu sudah tahu apa yang harus dilakukan, gunakan:

pkg update && pkg upgrade
pkg install python git termux-api
git clone https://github.com/XDON1/Termux-WiFi-Radar.git
cd Termux-WiFi-Radar
python gdtradar.py


⚠️ Jangan lupa: aplikasi Termux:API juga harus terinstall di Android.

🗑️ Menghapus Project

Jika kamu ingin menghapus project:

cd ..


Kemudian:

rm -rf Termux-WiFi-Radar


⚠️ Perhatian

Perintah rm -rf akan menghapus folder beserta seluruh isinya.

Pastikan kamu berada di lokasi yang benar sebelum menjalankan perintah tersebut.

🛑 Menghentikan Program

Saat radar sedang berjalan:

CTRL + C


akan menghentikan program.

⚙️ Persyaratan
Komponen	Status
📱 Android	✅ Required
📟 Termux	✅ Required
🔌 Termux:API App	✅ Required
📦 termux-api package	✅ Required
🐍 Python	✅ Required
📶 Wi-Fi	✅ Required
📍 Location Permission	⚠️ Tergantung perangkat/Android
🌐 Internet	📥 Dibutuhkan saat instalasi/clone
🔐 Disclaimer

Termux WiFi Radar dibuat untuk monitoring dan pembelajaran jaringan pada perangkat sendiri atau lingkungan yang memiliki izin.

Tools ini hanya membaca informasi jaringan yang tersedia melalui API Android/Termux.

Tools ini tidak menyediakan fitur untuk:

❌ Mengambil password Wi-Fi
❌ Membobol jaringan Wi-Fi
❌ Mengakses router tanpa izin
❌ Menyerang perangkat lain
❌ Deauthentication / disconnect attack
❌ Menghindari keamanan jaringan
❌ Mengambil kredensial jaringan

Gunakan tools ini secara bertanggung jawab dan hanya pada perangkat atau jaringan yang kamu miliki atau memiliki izin untuk dianalisis.

⭐ Support Project

Jika project ini membantu kamu belajar tentang:

📡 Wi-Fi
🌐 Networking
📱 Termux
🐍 Python
🤖 Android API

jangan lupa berikan ⭐ Star pada repository.

📄 License

Project ini menggunakan lisensi MIT License.

Lihat file LICENSE untuk informasi lengkap.