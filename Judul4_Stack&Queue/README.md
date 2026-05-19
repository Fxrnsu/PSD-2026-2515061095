# Judul Program
Sistem Antrean Playlist Pemutar Musik Menggunakan Queue Array

## Deskripsi Singkat
Program ini adalah simulasi sistem playlist pada aplikasi pemutar musik. Program ini berfungsi untuk mengatur daftar tunggu pemutaran lagu menggunakan struktur data Queue.

## Source Code
<img width="1418" height="4016" alt="codeta4" src="https://github.com/user-attachments/assets/c556d7b8-fa00-42ef-bda9-a251a686af7f" />

**Penjelasan Logika Program:**
1. `class QueueArray:` : Membuat (*class*) utama untuk antrean menggunakan struktur array.
2. `def __init__(self, max_size=100):` : Menginisialisasi pengaturan awal saat antrean dibuat, dengan kapasitas bawaan 100 elemen.
3. `self.MAXN = max_size` : Menyimpan batas maksimal memori ke dalam variabel `MAXN`.
4. `self.q = [None] * self.MAXN` : Membuat list kosong sejumlah kapasitas maksimal untuk menampung lagu.
5. `self.front_idx = -1` dan `self.rear_idx = -1` : Mengatur indeks depan dan belakang menjadi -1, sebagai penanda mutlak bahwa antrean masih kosong.
6. `def is_empty(self):` : Fungsi untuk mengecek apakah antrean kosong (mengembalikan nilai *True* jika `front_idx` adalah -1).
7. `def is_full(self):` : Fungsi untuk mengecek apakah memori antrean penuh.
8. `def enqueue(self, x):` : Fungsi untuk menambahkan lagu baru ke dalam antrean.
9. `if self.is_full(): return` : Jika antrean penuh, cetak peringatan dan operasi penambahan dibatalkan.
10. `if self.is_empty():` : Jika antrean tadinya kosong, indeks depan dan belakang diset ke angka 0.
11. `else: self.rear_idx = (self.rear_idx + 1) % self.MAXN` : Jika tidak kosong, indeks belakang bergeser maju 1 langkah.
12. `self.q[self.rear_idx] = x` : Memasukkan data lagu `x` ke indeks belakang yang baru.
13. `def dequeue(self):` : Fungsi untuk memutar lagu dan menghapusnya dari antrean.
14. `if self.is_empty(): return` : Jika antrean kosong, operasi langsung dibatalkan.
15. `print(...)` : Mencetak judul lagu yang ada di indeks terdepan seolah-olah sedang diputar.
16. `if self.front_idx == self.rear_idx:` : Jika indeks depan dan belakang sama, set kembali kedua indeks ke -1.
17. `else: self.front_idx = (self.front_idx + 1) % self.MAXN` : Jika bukan lagu terakhir, indeks depan bergeser maju 1 langkah, secara logis meninggalkan/menghapus data lagu lama.
18. `def peek(self):` : Fungsi untuk melihat lagu terdepan tanpa memutar atau menghapusnya.
19. `def display(self):` : Fungsi untuk mencetak seluruh isi daftar playlist ke layar.
20. Blok `while True:` di dalam `display` : Melakukan perulangan untuk menelusuri dan mencetak lagu dari indeks depan sampai menyentuh indeks belakang.
21. `def main():` : Fungsi utama tempat antarmuka program berjalan.
22. `playlist = QueueArray(20)` : Membuat objek antrean dengan kapasitas maksimal 20 lagu.
23. `playlist.enqueue(...)` : Memasukkan 5 data lagu awal secara langsung.
24. Blok `while True:` dan `try-except:` : Menampilkan menu secara berulang dan menangkal *error* jika pengguna salah memasukkan tipe data huruf saat memilih menu.
25. `if pilihan == 1: playlist.display()` : Jika menu 1 dipilih, panggil fungsi untuk menampilkan daftar antrean.
26. `elif pilihan == 2: playlist.dequeue()` : Jika menu 2 dipilih, panggil fungsi untuk memutar lagu terdepan.
27. `elif pilihan == 3: playlist.peek()` : Jika menu 3 dipilih, panggil fungsi untuk mengecek lagu giliran selanjutnya.
28. `elif pilihan == 4:` : Jika menu 4 dipilih, program akan meminta input judul lagu baru, lalu memasukannya ke dalam antrean menggunakan fungsi `playlist.enqueue(lagu_baru)`.
29. `elif pilihan == 5: break` : Jika menu 5 dipilih, hentikan perulangan `while` dan program selesai.
30. `if __name__ == "__main__": main()` : Gerbang pengecekan untuk memastikan fungsi `main()` dieksekusi hanya saat file ini dijalankan secara langsung.

## Output Program
<img width="456" height="288" alt="Screenshot 2026-05-19 093643" src="https://github.com/user-attachments/assets/910a782c-99c7-4c83-bfcd-d80486c1f660" />
<img width="328" height="52" alt="Screenshot 2026-05-19 094123" src="https://github.com/user-attachments/assets/eac7dc37-f0e7-4621-be1e-554ba8fdbcdc" />
<img width="527" height="83" alt="Screenshot 2026-05-19 094129" src="https://github.com/user-attachments/assets/a9c4e831-d195-44d6-84ea-8796a921c8ef" />

**Penjelasan Output:**
Saat program dijalankan, 5 buah lagu sudah otomatis masuk ke dalam antrean. Saat menu 1 dipilih, program berhasil menampilkan deretan lagu tersebut dari urutan pertama hingga terakhir. Ketika menu 2 dijalankan, program mengeksekusi operasi `Dequeue`, memutar lagu Hindia, lalu menggeser indeks sehingga lagu tersebut keluar dari daftar tunggu. Jika pengguna menekan menu 4 (`Enqueue`), pengguna dapat mengetikkan judul lagu baru yang secara otomatis akan ditempatkan pada urutan paling akhir dari antrean pemutaran.

## Link YouTube

