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
