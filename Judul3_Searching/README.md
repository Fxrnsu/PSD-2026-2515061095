# Judul Program
Sistem Database Nomor Pin Peserta UTBK Menggunakan Binary Search

## Deskripsi Singkat
Program ini berfungsi untuk menyimpan dan mencari nomor pin peserta UTBK di dalam sebuah database. Algoritma struktur data yang diterapkan adalah Binary Search. Algoritma ini memiliki efisiensi waktu logaritmik atau O(log n). Syarat utama Binary Search adalah data harus dalam keadaan terurut terlebih dahulu. Oleh karena itu, program secara otomatis menggunakan fungsi `.sort()` pada list sebelum pencarian dimulai. Proses pencarian dilakukan dengan cara memeriksa nilai tengah array, lalu membuang setengah bagian data yang tidak mungkin berisi target secara berulang hingga data ditemukan.

## Source Code
<img width="1556" height="1850" alt="potota3" src="https://github.com/user-attachments/assets/f49f553b-c681-4d36-a82f-1093eec9702a" />

**Penjelasan Logika Program :**
1. `def binary_search(arr, n, target):` : Membuat fungsi pencarian dengan parameter *array* (`arr`), jumlah elemen (`n`), dan nomor pin yang dicari (`target`).
2. `l = 0` : Menetapkan batas kiri di indeks 0.
3. `r = n - 1` : Menetapkan batas kanan di indeks paling akhir array.
4. `pos = -1` : Menyiapkan variabel penanda posisi dengan nilai awal -1 (artinya data belum ditemukan).
6. `while l <= r:` : Melakukan perulangan selama batas kiri belum melewati batas kanan.
7. `m = l + (r - l) // 2` : Menghitung indeks tengah (median) untuk membagi porsi data pencarian.
8. `if arr[m] == target:` : Mengecek apakah nilai di posisi tengah sama persis dengan target pin.
9. `pos = m` lalu `break` : Jika sama, simpan posisinya dan hentikan perulangan pencarian secara paksa.
10. `elif arr[m] < target:` : Jika nilai tengah lebih kecil dari target, maka:
11. `l = m + 1` : Geser batas kiri ke kanan nilai tengah (fokus pencarian pindah murni ke sisi kanan).
12. `else:` dan `r = m - 1` : Jika nilai tengah lebih besar, geser batas kanan ke kiri nilai tengah (fokus pencarian pindah murni ke sisi kiri).
13. `def main():` : Fungsi utama tempat alur program berjalan.
14. `daftar_pin = [...]` : Mendeklarasikan data pin peserta secara langsung ke dalam *list* (*hardcode*) agar terisi otomatis.
15. `n = len(...)` : Menghitung total data di dalam *list* tersebut.
16. `daftar_pin.sort()` : Mengurutkan isi list secara otomatis dari yang terkecil (syarat wajib sebelum Binary Search dijalankan).
17. Blok `try-except`: Menangkap *error* jika *user* sengaja memasukkan huruf saat ditanya nomor pin yang ingin dicari.
18. `target_pin = int(input(...))` : Meminta *user* mengetikkan satu nomor pin target.
19. `indeks_ditemukan = binary_search(...)` : Memanggil algoritma pencarian dan menyimpan hasil indeksnya.
20. `if indeks_ditemukan != -1:` : Mengecek hasil kembalian. Jika bukan -1, berarti nomor pin berhasil ditemukan dan program akan mencetak indeks lokasinya. Jika -1, data tidak ada.

## Output Program
<img width="474" height="188" alt="Screenshot 2026-05-12 220144" src="https://github.com/user-attachments/assets/33b02e64-e2e1-4f64-9ffa-f9ee8be4878b" />

**Penjelasan Output:**
Program langsung menyortir *list* dan menampilkannya: `[44, 99, 294, 301, 403, 404, 405]`. Pengguna hanya diminta mengetikkan satu angka target, misalnya `405`. Algoritma *Binary Search* kemudian bekerja mengecek posisi tengah dan langsung menemukan hasil bahwa Pin 405 DITEMUKAN pada indeks ke-6.

## Link YouTube

## Tugas
<img width="3472" height="4624" alt="IMG_20260512_222502" src="https://github.com/user-attachments/assets/5b726815-fb57-4c97-abda-659f72dfabb9" />

