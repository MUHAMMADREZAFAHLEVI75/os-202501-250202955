# Laporan Praktikum Minggu 12

## Virtualisasi Menggunakan Virtual Machine

---

### Identitas Kelompok

* Mata Kuliah : Sistem Operasi
* Topik       : Virtualisasi Menggunakan Virtual Machine
* Minggu      : 12
* Anggota     : Muhammad Reza Fahlevi (250202955)
              : tri agustin wahyuningtyas (250202970)
              : amarudin ibnu salam (250202929)

---

## A. Pendahuluan

Virtualisasi merupakan teknologi yang memungkinkan sebuah sistem komputer menjalankan lebih dari satu sistem operasi secara bersamaan pada satu perangkat keras fisik. Pada praktikum ini digunakan **Virtual Machine (VM)** untuk menginstal dan menjalankan sistem operasi guest di atas sistem operasi host menggunakan aplikasi virtualisasi.

Praktikum ini bertujuan untuk memahami hubungan antara **host OS**, **guest OS**, dan **hypervisor**, serta bagaimana pengaturan resource seperti CPU, RAM, dan storage memengaruhi kinerja sistem.

---

## B. Tujuan Praktikum

1. Menginstal software virtualisasi (VirtualBox/VMware).
2. Membuat dan menjalankan OS guest pada VM.
3. Mengatur konfigurasi resource VM.
4. Memahami mekanisme isolasi dan proteksi OS melalui virtualisasi.
5. Menyusun laporan praktikum secara sistematis.

---

## C. Alat dan Bahan

* PC
* Sistem Operasi Host: Windows 11
* Software Virtualisasi: **Oracle VirtualBox**
* File ISO OS Guest: **windows**
* Koneksi internet

---

## D. Langkah Praktikum

### 1. Instalasi VirtualBox

1. Mengunduh Oracle VirtualBox dari situs resmi.
2. Melakukan proses instalasi hingga selesai.
3. Mengaktifkan fitur virtualisasi (VT-x / AMD-V) melalui BIOS.

<img width="1920" height="1080" alt="Screenshot 2026-01-14 234158" src="https://github.com/user-attachments/assets/929e684a-983d-422d-a445-b219f48556e4" />


---

### 2. Pembuatan Virtual Machine

1. Membuka aplikasi VirtualBox.
2. Membuat VM baru dengan spesifikasi:

   * Nama VM: windows 10
   * Tipe OS: windows
   * Versi: 10 2h22
3. Mengatur resource awal:

   * CPU: 8 Core
   * RAM: 8048 MB
   * Storage: 50 GB (nvme)

<img width="1900" height="1047" alt="Screenshot 2026-01-15 001158" src="https://github.com/user-attachments/assets/4edfcdb8-d14c-4a3c-9412-168d8a68d099" />
<img width="1919" height="1079" alt="Screenshot 2026-01-15 001101" src="https://github.com/user-attachments/assets/f26aca65-3f9e-45bc-ac47-1e63e12b862a" />
<img width="1919" height="1079" alt="Screenshot 2026-01-15 001115" src="https://github.com/user-attachments/assets/2c1ad9eb-c9df-4095-8608-21601f0c9b32" />
<img width="1906" height="1076" alt="Screenshot 2026-01-15 001145" src="https://github.com/user-attachments/assets/e938f9ab-14c1-41de-9b89-53d6665a3661" />


---

### 3. Instalasi OS Guest

1. Menjalankan VM.
2. Memilih file ISO windows sebagai media instalasi.
3. Mengikuti langkah instalasi hingga selesai.
4. Melakukan login dan memastikan OS berjalan normal.

<img width="1919" height="1079" alt="Screenshot 2026-01-15 001430" src="https://github.com/user-attachments/assets/af59ec04-e3b4-4a41-88f3-2ca1c4dbbb7f" />
<img width="1919" height="1079" alt="Screenshot 2026-01-15 001555" src="https://github.com/user-attachments/assets/3d9d84fd-41fb-4688-ad95-222424ec55c2" />
<img width="1891" height="1065" alt="Screenshot 2026-01-15 001715" src="https://github.com/user-attachments/assets/dba98ca0-190b-4615-8246-1010c8efa4ed" />
<img width="1919" height="1079" alt="Screenshot 2026-01-15 001805" src="https://github.com/user-attachments/assets/ec2069d7-74ad-48dc-a0f2-e63ba89b70e0" />
<img width="1901" height="1067" alt="Screenshot 2026-01-15 002030" src="https://github.com/user-attachments/assets/b59c17e1-cecc-46eb-9dc5-ad2ac8afcedc" />
<img width="1909" height="1074" alt="Screenshot 2026-01-15 002436" src="https://github.com/user-attachments/assets/4fb22d23-775d-4245-8f1d-1fa1d6270334" />


---

### 4. Konfigurasi Resource VM

* Sebelum perubahan: 8 Core CPU dan 8 GB RAM.
* Setelah perubahan: 6 Core CPU dan 5 GB RAM.

**Hasil Pengamatan:**
Setelah resource ditingkatkan, performa VM menjadi lebih responsif, proses booting lebih cepat, dan aplikasi berjalan lebih lancar.

<img width="1907" height="1074" alt="Screenshot 2026-01-15 002639" src="https://github.com/user-attachments/assets/437b1d17-fe79-4aa9-90f6-b170ebf570ef" />
<img width="1864" height="1044" alt="Screenshot 2026-01-15 004103" src="https://github.com/user-attachments/assets/13dce7cb-3a43-4a59-b849-872773d8a995" />
<img width="1903" height="1069" alt="Screenshot 2026-01-15 004227" src="https://github.com/user-attachments/assets/b8678e5a-3eea-4302-b0f0-7847288ab559" />


---

## E. Analisis Proteksi OS

Virtual Machine menyediakan **isolasi** antara sistem host dan guest. Jika terjadi error atau malware pada OS guest, maka tidak akan langsung memengaruhi OS host.

Konsep ini mirip dengan **sandboxing**, di mana sistem guest berjalan dalam lingkungan terisolasi. Selain itu, virtualisasi juga mendukung **hardening OS**, karena setiap VM dapat dikonfigurasi dengan kebijakan keamanan masing-masing.

---

## F. Quiz

### 1. Apa perbedaan antara host OS dan guest OS?

**Host OS** adalah sistem operasi utama yang berjalan langsung di atas hardware, sedangkan **guest OS** adalah sistem operasi yang berjalan di dalam virtual machine di atas host OS.

### 2. Apa peran hypervisor dalam virtualisasi?

Hypervisor berperan sebagai pengelola virtualisasi yang mengatur pembagian resource hardware (CPU, RAM, storage) antara host dan guest OS serta memastikan isolasi antar VM.

### 3. Mengapa virtualisasi meningkatkan keamanan sistem?

Karena virtualisasi menyediakan isolasi sistem, sehingga gangguan atau serangan pada satu VM tidak langsung memengaruhi sistem lain maupun host OS.

---

## G. Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa teknologi virtualisasi memungkinkan menjalankan beberapa sistem operasi secara bersamaan dengan aman dan efisien. Pengaturan resource yang tepat sangat memengaruhi performa VM, dan mekanisme isolasi meningkatkan keamanan sistem secara keseluruhan.

---

## H. Referensi

1. Silberschatz, A., Galvin, P., Gagne, G. *Operating System Concepts*.
2. Tanenbaum, A. *Modern Operating Systems*.
3. Oracle VirtualBox Documentation.
4. OSTEP – Virtualization.
