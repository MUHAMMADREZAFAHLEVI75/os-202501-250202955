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

*(Screenshot: instalasi_vm.png)*

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

*(Screenshot: konfigurasi_resource.png)*

---

### 3. Instalasi OS Guest

1. Menjalankan VM.
2. Memilih file ISO windows sebagai media instalasi.
3. Mengikuti langkah instalasi hingga selesai.
4. Melakukan login dan memastikan OS berjalan normal.

*(Screenshot: os_guest_running.png)*

---

### 4. Konfigurasi Resource VM

* Sebelum perubahan: 8 Core CPU dan 8 GB RAM.
* Setelah perubahan: 6 Core CPU dan 5 GB RAM.

**Hasil Pengamatan:**
Setelah resource ditingkatkan, performa VM menjadi lebih responsif, proses booting lebih cepat, dan aplikasi berjalan lebih lancar.

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
