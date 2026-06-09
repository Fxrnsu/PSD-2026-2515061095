class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

class Slot:
    def __init__(self):
        self.key = None
        self.value = None
        self.state = SlotState.EMPTY

class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Slot() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return key % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        start_index = index

        while self.table[index].state == SlotState.OCCUPIED:
            if self.table[index].key == key:
                self.table[index].value = value
                return
            
            index = (index + 1) % self.SIZE
            if index == start_index:
                print("Kapasitas perpustakaan (Hash Table) penuh!")
                return

        self.table[index].key = key
        self.table[index].value = value
        self.table[index].state = SlotState.OCCUPIED
        print(f"Buku [{key}] '{value}' berhasil disimpan di Rak {index}.")

    def search(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index].state != SlotState.EMPTY:
            if self.table[index].state == SlotState.OCCUPIED and self.table[index].key == key:
                return self.table[index]
            index = (index + 1) % self.SIZE
            if index == start_index:
                break
        return None

    def remove_key(self, key):
        entry = self.search(key)
        if entry is None:
            return False
        entry.state = SlotState.DELETED
        return True

    def display(self):
        print("\n=== Menampilka Buku  ===")
        for i in range(self.SIZE):
            print(f"Rak {i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("KOSONG")
            elif self.table[i].state == SlotState.DELETED:
                print("DIHAPUS")
            else:
                print(f"[Kode: {self.table[i].key}] {self.table[i].value}")
        print("=============================================\n")


def main():
    print("=== Sistem Pencarian Buku Perpustakaan ===")

    perpustakaan = HashMapOpenAddressing(10)
    
    print("\n[Memuat database buku awal...]")
    perpustakaan.insert(101, "Struktur Data dengan Python")
    perpustakaan.insert(205, "Kalkulus Lanjut")
    perpustakaan.insert(301, "Pemrograman Web")
    perpustakaan.insert(111, "Jaringan Komputer") 
    
    while True:
        print("\nMenu Utama Perpustakaan:")
        print("1. Tampilkan Semua Rak Buku")
        print("2. Cari Judul Buku")
        print("3. Tambah Buku Baru")
        print("4. Hapus Buku")
        print("5. Keluar Sistem")
        
        try:
            pilihan = int(input("Pilih aksi (1-5): "))
        except ValueError:
            print("Masukkan angka!")
            continue
            
        if pilihan == 1:
            perpustakaan.display()
            
        elif pilihan == 2:
            try:
                kode_cari = int(input("Masukkan Kode Buku yang dicari: "))
                hasil = perpustakaan.search(kode_cari)
                if hasil is not None:
                    print(f"DITEMUKAN! Buku: '{hasil.value}' (Kode: {hasil.key})")
                else:
                    print("Buku tidak ditemukan di dalam sistem.")
            except ValueError:
                print("Kode buku harus berupa angka!")
                
        elif pilihan == 3:
            try:
                kode_baru = int(input("Masukkan Kode Buku (Angka): "))
                judul_baru = input("Masukkan Judul Buku: ")
                perpustakaan.insert(kode_baru, judul_baru)
            except ValueError:
                print("Kode buku harus berupa angka!")
                
        elif pilihan == 4:
            try:
                kode_hapus = int(input("Masukkan Kode Buku yang akan ditarik/dihapus: "))
                if perpustakaan.remove_key(kode_hapus):
                    print(f"Buku dengan kode {kode_hapus} berhasil dihapus  (Status: DELETED).")
                else:
                    print("Gagal menghapus! Buku tidak ditemukan.")
            except ValueError:
                print("Kode buku harus berupa angka!")
                
        elif pilihan == 5:
            print("Menutup sistem perpustakaan. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()