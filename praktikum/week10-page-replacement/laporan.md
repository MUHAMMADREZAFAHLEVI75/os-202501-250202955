
# Laporan Praktikum Minggu [X]
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Muhammad Reza Fahlevi
- **NIM**   : 250202955
- **Kelas** : 1IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.


---

## Dasar Teori
Page Replacement dalam Sistem Operasi
Page replacement adalah mekanisme pada sistem operasi untuk menentukan halaman (page) mana yang harus digantikan ketika memori utama (RAM) sudah penuh dan terjadi page fault. Tujuannya adalah mengoptimalkan penggunaan memori dan meminimalkan jumlah page fault.

Algoritma FIFO (First-In First-Out)
FIFO menggantikan halaman yang pertama kali masuk ke memori tanpa memperhatikan seberapa sering atau terakhir halaman tersebut digunakan. Algoritma ini sederhana dan mudah diimplementasikan, tetapi dapat menyebabkan Belady’s Anomaly, yaitu peningkatan page fault meskipun jumlah frame ditambah.

Algoritma LRU (Least Recently Used)
LRU menggantikan halaman yang paling lama tidak digunakan berdasarkan asumsi bahwa halaman yang sering digunakan di masa lalu kemungkinan besar akan digunakan kembali. Algoritma ini umumnya menghasilkan page fault lebih sedikit dibanding FIFO, namun lebih kompleks dalam implementasi karena membutuhkan pencatatan waktu atau urutan akses.

Prinsip Lokalitas Referensi
Kedua algoritma didasarkan pada konsep lokalitas, khususnya temporal locality, yaitu kecenderungan program untuk mengakses kembali halaman yang baru saja digunakan. LRU memanfaatkan prinsip ini lebih optimal dibanding FIFO.

Tujuan Pemilihan Algoritma Page Replacement
Pemilihan algoritma page replacement bertujuan untuk meningkatkan kinerja sistem dengan menurunkan page fault rate, mempercepat eksekusi proses, dan mengelola sumber daya memori secara efisien.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```
---

## Hasil Eksekusi
![WhatsApp Image 2025-12-28 at 15 48 56](https://github.com/user-attachments/assets/69124aa2-6e1c-4aa6-a012-77f333f0245c)
![WhatsApp Image 2025-12-28 at 15 46 41](https://github.com/user-attachments/assets/09cb8548-345a-49d0-bf2f-4433701ea575)



---

## Analisis
   Buat tabel perbandingan seperti berikut:

| Algoritma | Jumlah Page Fault | Keterangan                                                                                             |
| :-------- | :---------------: | :----------------------------------------------------------------------------------------------------- |
| **FIFO**  |       **10**      | Mengganti halaman yang paling awal masuk ke memori tanpa memperhatikan frekuensi atau waktu penggunaan |
| **LRU**   |       **9**       | Mengganti halaman yang paling lama tidak digunakan sehingga lebih sesuai dengan pola akses program     |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.

perbedaan jumlah page fault terjadi karena cara masing-masing algoritma menentukan halaman yang diganti:

FIFO hanya melihat urutan kedatangan halaman.
Akibatnya, halaman yang masih sering digunakan bisa saja dikeluarkan dari memori hanya karena datang lebih awal.

LRU mempertimbangkan riwayat penggunaan halaman.
Halaman yang baru saja digunakan akan dipertahankan, sedangkan yang lama tidak digunakan akan diganti.

Karena pola akses program umumnya memiliki lokalitas temporal (halaman yang sering dipakai akan dipakai lagi), LRU lebih mampu menyesuaikan diri dengan kebutuhan program.

   - Analisis algoritma mana yang lebih efisien dan alasannya.

Berdasarkan hasil simulasi, LRU menghasilkan jumlah page fault lebih sedikit (9) dibandingkan FIFO (10).

Hal ini menunjukkan bahwa LRU lebih efisien dalam penggunaan memori karena:
- Mempertahankan halaman yang sering digunakan
- Mengurangi kemungkinan terjadinya page fault berulang
- Tidak mengalami Belady’s Anomaly

---

## Kesimpulan
Algoritma page replacement FIFO dan LRU berhasil diimplementasikan dan disimulasikan menggunakan reference string dengan 3 frame memori, sehingga proses penggantian halaman dapat diamati secara jelas.

Berdasarkan hasil simulasi, algoritma LRU menghasilkan jumlah page fault lebih sedikit (9) dibandingkan algoritma FIFO (10), karena LRU mempertimbangkan riwayat penggunaan halaman dan memanfaatkan prinsip lokalitas temporal.

Dengan demikian, LRU lebih efisien dibanding FIFO dalam pengelolaan memori, meskipun memiliki tingkat kompleksitas implementasi yang lebih tinggi, sedangkan FIFO lebih sederhana namun kurang optimal dari sisi performa.

---

## E. Tugas & Quiz
### Tugas
1. Buat program simulasi page replacement FIFO dan LRU.
2. Jalankan simulasi dengan dataset uji.
3. Sajikan hasil simulasi dalam tabel atau grafik.
4. Tulis laporan praktikum pada `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Apa perbedaan utama FIFO dan LRU?

FIFO (First In First Out) mengganti halaman yang paling lama berada di memori, tanpa memperhatikan apakah halaman tersebut masih sering digunakan atau tidak.

LRU (Least Recently Used) mengganti halaman yang paling lama tidak digunakan, dengan mempertimbangkan pola akses halaman.

Perbedaan utamanya terletak pada kriteria penggantian halaman: FIFO berdasarkan waktu masuk, sedangkan LRU berdasarkan waktu terakhir digunakan.

2. Mengapa FIFO dapat menghasilkan Belady’s Anomaly?

Belady’s Anomaly adalah kondisi ketika penambahan jumlah frame justru meningkatkan jumlah page fault.

Hal ini terjadi pada FIFO karena algoritma ini tidak mempertimbangkan lokalitas referensi.

Halaman yang sering dipakai bisa saja diganti hanya karena datang lebih awal, sehingga saat dibutuhkan kembali akan menimbulkan page fault tambahan.
Karena bersifat “buta” terhadap pola akses, FIFO rentan mengalami anomali ini.

3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?

LRU memanfaatkan prinsip lokalitas temporal, yaitu halaman yang baru digunakan cenderung akan digunakan kembali dalam waktu dekat.

Dengan mempertahankan halaman yang sering diakses, LRU biasanya mengurangi jumlah page fault.

LRU juga termasuk algoritma yang tidak mengalami Belady’s Anomaly, sehingga performanya lebih stabil.
Akibatnya, LRU umumnya lebih efisien dan optimal dibanding FIFO, meskipun implementasinya lebih komplek

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
