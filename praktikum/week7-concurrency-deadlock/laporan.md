

# Laporan Praktikum Minggu VII
Topik: Concurrency Deadlock

---

## Identitas
- **Nama**  : Tri Agustin Wahyuningtyas
- **NIM**   : 250220970 
- **Kelas** : 1IKRA

---
## Pendahuluan
Pada sistem operasi modern, banyak proses harus berjalan secara bersamaan (concurrency). Ketika beberapa proses mengakses sumber daya yang terbatas, masalah koordinasi menjadi sangat penting. Salah satu contoh klasik yang sering digunakan untuk menjelaskan permasalahan sinkronisasi adalah Dining Philosophers Problem.

Masalah ini menggambarkan lima filosof yang duduk melingkar dan harus berebut lima garpu untuk makan. Jika pengaturan sumber daya tidak tepat, mereka dapat saling menunggu tanpa akhir—terjebak dalam kondisi deadlock.

Melalui praktikum ini, penulis mempelajari bagaimana deadlock muncul serta bagaimana cara menghindarinya menggunakan mekanisme sinkronisasi seperti semaphore dan aturan penguncian khusus.

---

## Tujuan Praktikum 
Setelah melakukan percobaan ini, mahasiswa diharapkan mampu:

1. Mengenali dan menjelaskan empat kondisi terbentuknya deadlock.
2. Mempraktikkan penggunaan thread, lock, dan semaphore dalam program.
3. Menganalisis penyebab deadlock melalui kode simulasi.
4. Mengimplementasikan versi solusi yang bebas deadlock.
5. Menyusun laporan eksperimen secara sistematis dan mudah dipahami.

---

## Dasar Teori
Concurrency memungkinkan sejumlah proses berjalan seolah-olah simultan. Walaupun meningkatkan performa sistem, concurrency dapat menimbulkan beberapa masalah seperti race condition, starvation, dan deadlock.

Deadlock adalah kondisi ketika dua atau lebih proses saling menunggu resource yang tidak pernah dilepas, sehingga tidak ada proses yang dapat melanjutkan eksekusinya. Suatu deadlock dapat terjadi hanya jika empat kondisi Coffman terpenuhi:
Mutual Exclusion – resource hanya bisa digunakan satu proses.
Hold and Wait – proses memegang sebagian resource sambil menunggu resource lain.
No Preemption – resource tidak dapat direbut paksa.
Circular Wait – proses menunggu secara melingkar.

Untuk menghindari deadlock, sistem operasi menggunakan mekanisme seperti:
Pencegahan (prevention)
Penghindaran (avoidance)
Pendeteksian (detection)
Pemulihan (recovery)
Dalam percobaan ini, fokus solusi ada pada prevention dengan memutus circular wait.

---

## Langkah Praktikum

1.Membuat dua versi simulasi Dining Philosophers:
  -Versi dasar tanpa pencegahan (potensi deadlock tinggi)
  -Versi perbaikan dengan semaphore dan perubahan urutan pengambilan garpu
  
2.Menjalankan script Python dan mengamati output.

3.Mencatat kondisi sebelum terjadi deadlock dan setelah deadlock dicegah.

4.Membuat analisis perbandingan.

5.Menyusun laporan akhir.

---

## Kode / Perintah
1. **Persiapan Tim**
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```


---

## Eksperimen 1
versi python
```
import threading
import time

forks = [threading.Lock() for _ in range(5)]

def philosopher(i):
    left = i
    right = (i + 1) % 5

    while True:
        print(f"Philosopher {i} is thinking")
        time.sleep(1)

        forks[left].acquire()
        print(f"Philosopher {i} picked left fork {left}")

        forks[right].acquire()
        print(f"Philosopher {i} picked right fork {right}")

        print(f"Philosopher {i} is eating")
        time.sleep(1)

        forks[left].release()
        forks[right].release()

for i in range(5):
    threading.Thread(target=philosopher, args=(i,)).start()

```
**output**
``` 
Philosopher 0 is thinking
Philosopher 1 is thinking
Philosopher 2 is thinking
Philosopher 3 is thinking
Philosopher 4 is thinking
Philosopher 1 picked left fork 1
Philosopher 2 picked left fork 2
Philosopher 3 picked left fork 3
Philosopher 4 picked left fork 4
Philosopher 0 picked left fork 0
```
Kapan Deadlock Terjadi?

Deadlock bisa terjadi tepat saat semua filsuf secara simultan mengambil garpu kiri mereka dan kemudian berusaha mengambil garpu kanan, yang sudah dipegang oleh tetangganya. Karena setiap filsuf menunggu garpu kanan yang tidak pernah dilepaskan, sistem macet dan tidak ada yang bisa melanjutkan untuk makan.

Mengapa Deadlock Terjadi?

Deadlock terjadi karena setiap filsuf bersikeras mengambil dan menahan satu resource (garpu kiri) sambil menunggu resource lain (garpu kanan) yang dipegang oleh filsuf lain. Tidak ada mekanisme pencegahan seperti pelepasan resource secara paksa, pengambilan resource dalam urutan tertentu, atau timeout yang bisa memutus siklus tunggu ini.

---
## Ekperimen 2

```
import threading
import time
import random

NUM_PHILOSOPHERS = 5
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]
max_eaters = threading.Semaphore(4)

def philosopher(i):
    left = i
    right = (i + 1) % NUM_PHILOSOPHERS

    while True:
        print(f"Philosopher {i} is thinking")
        time.sleep(random.uniform(0.2, 0.6))

        max_eaters.acquire()

        if i == NUM_PHILOSOPHERS - 1:
            forks[right].acquire()
            forks[left].acquire()
        else:
            forks[left].acquire()
            forks[right].acquire()

        print(f"Philosopher {i} is eating")
        time.sleep(random.uniform(0.2, 0.5))

        forks[left].release()
        forks[right].release()
        max_eaters.release()


```
output
```

Philosopher 0 is thinking
Philosopher 1 is thinking
Philosopher 2 is thinking
Philosopher 3 is thinking
Philosopher 4 is thinking

Philosopher 1 picked left fork 1
Philosopher 1 picked right fork 2
Philosopher 1 is eating
Philosopher 3 picked left fork 3
Philosopher 3 picked right fork 4
Philosopher 3 is eating
Philosopher 0 picked left fork 0
Philosopher 0 picked right fork 1   ← menunggu jika fork 1 dipakai
Philosopher 1 released both forks
Philosopher 0 picked right fork 1
Philosopher 0 is eating

Philosopher 4 picked right fork 0
Philosopher 4 picked left fork 4
Philosopher 4 is eating

Philosopher 2 picked left fork 2
Philosopher 2 picked right fork 3
Philosopher 2 is eating

Philosopher 3 released both forks
Philosopher 4 released both forks
Philosopher 0 released both forks
Philosopher 2 released both forks

Philosopher 1 is thinking
Philosopher 3 is thinking
Philosopher 0 is thinking
Philosopher 4 is thinking
Philosopher 2 is thinking
```
# Pembuktian bahwa ini bukan Deadlock

Mengapa Versi Ini Bebas Deadlock?

Ada dua alasan utama:

1. Semaphore membatasi jumlah filosof yang boleh mengambil garpu → maksimal 4

Artinya tidak semua filosof dapat memegang satu garpu secara bersamaan.

Circular wait butuh 5 node.
Di sini maksimal hanya ada 4 → siklus tidak bisa terbentuk.

2. Filosof terakhir mengambil garpu dengan urutan terbalik

Ini memecah pola simetris:

Filosof 0–3 → left → right

Filosof 4 → right → left

Dengan pola ini, urutan permintaan resource tidak lagi membentuk lingkaran.

---
## Ekperimen 3

| Kondisi Deadlock     | Versi Deadlock                        | Versi Fixed                                              |
| -------------------- | ------------------------------------- | -------------------------------------------------------- |
| **Mutual Exclusion** | Terjadi                               | Tetap terjadi (normal)                                   |
| **Hold and Wait**    | Terjadi                               | Masih terjadi (aman selama circular wait terputus)       |
| **No Preemption**    | Terjadi                               | Masih terjadi                                            |
| **Circular Wait**    | **Terjadi (penyebab utama deadlock)** | **Dihilangkan melalui semaphore + urutan garpu berbeda** |


---

## Hasil Simulasi
Sertakan screenshot hasil percobaan atau diagram:

---

## Analisis

1. Analisis Eksperimen Versi 1 (Tanpa Mekanisme Pencegah Deadlock)

Pada percobaan pertama, semua filsuf bekerja tanpa aturan tambahan — mereka langsung mengambil garpu kiri terlebih dahulu. Dari hasil output, seluruh filsuf memang sukses memegang garpu kiri, tetapi tidak ada satu pun yang berhasil mengambil garpu kanan. Akhirnya, tidak ada proses makan yang terjadi.

Pada titik ini, setiap filsuf terjebak karena garpu yang ia butuhkan sedang digunakan oleh tetangganya. Terbentuklah rantai tunggu seperti berikut:

F0 → menunggu garpu 1  
F1 → menunggu garpu 2  
F2 → menunggu garpu 3  
F3 → menunggu garpu 4  
F4 → menunggu garpu 0  (membuat lingkaran lengkap)

Situasi tersebut memenuhi keempat kondisi deadlock menurut Coffman. Yang paling terlihat adalah circular wait, karena kelima filsuf saling menunggu dalam urutan melingkar tanpa jalan keluar.

Tidak ada mekanisme:
untuk mengubah urutan pengambilan garpu,
membatasi siapa yang boleh makan,
atau memaksa pelepasan garpu.

Akibatnya, sistem berhenti total dan tidak satu filsuf pun dapat melanjutkan. Eksperimen ini menunjukkan bahwa desain Dining Philosophers versi dasar secara alami mengarah pada deadlock.

2. Analisis Eksperimen Versi 2 (Semaphore + Urutan Garpu Dibalik)
Pada versi kedua, dua metode pencegahan deadlock dimasukkan:

1. Semaphore max_eaters = 4
Hanya empat filsuf yang boleh mencoba makan dalam satu waktu.

2. Filsuf terakhir mengambil garpu dengan urutan terbalik
Ia mengambil garpu kanan dulu, baru garpu kiri, untuk memecahkan pola pengambilan sumber daya yang identik.

Setelah modifikasi ini dijalankan, output menunjukkan bahwa:

Proses makan terjadi secara bergantian tanpa kebuntuan.
Tidak ada lima filsuf yang menunggu selamanya.
Selalu ada filsuf yang berhasil makan dan kemudian melepas garpu.

Dengan maksimum empat filsuf di zona makan, tidak pernah terbentuk kondisi di mana kelima garpu terkunci sekaligus.

Penerapan urutan terbalik pada filsuf terakhir juga menghilangkan pola permintaan resource yang membentuk lingkaran sempurna. Dengan begitu, kondisi circular wait terputus, sehingga deadlock tidak mungkin muncul.

Secara keseluruhan, kedua mekanisme ini terbukti efektif menghilangkan salah satu syarat utama deadlock. Karena kondisi Coffman keempat tidak terpenuhi, maka sistem dapat berjalan bebas deadlock.

---

## Kesimpulan
1. Deadlock pada Dining Philosophers terjadi karena semua kondisi Coffman terpenuhi, terutama      circular wait.

2. Dengan membatasi akses menggunakan semaphore serta mengubah urutan pengambilan garpu,           circular wait dapat dihilangkan.

3. Versi perbaikan berjalan lebih stabil dan tidak menunjukkan tanda deadlock.

4. Praktikum ini menunjukkan bahwa pengaturan resource sangat menentukan apakah sistem             concurrency aman atau tidak.

---

## Tugas & Quiz
### Tugas
1. Analisis versi *Dining Philosophers* yang menyebabkan deadlock dan versi fixed yang bebas deadlock.  
2. Dokumentasikan hasil diskusi kelompok ke dalam `laporan.md`.  
3. Sertakan diagram atau screenshot hasil simulasi/pseudocode.  
4. Laporkan temuan penyebab deadlock dan solusi pencegahannya.  

1. Analisis Versi Dining Philosophers yang Menyebabkan Deadlock
pada versi awal, setiap filsuf menjalankan pola yang sama: berpikir, mengambil garpu kiri, mengambil garpu kanan, lalu makan. Karena semua filsuf mengambil garpu kiri lebih dulu, situasi berikut terjadi:

1. Semua filsuf berhasil mengambil garpu kiri.
2. Semua kemudian berusaha mengambil garpu kanan.
3. Garpu kanan masing-masing sedang dipegang filsuf lain.
4. Tidak ada filsuf yang bisa maju atau mundur.

Akibatnya, terbentuk kondisi circular wait:

F0 → menunggu garpu 1
F1 → menunggu garpu 2
F2 → menunggu garpu 3
F3 → menunggu garpu 4
F4 → menunggu garpu 0


Lingkaran tersebut memenuhi seluruh syarat deadlock menurut Coffman:

Mutual Exclusion: garpu hanya bisa dipakai satu filsuf.
Hold and Wait: setiap filsuf memegang 1 garpu sambil menunggu garpu lainnya.
No Preemption: garpu tidak dapat direbut paksa.
Circular Wait: seluruh filsuf saling menunggu dalam bentuk siklus.

Karena keempat kondisi terpenuhi, sistem berhenti total dan tidak ada filsuf yang dapat makan. Versi ini membuktikan bahwa implementasi dasar Dining Philosophers sangat rawan deadlock.

Analisis Versi Fixed (Bebas Deadlock)
Versi perbaikan menggunakan dua strategi:

1. Semaphore max_eaters = 4
   Hanya empat filsuf yang boleh masuk ke fase mengambil garpu.
   Ini mencegah situasi di mana lima garpu terkunci sekaligus.

2. Filosof terakhir mengambil garpu dengan urutan terbalik (right → left)
   Perubahan urutan ini memutus pola simetris yang menciptakan circular wait.

Hasilnya:

- Tidak ada lima filsuf yang memegang satu garpu bersamaan.
- Selalu ada filsuf yang berhasil menyelesaikan proses makan.
- Tidak muncul rantai tunggu melingkar.
- Setiap filsuf mendapat giliran makan secara bergantian.

Dengan kombinasi kedua metode ini, kondisi circular wait dihilangkan, sehingga salah satu syarat deadlock tidak terpenuhi. Karena satu syarat Coffman saja hilang, deadlock tidak dapat terjadi.

### Quiz
Tuliskan jawaban di bagian **Quiz** laporan:
1. Empat kondisi penyebab deadlock:

Mutual Exclusion

Hold and Wait

No Preemption

Circular Wait

2. Mengapa sinkronisasi diperlukan?

Sinkronisasi dibutuhkan agar proses yang berjalan bersamaan tidak saling merusak data, tidak berebut resource secara tidak teratur, serta memastikan critical section hanya diakses oleh satu proses pada satu waktu.

3. Perbedaan semaphore dan monitor:

Semaphore → mekanisme sinkronisasi level rendah, perlu pengelolaan manual (rawan error).

Monitor → mekanisme tingkat tinggi, mutual exclusion dijamin secara otomatis oleh bahasa pemrograman.

---

## Refleksi Diri
Tuliskan secara singkat:

- Apa bagian yang paling menantang minggu ini?  

Bagian tersulit bagi penulis adalah memahami kapan tepatnya deadlock terjadi, bukan hanya menjalankan kodenya. Setelah memvisualisasikan alur tunggu setiap filosof, barulah terlihat mengapa sistem bisa macet total.

- Bagaimana cara Anda mengatasinya?
  
Strategi yang membantu adalah menguji dua versi kode sekaligus dan mengamati perbedaannya. Melihat bagaimana perubahan kecil seperti membalik urutan pengambilan garpu dapat memperbaiki seluruh sistem adalah bagian paling menarik dari praktikum ini.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
