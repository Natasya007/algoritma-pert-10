def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:  # dibalik untuk descending
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# input jumlah data
n = int(input("masukkan jumlah data: "))
data = []

# input satu per satu
for i in range(n):
    angka = int(input(f"masukkan angka ke-{i+1}: "))
    data.append(angka)

print("data sebelum sorting:", data)

# proses
hasil = bubble_sort(data)

print("data setelah sorting:", hasil)