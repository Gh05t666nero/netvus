# Introduction
**NETVUS** adalah singkatan dari **Network CVE Vulnerability Scanner**, merupakan alat pemindaian kerentanan CVE jaringan yang powerfull. Alat ini terintegrasi dengan database perusahaan peneliti keamanan siber terkemuka di dunia **Tenable**, hal inilah yang membuat **NETVUS** menjadi salah satu alat scanner jaringan yang unggul.

# Fitur-Fitur
* **Identifikasi Kerentanan**
  * Dengan mengandalkan pemindaian jaringan **Nmap**, memungkinkan alat ini untuk memindai port terbuka, product, dan versi teknologi yang digunakan oleh server informasi tersebut digunakan untuk mengidentifikasi paparan CVE.
* **Melihat Detail Kerentanan**
  * **NETVUS** dilengkapi dengan pencari informasi mengenai kerentanan yang ditemukan melalui **Exploit ID**. Hal ini dapat membantu pengguna untuk melihat **Exploit Title**, **Synopsis**, **Description**, **Remediation**, dan **Referensi CVE**.

# Instalasi
* **Linux**
  ```bash
  pip3 install -r requirements.txt
  ```
* **Termux**
  ```bash
  pip install -r requirements.txt
  ```

# Penggunaan
* **Menampilkan Pesan Bantuan**
  ```bash
  python3 netvus.py -
  ```
* **Memindai Kerentanan**
* 
