class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Antrean lagu penuh!")
            return
        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN
        self.q[self.rear_idx] = x
        print(f"Berhasil menambahkan '{x}' ke dalam antrean.")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kosong, tidak ada lagu yang diputar.")
            return
        print(f"Sedang memutar: '{self.q[self.front_idx]}'")
        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Antrean kosong.")
            return
        print(f"Lagu selanjutnya: '{self.q[self.front_idx]}'")

    def display(self):
        if self.is_empty():
            print("Antrean playlist kosong.")
            return
        print("\n=== Daftar Antrean Lagu (Dari atas ke bawah) ===")
        i = self.front_idx
        nomor = 1
        while True:
            print(f"{nomor}. {self.q[i]}")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
            nomor += 1
        print("================================================\n")


def main():
    print("=== Sistem Antrean Playlist Pemutar Musik ===")
    playlist = QueueArray(20) 
    playlist.enqueue("Hindia - Evaluasi")
    playlist.enqueue("Bernadya - Satu Bulan")
    playlist.enqueue("Pamungkas - To the Bone")
    playlist.enqueue("Tulus - Hati-Hati di Jalan")
    playlist.enqueue("Nadin Amizah - Rayuan Perempuan Gila")
    
    while True:
        print("\nMenu Playlist:")
        print("1. Lihat Daftar Antrean")
        print("2. Putar Lagu Selanjutnya")
        print("3. Cek Lagu Giliran Berikutnya")
        print("4. Tambah Lagu Baru")
        print("5. Tutup Pemutar Musik")
        
        try:
            pilihan = int(input("Pilih (1-5): "))
        except ValueError:
            print("Harap masukkan angka!")
            continue
            
        if pilihan == 1:
            playlist.display()
        elif pilihan == 2:
            playlist.dequeue()
        elif pilihan == 3:
            playlist.peek()
        elif pilihan == 4:
            lagu_baru = input("Masukkan 'Nama Penyanyi - Judul Lagu': ")
            playlist.enqueue(lagu_baru)
        elif pilihan == 5:
            print("Mematikan pemutar musik.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()