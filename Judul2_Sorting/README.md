# Judul Program
Program Papan Skor (Leaderboard) Menggunakan Selection Sort

## Deskripsi Singkat
Program ini berfungsi untuk mencatat skor para pemain dan secara otomatis mengurutkannya untuk membuat sebuah Papan Skor (Leaderboard). Pengguna dapat memasukkan jumlah pemain dan skor masing-masing. Setelah semua data terkumpul, program akan menampilkan daftar skor yang sudah terurut secara descending.

Algoritma struktur data yang diterapkan pada program ini adalah **Selection Sort**. Algoritma ini bekerja dengan cara mencari nilai terbesar (maksimum) dari kumpulan data yang belum terurut pada setiap perulangannya, kemudian menempatkan nilai tersebut di posisi paling depan. Proses ini diulang terus-menerus hingga seluruh data tersusun rapi.

## Source Code
<img width="1542" height="1850" alt="ss ta2" src="https://github.com/user-attachments/assets/3fcdab1e-e796-4556-902e-69531ae37e65" />

**Penjelasan Logika Program :**
1. `def tukar(arr, i, j):` : Membuat fungsi bantuan untuk menukar posisi dua data di dalam array.
2. `temp = arr[i]` : Menyimpan data array indeks ke-`i` sementara di variabel `temp`.
3. `arr[i] = arr[j]` : Mengganti isi array indeks ke-`i` dengan isi array indeks ke-`j`.
4. `arr[j] = temp` : Mengisi array indeks ke-`j` dengan data awal indeks `i` yang ada di `temp`.
5. 
6. `def selection_sort_descending(arr, n):` : Membuat fungsi utama algoritma Selection Sort dengan parameter array (`arr`) dan jumlah elemen (`n`).
7. `for i in range(n - 1):` : Melakukan perulangan luar dari elemen pertama hingga sebelum elemen terakhir.
8. `pos = i` : Menetapkan indeks `i` sebagai acuan awal (sementara dianggap memiliki nilai terbesar).
9. `for j in range(i + 1, n):` : Melakukan perulangan dalam untuk membandingkan nilai acuan dengan elemen-elemen di sebelahnya.
10. `if arr[j] > arr[pos]:` : Mengecek apakah elemen ke-`j` lebih besar dari elemen acuan (`pos`). Ini kunci untuk pengurutan Descending.
11. `pos = j` : Jika ketemu nilai yang lebih besar, *update* `pos` menjadi indeks `j` tersebut.
12. `if pos != i:` : Setelah perulangan dalam selesai, cek apakah indeks nilai terbesar (`pos`) berubah dari asumsi awal (`i`).
13. `tukar(arr, i, pos)` : Jika berubah, panggil fungsi `tukar` untuk memindahkan nilai terbesar itu ke posisi depan.
14. 
15. `def main():` : Membuat fungsi utama program interaktif.
16. `print("=== Program... ===")` : Menampilkan judul program.
17. 
18. `daftar_skor = []` : Membuat list kosong untuk menampung skor.
19. `try:` : Mulai blok penanganan error untuk input jumlah pemain.
20. `jumlah = int(input(...))` : Meminta input jumlah pemain dan mengubahnya jadi angka (`int`).
21. `except ValueError:` : Menangkap error jika yang diinput adalah huruf.
22. `print("Harap masukkan angka!")` : Menampilkan pesan error.
23. `return` : Menghentikan program jika input jumlah salah.
24. 
25. `for i in range(jumlah):` : Mengulang permintaan input skor sebanyak jumlah pemain.
26. `while True:` : Perulangan agar program terus meminta input di indeks yang sama jika user salah ketik.
27. `try:` : Blok penanganan error untuk input skor.
28. `skor = int(input(...))` : Meminta input skor dan mengubahnya jadi angka.
29. `daftar_skor.append(skor)` : Memasukkan skor tersebut ke dalam list `daftar_skor`.
30. `break` : Keluar dari `while` karena input skor sukses.
31. `except ValueError:` : Menangkap error jika user memasukkan huruf pada skor.
32. `print("Input tidak valid...")` : Peringatan untuk mengetik ulang skor.
33. 
34. `print(f"\nSkor sebelum diurutkan: {daftar_skor}")` : Mencetak list skor dalam kondisi acak (sebelum disortir).
35. `selection_sort_descending(daftar_skor, jumlah)` : Memanggil fungsi *sorting* untuk mengurutkan `daftar_skor` yang berisi `jumlah` elemen.
36. `print("\n--- Leaderboard... ---")` : Menampilkan teks pembatas hasil.
37. `for i in range(jumlah):` : Perulangan untuk mencetak hasil akhir.
38. `print(f"Peringkat {i+1}: {daftar_skor[i]}")` : Mencetak skor yang sudah terurut beserta nomor peringkatnya.
39. 
40. `if __name__ == "__main__":` : Gerbang utama agar program hanya jalan jika dieksekusi langsung.
41. `main()` : Menjalankan fungsi `main()`.

## Output Program
<img width="479" height="286" alt="image" src="https://github.com/user-attachments/assets/b40e796b-a207-4212-b05c-a0b3fa5304ff" />

**Penjelasan Output:**
Gambar di atas menunjukkan bahwa program berjalan sempurna tanpa error. Saat program dijalankan, sistem meminta input jumlah skor yang ingin dicatat misalnya 4. Lalu pengguna memasukkan skor secara acak: 120, 450, 90, dan 300. Program menampilkan susunan list acak tersebut terlebih dahulu. Setelah fungsi `selection_sort_descending` dijalankan, program menampilkan "Leaderboard" di mana skor sudah otomatis terurut dari yang paling besar ke yang paling kecil.

## Link YouTube
