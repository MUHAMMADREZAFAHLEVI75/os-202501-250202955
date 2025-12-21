

# Laporan Praktikum Minggu [IX]
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas
- **NIM**   : 250202970
- **Kelas** : 1IKRA

---

## Tujuan
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.


---

## Dasar Teori

Penjadwalan CPU merupakan komponen inti dalam sistem operasi yang bertugas mengatur alokasi waktu CPU kepada berbagai proses yang berada dalam keadaan ready. Karena CPU hanya dapat mengeksekusi satu proses pada satu waktu, diperlukan mekanisme penjadwalan agar setiap proses memperoleh kesempatan eksekusi secara teratur, efisien, dan adil.

Algoritma penjadwalan CPU digunakan sebagai aturan atau strategi untuk menentukan proses mana yang dieksekusi terlebih dahulu. Setiap algoritma dirancang dengan pendekatan yang berbeda, seperti berdasarkan urutan kedatangan, lama waktu eksekusi, prioritas, atau pembagian waktu (time sharing), sehingga menghasilkan kinerja sistem yang berbeda pula.

Kriteria kinerja penjadwalan menjadi acuan dalam mengevaluasi efektivitas suatu algoritma. Kriteria tersebut meliputi waiting time (waktu proses menunggu di antrian), turnaround time (total waktu sejak proses datang hingga selesai), response time (waktu respon pertama), serta throughput (jumlah proses yang selesai dalam satuan waktu tertentu).

Simulasi algoritma penjadwalan CPU dilakukan untuk memodelkan kondisi eksekusi proses secara sederhana dan terkontrol. Dengan simulasi, dapat dianalisis dampak dari perbedaan algoritma terhadap kinerja sistem tanpa harus mengubah atau mengganggu sistem operasi yang sebenarnya.

Percobaan simulasi penjadwalan CPU bertujuan untuk meningkatkan pemahaman konseptual terhadap cara kerja algoritma, membandingkan kelebihan dan keterbatasannya, serta membantu dalam menentukan algoritma yang paling sesuai untuk kondisi dan kebutuhan sistem tertentu.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
```
{
  "process": "P1",
  "arrival": 0,
  "burst": 5
}
```

ArrivalTime dan BurstTime diubah ke int agar bisa dihitung.

Mengurutkan Proses (FCFS)
```
python
Copy code
processes.sort(key=lambda x: x["arrival"])
Penjelasan:
FCFS (First Come First Served) berarti:
```

Proses yang datang lebih dulu akan dieksekusi lebih dulu

List processes diurutkan berdasarkan Arrival Time terkecil → terbesar

Inisialisasi Variabel
```
python
Copy code
current_time = 0
total_waiting = 0
total_turnaround = 0
Fungsi variabel:
Variabel	Fungsi
current_time	Waktu CPU saat ini
total_waiting	Total semua waiting time
total_turnaround	Total semua turnaround time
```
Menampilkan Header Output
```
python
Copy code
print("SIMULASI CPU SCHEDULING - FCFS\n")
print("{:<8} {:<12} {:<11} {:<13} {:<16}".format(
    "Process", "Arrival", "Burst", "Waiting", "Turnaround"
))
```
Penjelasan:
Menampilkan judul simulasi

Membuat tabel rapi berisi:

Process

Arrival Time

Burst Time

Waiting Time

Turnaround Time
Proses Perhitungan FCFS
```
python
Copy code
for p in processes:
Program memproses satu per satu proses sesuai urutan kedatangan.
```
a. Sinkronisasi Waktu CPU
```
python
Copy code
if current_time < p["arrival"]:
    current_time = p["arrival"]
```
Penjelasan:
Jika CPU menganggur (belum ada proses datang)

Waktu CPU meloncat ke waktu kedatangan proses

b. Menghitung Waiting Time
```
python
Copy code
waiting_time = current_time - p["arrival"]
Waiting Time =
```
Waktu mulai eksekusi − Waktu kedatangan

c. Menghitung Turnaround Time
```
python
Copy code
turnaround_time = waiting_time + p["burst"]
Turnaround Time =
```
Waiting Time + Burst Time

d. Menyimpan Total
```
python
Copy code
total_waiting += waiting_time
total_turnaround += turnaround_time
Digunakan nanti untuk menghitung rata-rata.
```

e. Menampilkan Data Proses
```
python
Copy code
print("{:<8} {:<12} {:<11} {:<13} {:<16}".format(
    p["process"], p["arrival"], p["burst"],
    waiting_time, turnaround_time
))
Menampilkan hasil tiap proses dalam bentuk tabel.
```
f. Update Waktu CPU
```
python
Copy code
current_time += p["burst"]
CPU bergerak maju sesuai lama eksekusi proses (Burst Time).
```
Menghitung Rata-rata
```
python
Copy code
n = len(processes)
print("\nRata-rata Waiting Time     :", total_waiting / n)
print("Rata-rata Turnaround Time :", total_turnaround / n)
Penjelasan:
n = jumlah proses
```
Menghitung:

Average Waiting Time

Average Turnaround Time 

2.Bandingkan hasil simulasi dengan perhitungan manual.

1. Ringkasan Perhitungan Manual FCFS

Tabel manual:
| Proses | Arrival | Burst | Start | Finish | WT | TAT |
| ------ | ------- | ----- | ----- | ------ | -- | --- |
| P1     | 0       | 6     | 0     | 6      | 0  | 6   |
| P2     | 1       | 8     | 6     | 14     | 5  | 13  |
| P3     | 2       | 7     | 14    | 21     | 12 | 19  |
| P4     | 3       | 3     | 21    | 24     | 18 | 21  |

Rata-rata (manual)

Waiting Time (WT)

0+5+12+184/4=35/4=8,75

Turnaround Time (TAT)

6+13+19+21/4=59/4=14,75

2. Hasil Simulasi Program Python

Program melakukan langkah berikut:

Mengurutkan proses berdasarkan Arrival Time → P1, P2, P3, P4

Menghitung:

Waiting Time = current_time − arrival

Turnaround Time = waiting + burst

| Proses | Arrival | Burst | Waiting | Turnaround |
| ------ | ------- | ----- | ------- | ---------- |
| P1     | 0       | 6     | 0       | 6          |
| P2     | 1       | 8     | 5       | 13         |
| P3     | 2       | 7     | 12      | 19         |
| P4     | 3       | 3     | 18      | 21         |

Rata-rata (simulasi)

Rata-rata Waiting Time = 8.75

Rata-rata Turnaround Time = 14.75

3.Jelaskan kelebihan dan keterbatasan simulasi.

Kelebihan Simulasi FCFS

Mudah dipahami dan sederhana
Simulasi FCFS menggunakan konsep first come first served, sehingga alurnya jelas: proses yang datang lebih awal akan dieksekusi lebih dulu. Hal ini sangat cocok untuk pembelajaran dasar penjadwalan CPU.

Sesuai dengan perhitungan teoritis
Hasil simulasi terbukti sama dengan perhitungan manual, sehingga simulasi dapat dijadikan alat verifikasi atau validasi perhitungan FCFS.

Minim overhead sistem
Karena bersifat non-preemptive, tidak terjadi context switching di tengah proses. CPU menjalankan satu proses sampai selesai, sehingga overhead sistem rendah.

Implementasi program mudah dikembangkan
Struktur simulasi sederhana dan rapi, sehingga mudah dimodifikasi untuk:

Menambahkan Gantt Chart

Menghitung Start Time dan Finish Time

Dikembangkan ke algoritma lain seperti SJF, Priority, atau Round Robin

Cocok untuk analisis akademik
Simulasi ini sangat baik digunakan dalam tugas kuliah atau praktikum karena memperlihatkan hubungan langsung antara Arrival Time, Burst Time, Waiting Time, dan Turnaround Time.

Keterbatasan Simulasi FCFS

Terjadi Convoy Effect
Jika proses dengan Burst Time besar datang lebih awal, maka proses-proses kecil harus menunggu lama. Hal ini menyebabkan waktu tunggu rata-rata menjadi tinggi.

Tidak bersifat preemptive
CPU tidak dapat menghentikan proses yang sedang berjalan, meskipun ada proses lain yang lebih penting atau lebih singkat datang kemudian.

Tidak mempertimbangkan prioritas proses
Semua proses diperlakukan sama tanpa melihat tingkat kepentingan atau urgensi, sehingga tidak cocok untuk sistem real-time.

Response time buruk untuk sistem interaktif
Pengguna harus menunggu lama jika proses di depan antrean memiliki Burst Time besar, sehingga pengalaman pengguna menjadi kurang baik.

Kurang merepresentasikan sistem operasi modern
Sistem operasi modern menggunakan algoritma yang lebih kompleks dan adaptif. Simulasi FCFS ini hanya menggambarkan kondisi ideal dan sederhana, bukan kondisi nyata yang dinamis.

---

## Kesimpulan
Simulasi algoritma penjadwalan CPU menggunakan metode First Come First Served (FCFS) berhasil diimplementasikan dengan baik dan mampu menghitung waiting time serta turnaround time secara akurat berdasarkan arrival time dan burst time setiap proses.

Hasil simulasi program Python menunjukkan nilai yang sama dengan perhitungan manual, yaitu rata-rata waiting time sebesar 8,75 dan rata-rata turnaround time sebesar 14,75, sehingga dapat disimpulkan bahwa algoritma dan logika program berjalan dengan benar.

Melalui praktikum ini, diperoleh pemahaman yang lebih baik mengenai cara kerja penjadwalan CPU serta kelebihan dan keterbatasan algoritma FCFS, khususnya terkait kesederhanaan implementasi dan dampak convoy effect terhadap kinerja sistem.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?
   **Jawaban** Simulasi diperlukan untuk menguji algoritma scheduling karena dapat meniru kondisi kerja CPU tanpa harus menggunakan sistem nyata. Dengan simulasi, kinerja algoritma dapat dibandingkan secara adil, seperti waiting time dan turnaround time, serta memudahkan analisis, pembelajaran, dan mengurangi risiko kesalahan pada sistem sebenarnya.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
   **Jawaban**
Jika dataset besar, perbedaannya:
Simulasi: lebih cepat, konsisten, dan minim kesalahan karena dihitung otomatis oleh program.
Perhitungan manual: lambat, rawan salah hitung, dan sulit dilakukan karena terlalu banyak data.
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan. 
   **Jawaban:**
Algoritma FCFS (First Come First Serve) adalah yang paling mudah diimplementasikan.
Penjelasan:
FCFS hanya memproses tugas berdasarkan urutan kedatangan tanpa perhitungan tambahan atau pemilihan prioritas. Cukup mengurutkan proses berdasarkan arrival time lalu mengeksekusinya secara berurutan. Berbeda dengan algoritma lain seperti SJF atau Priority yang memerlukan perbandingan dan pengambilan keputusan lebih kompleks.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
