def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selection_sort_descending(arr, n):
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if arr[j] > arr[pos]: 
                pos = j
        if pos != i:
            tukar(arr, i, pos)

def main():
    print("=== Program Papan Skor (Leaderboard) ===")
    
    daftar_skor = []
    try:
        jumlah = int(input("Berapa banyak pemain yang ingin dicatat skornya? "))
    except ValueError:
        print("Harap masukkan angka!")
        return

    for i in range(jumlah):
        while True:
            try:
                skor = int(input(f"Masukkan skor pemain ke-{i+1}: "))
                daftar_skor.append(skor)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")

    print(f"\nSkor sebelum diurutkan: {daftar_skor}")
    selection_sort_descending(daftar_skor, jumlah)
    print("\n--- Leaderboard (Peringkat Tertinggi ke Terendah) ---")
    for i in range(jumlah):
        print(f"Peringkat {i+1}: {daftar_skor[i]}")

if __name__ == "__main__":
    main()