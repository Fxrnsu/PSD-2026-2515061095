def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1
    
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            l = m + 1 
        else:
            r = m - 1 
    return pos

def main():
    print("=== Sistem Database Nomor Pin Peserta UTBK ===")
    
    daftar_pin = [44, 404, 301, 405, 99, 294, 403]
    n = len(daftar_pin)
    
    daftar_pin.sort()
    
    print(f"Data Pin Peserta yang terdaftar (Terurut): \n{daftar_pin}\n")
    try:
        target_pin = int(input("Masukkan Nomor Pin peserta yang ingin dicari: "))
    except ValueError:
        print("Input tidak valid, silakan jalankan ulang dan masukkan angka!")
        return
            
    indeks_ditemukan = binary_search(daftar_pin, n, target_pin)
    
    print("\n--- Hasil Pencarian ---")
    if indeks_ditemukan != -1:
        print(f"✅ Pin {target_pin} DITEMUKAN pada indeks ke-{indeks_ditemukan}.")
    else:
        print(f"❌ Pin {target_pin} TIDAK DITEMUKAN.")

if __name__ == "__main__":
    main()