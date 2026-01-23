# Laporan Praktikum Minggu 14

Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas

* **Nama**  : Muhammad Reza Fahlevi
* **NIM**   : 250202955
* **Kelas** : 1 IKRA
* **Program Studi** : Ilmu Komputer

---

## Pendahuluan (Introduction)

Docker merupakan teknologi containerisasi yang memungkinkan aplikasi dijalankan secara terisolasi dengan memanfaatkan kernel sistem operasi host. Salah satu keunggulan utama Docker adalah kemampuannya dalam mengelola dan membatasi penggunaan sumber daya seperti CPU dan memori, sehingga beberapa container dapat berjalan secara bersamaan tanpa saling mengganggu.

Namun, tanpa pembatasan resource, sebuah container berpotensi menggunakan CPU dan memori secara berlebihan yang dapat menyebabkan penurunan performa sistem maupun container lain. Oleh karena itu, mekanisme pembatasan resource menjadi aspek penting dalam penerapan Docker, khususnya pada lingkungan multi-container dan sistem produksi.

Praktikum ini bertujuan untuk menguji dan menganalisis pengaruh pembatasan CPU dan memori terhadap performa container Docker dengan menggunakan program uji berbasis Python.

Tujuan praktikum ini adalah:

1. Membuat Dockerfile sederhana untuk menjalankan aplikasi uji.
2. Menjalankan container dengan dan tanpa pembatasan CPU dan memori.
3. Mengamati perbedaan performa dan penggunaan resource container.

---

## Metode (Methods)

### Lingkungan Uji

* Sistem Operasi: Windows 11
* Platform Container: Docker Desktop (WSL2)
* Bahasa Pemrograman: Python 3.x
* Tools Monitoring: `docker stats`

### Struktur Folder

```
week13-docker-resource-limit
 ┣ code
 ┃ ┗ projeck-docker
 ┃ ┃ ┣ app.py
 ┃ ┃ ┣ Dockerfile
 ┃ ┃ ┗ requirements.txt
 ┣ screenshots
 ┃ ┣ docker_stats.png
 ┃ ┣ ssstrestestcpunonlimit.png
 ┃ ┣ sstestcpudenganlimit.png
 ┃ ┗ sstestmemoridenganlimit.png
 ┗ laporan.md
```

### Program Uji

Program Python digunakan untuk melakukan stress test CPU dan memori dengan cara menjalankan loop intensif CPU dan melakukan alokasi memori bertahap hingga mencapai batas tertentu.

### Langkah Praktikum

1. Menulis program Python untuk uji CPU dan memori.
2. Membuat Dockerfile untuk menjalankan program di dalam container.
3. Melakukan build image Docker.
4. Menjalankan container tanpa pembatasan resource.
5. Menjalankan container dengan pembatasan CPU dan memori menggunakan parameter Docker.
6. Mengamati penggunaan resource menggunakan perintah `docker stats`.

---

## Hasil (Results)

Hasil pengujian menunjukkan perbedaan yang signifikan antara container yang dijalankan tanpa pembatasan resource dan container dengan pembatasan CPU dan memori.

### Tanpa Resource Limit

* Penggunaan CPU dapat mencapai 100% atau lebih (multi-core).
* Penggunaan memori meningkat secara terus-menerus hingga mendekati kapasitas RAM host.
* Proses berjalan lebih cepat karena tidak ada pembatasan sumber daya.

### Dengan Resource Limit

* Penggunaan CPU dibatasi sesuai nilai parameter `--cpus`.
* Penggunaan memori berhenti pada batas yang ditentukan (misalnya 500 MB).
* Ketika memori mencapai batas, proses mengalami `MemoryError` atau dihentikan oleh OOM Killer.
* Performa aplikasi menjadi lebih lambat dibandingkan tanpa limit.

Penggunaan CPU dan memori dapat dimonitor secara real-time menggunakan perintah:

```bash
docker stats
```

---

## Analisis dan Pembahasan (Discussion)

### Hubungan dengan Teori Sistem Operasi

Docker tidak menggunakan kernel sendiri, melainkan berjalan langsung di atas kernel Linux. Oleh karena itu, pengelolaan dan pembatasan resource container sepenuhnya ditangani oleh kernel host.

Pembatasan CPU dan memori pada Docker dilakukan menggunakan fitur **control groups (cgroups)**:

* **CPU cgroups** membatasi jatah waktu CPU yang dapat digunakan oleh container.
* **Memory cgroups** membatasi jumlah maksimum memori yang dapat dialokasikan.

Ketika aplikasi di dalam container melakukan system call seperti `malloc()`, `sleep()`, atau penjadwalan CPU, permintaan tersebut diproses oleh kernel host. Apabila penggunaan memori melebihi batas yang ditentukan, kernel dapat menolak alokasi atau menghentikan proses melalui mekanisme **OOM Killer**.

### Perbedaan Lingkungan Linux dan Windows

| Aspek         | Linux               | Windows                    |
| ------------- | ------------------- | -------------------------- |
| Kernel        | Native Linux Kernel | Windows Kernel             |
| Docker        | Langsung di kernel  | Melalui WSL2 / VM          |
| Akurasi Limit | Tinggi              | Bergantung konfigurasi WSL |
| Performa      | Stabil dan cepat    | Sedikit lebih lambat       |

Pada sistem Linux, pembatasan resource berjalan lebih presisi karena Docker menggunakan kernel secara langsung. Sementara itu, pada Windows, Docker berjalan di atas kernel Linux melalui WSL2 sehingga performa dan limit resource dipengaruhi oleh konfigurasi VM.

---

## Kesimpulan (Conclusion)

Berdasarkan hasil praktikum yang dilakukan, dapat disimpulkan bahwa:

1. Docker mendukung pembatasan CPU dan memori untuk menjaga kestabilan sistem.
2. Pembatasan resource memanfaatkan fitur kernel Linux berupa control groups (cgroups).
3. Container dengan resource limit memiliki performa yang lebih terkontrol namun lebih lambat dibandingkan container tanpa limit.
4. Penerapan resource limit sangat penting pada lingkungan multi-container dan sistem produksi.

---

## Refleksi Diri

* **Bagian paling menantang:** Memahami mekanisme kerja cgroups dan dampaknya terhadap performa aplikasi.
* **Cara mengatasinya:** Mempelajari dokumentasi Docker dan melakukan eksperimen langsung dengan berbagai konfigurasi limit CPU dan memori.

---

**Credit:**
*Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa*
