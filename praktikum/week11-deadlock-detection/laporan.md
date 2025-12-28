
# Laporan Praktikum Minggu [X]
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : [Nama Mahasiswa]  
- **NIM**   : [NIM Mahasiswa]  
- **Kelas** : [Kelas]

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:

Membuat program sederhana untuk mendeteksi deadlock.
Menjalankan simulasi deteksi deadlock dengan dataset uji.
Menyajikan hasil analisis deadlock dalam bentuk tabel.
Memberikan interpretasi hasil uji secara logis dan sistematis.
Menyusun laporan praktikum sesuai format yang ditentukan

---

## Dasar Teori
mahasiswa akan mempelajari mekanisme deteksi deadlock dalam sistem operasi.
Berbeda dengan Minggu 7 yang berfokus pada pencegahan dan penghindaran deadlock, pada minggu ini mahasiswa diarahkan untuk mendeteksi deadlock yang telah terjadi menggunakan pendekatan algoritmik.

---

## Langkah Praktikum
Bahasa pemrograman bebas (Python / C / Java / lainnya).
Program berbasis terminal, tidak memerlukan GUI.
Fokus penilaian pada logika algoritma deteksi deadlock, bukan kompleksitas bahasa.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
git add .
git commit -m "Minggu 11 - Deadlock Detection"
git push origin main
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
Apa perbedaan antara deadlock prevention, avoidance, dan detection?
Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?
Apa kelebihan dan kekurangan pendekatan deteksi deadlock?

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1.Apa perbedaan antara deadlock prevention, avoidance, dan detection?
1. Deadlock Prevention (Pencegahan Deadlock)
Konsep
Deadlock dicegah sejak awal dengan cara menghilangkan minimal satu dari empat kondisi deadlock.
Empat kondisi deadlock:
Mutual Exclusion
Hold and Wait
No Preemption
Circular Wait

Cara kerja
Sistem menerapkan aturan ketat, misalnya:
Proses harus meminta semua resource sekaligus
Resource boleh direbut paksa (preemption)
Penomoran resource untuk mencegah circular wait

Kelebihan
 Deadlock tidak mungkin terjadi

Kekurangan
Utilisasi resource rendah
Sistem menjadi tidak fleksibel

Contoh
Proses wajib meminta semua resource di awal, jika tidak tersedia → proses menunggu

2. Deadlock Avoidance (Penghindaran Deadlock)
Konsep
Sistem menghindari kondisi tidak aman (unsafe state) dengan menganalisis permintaan resource sebelum diberikan.

Cara kerja
Sistem mengecek apakah alokasi resource aman
Menggunakan algoritma seperti Banker’s Algorithm

Kelebihan
Utilisasi resource lebih baik daripada prevention
Deadlock tetap bisa dihindari

Kekurangan
Perlu informasi lengkap kebutuhan resource di awal
Perhitungan lebih kompleks

Contoh
Banker’s Algorithm memastikan sistem tetap dalam safe state sebelum memberi resource

3. Deadlock Detection (Deteksi Deadlock)
Konsep
Sistem membiarkan deadlock terjadi, lalu mendeteksinya dan melakukan pemulihan.

Cara kerja
Sistem secara berkala menjalankan algoritma deteksi deadlock
Jika deadlock ditemukan → proses dihentikan atau resource direbut

Kelebihan
Lebih fleksibel
Utilisasi resource tinggi

Kekurangan
Deadlock bisa terjadi
Perlu mekanisme recovery (terminasi proses, rollback)

Contoh
Sistem memeriksa wait-for graph untuk menemukan siklus (deadlock)**  
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
   **Alasan Deteksi Deadlock Tetap Diperlukan
1. Pencegahan dan Penghindaran Tidak Selalu Praktis
Deadlock prevention terlalu ketat → menurunkan performa sistem
Deadlock avoidance butuh informasi lengkap kebutuhan resource di awal, yang sering tidak realistis

Akibatnya, sistem nyata tidak selalu menggunakan dua pendekatan tersebut

2. Deadlock Bisa Terjadi pada Sistem Kompleks
Pada sistem modern:
Banyak proses berjalan bersamaan
Resource bersifat dinamis
Interaksi antar proses sulit diprediksi

Deadlock bisa terjadi tanpa disadari, sehingga harus dideteksi

3. Meningkatkan Utilisasi Resource
Dengan deteksi deadlock:
Sistem tidak membatasi alokasi resource secara berlebihan
Resource bisa digunakan semaksimal mungkin

Lebih efisien dibanding prevention

4. Deadlock Tidak Selalu Merugikan Jika Bisa Ditangani

Deadlock bisa jarang terjadi
Lebih murah membiarkan deadlock lalu memperbaikinya daripada mencegahnya terus-menerus

Pendekatan ini sering dipakai pada sistem besar

5. Memberi Mekanisme Pemulihan (Recovery)
Setelah deadlock terdeteksi, sistem bisa:
Menghentikan satu atau lebih proses
Melakukan rollback
Merebut kembali resource

Sistem bisa kembali berjalan normal:**  
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock? 
   | Kelebihan                   | Kekurangan             |
| --------------------------- | ---------------------- |
| Resource digunakan maksimal | Deadlock bisa terjadi  |
| Sistem fleksibel            | Perlu recovery         |
| Tidak butuh info awal       | Overhead deteksi       |
| Cocok sistem besar          | Risiko kehilangan data |


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
