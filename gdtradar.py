import subprocess
import json
import time
import os
import sys
import shutil

# WARNA
RESET   = "\033[0m"
BOLD    = "\033[1m"
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
CYAN    = "\033[96m"
MAGENTA = "\033[95m"
WHITE   = "\033[97m"
GRAY    = "\033[90m"


# FUNGSI UTILITY
def check_termux_command(command):
    #Periksa ketersediaan perintah Termux
    return shutil.which(command) is not None


def signal_percent(dbm):
    #Ubah dBm ke persentase (0-100%)
    try:
        value = 2 * (int(dbm) + 100)
        return max(0, min(100, value))
    except (ValueError, TypeError):
        return 0


def signal_color(percent):
    #Warna berdasarkan persentase
    if percent >= 75:
        return GREEN
    elif percent >= 50:
        return YELLOW
    elif percent >= 25:
        return MAGENTA
    else:
        return RED


def signal_label(percent):
    #Label Penjelasan 
    if percent >= 75:
        return "SANGAT KUAT"
    elif percent >= 50:
        return "KUAT"
    elif percent >= 25:
        return "SEDANG"
    elif percent >= 10:
        return "LEMAH"
    else:
        return "SANGAT LEMAH"


def build_signal_bar(percent, width=20):
   #Bar sinyal ada (#) Bar Kosong (-)
    filled = round(percent / 100 * width)
    return "#" * filled + "-" * (width - filled)


def clear_screen():
    #Perintah Clear Otomatis 
    os.system("clear" if os.name == "posix" else "cls")



# FUNGSI Wi-Fi
def get_connected_wifi():
    #Ambil informasi koneksi Wi-Fi saat ini
    if not check_termux_command("termux-wifi-connectioninfo"):
        print(RED + "Perintah termux-wifi-connectioninfo tidak ditemukan." + RESET)
        return {}

    try:
        result = subprocess.run(
            ["termux-wifi-connectioninfo"],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode != 0:
            return {}
        return json.loads(result.stdout)
    except (json.JSONDecodeError, subprocess.SubprocessError):
        return {}


def scan_wifi_networks():
    #Pindai jaringan Wi-Fi di sekitar dwngan Lokasi 
    if not check_termux_command("termux-wifi-scaninfo"):
        print(RED + "Perintah termux-wifi-scaninfo tidak ditemukan." + RESET)
        return []

    try:
        result = subprocess.run(
            ["termux-wifi-scaninfo"],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode != 0:
            return []
        return json.loads(result.stdout)
    except (json.JSONDecodeError, subprocess.SubprocessError):
        return []


# DISPLAY TAMPILAN 
def display_header():
    #Header Terminal
    print(BOLD + CYAN + "╔══════════════════════════════════════════════════════╗" + RESET)
    print(BOLD + CYAN + "║            GDT Wi-Fi SIGNAL RADAR                  ║" + RESET)
    print(BOLD + CYAN + "╚══════════════════════════════════════════════════════╝" + RESET)
    print()


def display_connected_wifi(wifi_info):
    # Wi-fi yang terhubung
    print(BOLD + GREEN + "  ● WIFI YANG SEDANG DIGUNAKAN" + RESET)
    print(GRAY + "  ─────────────────────────────────────────" + RESET)

    if not wifi_info:
        print(RED + "  ✖ Tidak dapat membaca koneksi Wi-Fi." + RESET)
        print(GRAY + "  Pastikan Wi-Fi aktif dan izin lokasi diberikan." + RESET)
        return

    ssid = wifi_info.get("ssid", "<unknown>")
    bssid = wifi_info.get("bssid", "<unknown>")
    ip = wifi_info.get("ip", "<unknown>")
    rssi = wifi_info.get("rssi", -100)

    percent = signal_percent(rssi)
    color = signal_color(percent)
    label = signal_label(percent)

    print(f"  {CYAN}SSID   {RESET}: {BOLD}{ssid}{RESET}")
    print(f"  {CYAN}BSSID  {RESET}: {bssid}")
    print(f"  {CYAN}IP     {RESET}: {ip}")
    print()
    print(f"  {CYAN}SIGNAL {RESET}: {color}{rssi} dBm{RESET}")
    # Tampilkan bar, persentase, dan label
    print(f"           {color}{build_signal_bar(percent)}{RESET} {color}{percent}%{RESET}")
    print(f"           {color}{label}{RESET}")   # tambahan label


def display_scan_results(netw ─────────────────────────────────────────" + RESET)

    if not networks:
        print(YELLOW + "  Tidak ada hasil scan." + RESET)
        print(GRAY + "  Pastikan Wi-Fi aktif dan izin lokasi Termux diberikan." + RESET)
        return

    # Urutan dari sinyal terkuat
    networks.sort(key=lambda x: x.get("rssi", -100), reverse=True)

    for i, net in enumerate(networks, 1):
        ssid = net.get("ssid", "<hidden>")
        bssid = net.get("bssid", "<unknown>")
        rssi = net.get("rssi", -100)

        percent = signal_percent(rssi)
        color = signal_color(percent)
        label = signal_label(percent)

        # Jaringan Digunakan pakai Tag [MAIN]
        is_current = (current_bssid and bssid.lower() == current_bssid.lower())
        if is_current:
            marker = BOLD + GREEN + "[MAIN]" + RESET
            name_color = BOLD + GREEN
        else:
            marker = "     "  # 5 spasi biar sejajar
            name_color = WHITE

        print(f"{marker} {YELLOW}{i:02d}{RESET} {name_color}{ssid[:25]}{RESET}")
        print(f"    {GRAY}BSSID :{RESET} {bssid}")
        # Tampilkan dBm, bar, persentase, dan label
        print(f"    {GRAY}Signal:{RESET} {color}{rssi} dBm{RESET}  {color}{build_signal_bar(percent, 15)}{RESET} {color}{percent}%{RESET}  {color}{label}{RESET}")
        print()   # pemisah


def display_footer():
    #footer
    print(GRAY + "  ─────────────────────────────────────────" + RESET)
    print(BOLD + CYAN + "  RADAR UPDATE SETIAP 8 DETIK" + RESET)
    print(GRAY + "  CTRL+C untuk keluar" + RESET)



# FUNGSI UTAMA
def main():
    #loop utama
    if not check_termux_command("termux-wifi-connectioninfo") and \
       not check_termux_command("termux-wifi-scaninfo"):
        print(RED + "Perintah Termux untuk Wi-Fi tidak ditemukan." + RESET)
        print("Pastikan Termux API sudah diinstal dan izin diberikan.")
        sys.exit(1)

    try:
        while True:
            clear_screen()
            display_header()

            current_wifi = get_connected_wifi()
            display_connected_wifi(current_wifi)
            print()

            current_bssid = current_wifi.get("bssid") if current_wifi else None
            networks = scan_wifi_networks()
            display_scan_results(networks, current_bssid)

            display_footer()
            time.sleep(8)

    except KeyboardInterrupt:
        clear_screen()
        print(BOLD + GREEN + "Program dihentikan. Sampai jumpa!" + RESET)
        sys.exit(0)


if __name__ == "__main__":
    main()