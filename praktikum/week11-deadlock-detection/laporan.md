# Laporan Praktikum Minggu 11

Topik: Simulasi dan Deteksi Deadlock

---

## Identitas

* **Nama**  : Muhammad Reza Fahlevi
* **NIM**   : 250202955
* **Kelas** : 1IKRA

---

## A. Pendahuluan

Deadlock merupakan kondisi pada sistem operasi di mana dua atau lebih proses saling menunggu sumber daya yang sedang dipegang oleh proses lain, sehingga tidak ada satu pun proses yang dapat melanjutkan eksekusinya. Pada praktikum ini dilakukan simulasi dan **deteksi deadlock**, yaitu pendekatan yang membiarkan deadlock terjadi lalu mendeteksinya menggunakan algoritma tertentu.

---

## B. Tujuan Praktikum

1. Mengimplementasikan algoritma deteksi deadlock.
2. Menjalankan simulasi menggunakan dataset uji.
3. Menentukan proses yang terlibat deadlock.
4. Menganalisis hasil deteksi berdasarkan teori deadlock.

---

## C. Dataset Uji

Dataset disimpan dalam file `dataset_deadlock.csv` dengan format berikut:

| Proses | Allocation | Request |
| ------ | ---------- | ------- |
| P1     | R1         | R2      |
| P2     | R2         | R3      |
| P3     | R3         | R1      |

Dataset ini membentuk *circular wait* antar proses.

---

## D. Algoritma Deteksi Deadlock

Pendekatan yang digunakan adalah **Resource Allocation Graph (RAG)**.

### Langkah Algoritma:

1. Membaca data proses, resource allocation, dan request.
2. Membentuk graf ketergantungan proses.
3. Mendeteksi adanya siklus (*cycle*) pada graf.
4. Jika terdapat siklus, maka proses dalam siklus tersebut berada dalam kondisi deadlock.

---

## E. Implementasi Program

Bahasa pemrograman yang digunakan adalah **Python**.

```python
# deadlock_detection.py
import csv
from collections import defaultdict

# Membaca dataset
allocation = {}
request = {}
processes = []

with open('dataset_deadlock.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        p = row['Proses']
        processes.append(p)
        allocation[p] = row['Allocation']
        request[p] = row['Request']

# Membentuk graph ketergantungan proses
graph = defaultdict(list)

for p1 in processes:
    for p2 in processes:
        if allocation[p1] == request[p2]:
            graph[p2].append(p1)

# Deteksi cycle dengan DFS
visited = set()
rec_stack = set()
deadlocked = set()

def dfs(p):
    visited.add(p)
    rec_stack.add(p)

    for neighbor in graph[p]:
        if neighbor not in visited:
            dfs(neighbor)
        elif neighbor in rec_stack:
            deadlocked.update(rec_stack)

    rec_stack.remove(p)

for p in processes:
    if p not in visited:
        dfs(p)

# Output hasil
print("Hasil Deteksi Deadlock:")
if deadlocked:
    print("Deadlock terdeteksi pada proses:", ', '.join(deadlocked))
else:
    print("Tidak terjadi deadlock")
```

---

## F. Hasil Eksekusi

hasil screenshot eksekusi:
<img width="1918" height="1018" alt="12121" src="https://github.com/user-attachments/assets/23437408-ed71-4b5a-b278-aa63b91d0387" />


Berdasarkan hasil eksekusi program:

| Proses | Status   |
| ------ | -------- |
| P1     | Deadlock |
| P2     | Deadlock |
| P3     | Deadlock |

Semua proses terlibat dalam kondisi deadlock.

---

## G. Analisis

Deadlock terjadi karena keempat kondisi deadlock terpenuhi:

1. **Mutual Exclusion** – Resource hanya dapat digunakan satu proses.
2. **Hold and Wait** – Proses memegang satu resource sambil menunggu resource lain.
3. **No Preemption** – Resource tidak dapat diambil paksa.
4. **Circular Wait** – Terjadi siklus P1 → P2 → P3 → P1.

---

## H. Quiz

### 1. Perbedaan deadlock prevention, avoidance, dan detection

* **Prevention**: Mencegah deadlock dengan menghilangkan salah satu dari empat kondisi deadlock.
* **Avoidance**: Menghindari deadlock dengan memastikan sistem selalu berada dalam *safe state*.
* **Detection**: Membiarkan deadlock terjadi lalu mendeteksinya menggunakan algoritma.

### 2. Mengapa deteksi deadlock tetap diperlukan?

Karena pencegahan dan penghindaran deadlock tidak selalu efisien atau memungkinkan, terutama pada sistem kompleks dan dinamis.

### 3. Kelebihan dan kekurangan deteksi deadlock

**Kelebihan:**

* Lebih fleksibel.
* Tidak membatasi alokasi resource secara ketat.

**Kekurangan:**

* Deadlock sudah terlanjur terjadi.
* Membutuhkan mekanisme recovery tambahan.

---

## I. Kesimpulan

Program simulasi berhasil mendeteksi deadlock menggunakan pendekatan graf dan pendeteksian siklus. Dataset uji menunjukkan kondisi deadlock yang valid sesuai teori sistem operasi.

---

## Referensi

1. Silberschatz et al., *Operating System Concepts*, 10th Edition
2. Tanenbaum, *Modern Operating Systems*, 4th Edition
3. OSTEP – Deadlock Detection
