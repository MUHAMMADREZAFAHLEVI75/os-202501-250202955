
# Laporan Praktikum Minggu [13]
Topik: Docker – Resource Limit (CPU & Memori)


---

## Identitas
- **Nama**  : muhammad reza fahlevi 
- **NIM**   : 250202955
- **Kelas** : 1 IKRA

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori
1. **Docker Container** adalah virtual mesin yang ringan yang bisa untuk menjalankan aplikasi secara di background, dengan berbagi kernel sistem operasi host 
2. **Resource Limit** adalah untuk membatasi penggunaan CPU dan Memori container agar tidak menggangu container lain.
3. 'docker stats' di gunakan untuk melihat **Monitoring resource** doker
4. Doker memmakai control grup di linux buat mengatur dan batasi sumber daya CPU dan memori

## Langkah Praktikum
1. Memastikan Docker telah terinstal dan berjalan dengan baik pada sistem.
2. Membuat program uji sederhana berbasis Python untuk menguji penggunaan CPU dan memori.
3. Menulis Dockerfile untuk menjalankan program uji tersebut di dalam container.
4. Melakukan build image Docker menggunakan Dockerfile.
5. Menjalankan container tanpa pembatasan resource.
6. Menjalankan container dengan pembatasan CPU dan memori.
7. Mengamati perbedaan hasil eksekusi serta penggunaan resource.
8. Melakukan commit dan push hasil praktikum ke repository GitHub.

---
Strukture folder
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


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
import time

print("=== CPU STRESS TEST DIMULAI ===")
start_time = time.time()

count = 0
while time.time() - start_time < 20:
    count += 1

print("CPU Stress Test selesai")
print(f"Total loop: {count}")

print("\n=== MEMORY STRESS TEST DIMULAI ===")

memory = []
try:
    for i in range(50): 
        memory.append(bytearray(10 * 1024 * 1024))
        print(f"Memory terpakai: {(i+1)*10} MB")
        time.sleep(1)
except MemoryError:
    print("Memory limit tercapai!")

print("Memory Stress Test selesai")


print("\nContainer aktif untuk monitoring (Ctrl+C untuk keluar)")
while True:
    time.sleep(1)

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

-Makna Hasil Percobaan
Berdasarkan pengujian yang telah dilakukan menggunakan program CPU & Memory Stress Test di dalam Docker container, diperoleh hasil sebagai berikut:
Tanpa resource limit
Penggunaan CPU dapat mencapai 100% atau lebih (multi-core).
Penggunaan memori terus meningkat seiring proses alokasi memori hingga mendekati kapasitas RAM host.
Container berjalan lebih cepat karena tidak ada pembatasan sumber daya.
Dengan resource limit (CPU & Memori)
Penggunaan CPU dibatasi sesuai parameter --cpus, sehingga container tidak bisa menggunakan seluruh core.
Penggunaan memori berhenti pada batas yang ditentukan (misalnya 500 MB).
Saat memori mencapai limit, proses akan:
Mengalami MemoryError, atau
Dihentikan otomatis oleh sistem (OOM Killer).
Performa aplikasi menjadi lebih lambat dibandingkan kondisi tanpa limit.
Perbedaan ini dapat diamati secara langsung menggunakan perintah:
docker stats
yang menampilkan pemakaian CPU dan memori secara real-time.

-Hubungan Hasil dengan Teori Sistem Operasi
a. Peran Kernel Linux
Docker berjalan langsung di atas kernel Linux, bukan menggunakan kernel sendiri. Kernel bertanggung jawab dalam:
Manajemen CPU
Manajemen memori
Penjadwalan proses
Isolasi container
Pembatasan resource pada Docker dilakukan oleh kernel menggunakan fitur cgroups (Control Groups).

b. Control Groups (cgroups)
CPU cgroups
Mengatur seberapa banyak waktu CPU yang boleh digunakan oleh container.
Memory cgroups
Membatasi jumlah maksimum memori yang dapat digunakan container.
Ketika container melebihi batas:
Kernel akan menolak alokasi memori tambahan
Kernel dapat mematikan proses container (OOM Killer)

c. System Call
Aplikasi Python di dalam container melakukan:
malloc() → permintaan memori
sched_yield() → penjadwalan CPU
sleep() → idle state
System call ini diteruskan ke kernel host, bukan kernel terpisah, sehingga pembatasan tetap berlaku walaupun aplikasi berjalan di container.

d. Arsitektur OS
Docker menerapkan:
Process-level virtualization
Bukan virtualisasi penuh seperti Virtual Machine
Lebih ringan, tetapi sangat bergantung pada kernel host

-Perbedaan Hasil di Lingkungan OS (Linux vs Windows)
| Aspek          | Linux                       | Windows                        |
| -------------- | --------------------------- | ------------------------------ |
| Kernel         | Native Linux Kernel         | Windows Kernel                 |
| Docker         | Berjalan langsung di kernel | Berjalan melalui **WSL2 / VM** |
| Resource Limit | Akurat & real-time          | Bergantung konfigurasi WSL     |
| Performa       | Lebih stabil & cepat        | Sedikit lebih lambat           |
| Monitoring     | `docker stats` langsung     | Melalui VM                     |
| OOM Handling   | Kernel Linux                | VM Linux (WSL2)                |
Penjelasan:
Di Linux, Docker menggunakan kernel secara langsung sehingga pembatasan CPU dan memori sangat presisi.
Di Windows, Docker Desktop menjalankan Linux kernel di atas WSL2, sehingga:
Resource limit masih berlaku
Tetapi dipengaruhi konfigurasi VM dan Windows scheduler


---

## Kesimpulan
Docker container dapat dijalankan dengan pembatasan CPU dan memori untuk mencegah penggunaan sumber daya sistem secara berlebihan dan menjaga kestabilan sistem host maupun container lain.
Pembatasan resource pada Docker memanfaatkan fitur kernel Linux seperti control groups (cgroups), sehingga penggunaan CPU dan memori container dapat dikontrol dan dimonitor secara real-time menggunakan perintah docker stats.
Hasil percobaan menunjukkan bahwa container dengan resource limit memiliki performa yang lebih terkontrol namun lebih lambat dibandingkan container tanpa limit, sehingga pembatasan resource sangat penting untuk lingkungan multi-container dan sistem produksi.

---
## Tugas & Quiz
### Tugas
1. Buat Dockerfile sederhana dan program uji di folder `code/`.
2. Build image dan jalankan container **tanpa limit**.
3. Jalankan container dengan limit **CPU** dan **memori**.
4. Sajikan hasil pengamatan dalam tabel/uraian singkat di `laporan.md`.

### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Mengapa container perlu dibatasi CPU dan memori?
**Jawaban:** Container perlu dibatasi CPU dan memori agar tidak menghabiskan seluruh sumber daya sistem host. Tanpa pembatasan, satu container dapat menggunakan CPU dan RAM secara berlebihan sehingga menyebabkan penurunan performa container lain atau bahkan membuat sistem menjadi tidak stabil. Pembatasan resource membantu menjaga kestabilan, keadilan pembagian sumber daya, dan keamanan sistem.
2. Apa perbedaan VM dan container dalam konteks isolasi resource?
**Jawaban:** Virtual Machine (VM) memiliki isolasi resource yang lebih kuat karena setiap VM memiliki sistem operasi dan kernel sendiri, sehingga CPU dan memori benar-benar terpisah dari VM lain.
Container berbagi kernel host, sehingga isolasi resource dilakukan menggunakan mekanisme kernel seperti cgroups dan namespace.
Akibatnya, VM lebih berat namun isolasinya kuat, sedangkan container lebih ringan dan efisien tetapi isolasi resource bergantung pada konfigurasi host.
3. Apa dampak limit memori terhadap aplikasi yang boros memori?
**Jawaban:** Jika aplikasi boros memori dijalankan dengan limit memori, maka ketika penggunaan memori mencapai batas:
- Aplikasi dapat mengalami MemoryError
- Proses dapat dihentikan oleh OOM Killer
- Performa aplikasi menurun atau aplikasi berhenti berjalan
Hal ini memaksa pengembang untuk membuat aplikasi yang lebih efisien dalam penggunaan memori dan mencegah kerusakan pada sistem host.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
