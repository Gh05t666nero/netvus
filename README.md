# Introduction
**NETVUS** adalah singkatan dari **Network CVE Vulnerability Scanner**, merupakan alat pemindaian kerentanan CVE jaringan yang powerfull. Alat ini terintegrasi dengan database perusahaan peneliti keamanan siber terkemuka di dunia **Tenable**, hal inilah yang membuat **NETVUS** menjadi salah satu alat scanner jaringan yang unggul.

## Fitur-Fitur
* **Memindai Kerentanan**
  * Dengan mengandalkan pemindaian jaringan **Nmap**, memungkinkan alat ini untuk memindai port terbuka, product, dan versi teknologi yang digunakan oleh server informasi tersebut digunakan untuk mengidentifikasi paparan CVE.
* **Melihat Detail Kerentanan**
  * **NETVUS** dilengkapi dengan pencari informasi mengenai kerentanan yang ditemukan melalui **Exploit ID**. Hal ini dapat membantu pengguna untuk melihat **Exploit Title**, **Synopsis**, **Description**, **Remediation**, dan **Referensi CVE**.

## Instalasi
* **Linux**
  ```bash
  pip3 install -r requirements.txt
  ```
* **Termux**
  ```bash
  pip install -r requirements.txt
  ```

## Penggunaan
* **Menampilkan Pesan Bantuan**
  ```bash
  python3 netvus.py -h
  ```
* **Memindai Kerentanan**
  ```bash
  python3 netvus.py -t <IP/Domain>
  ```
* **Melihat Detail Kerentanan**
  ```bash
  python3 netvus.py -s <Exploit ID>
  ```
## Lisensi
[GNU General Public License](https://github.com/Gh05t666nero/netvus/blob/main/LICENSE)
