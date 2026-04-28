# Judul Program
Program Sederhana Pencatat Nilai Mahasiswa

## Deskripsi Singkat
Program ini dibuat untuk mendata nilai mahasiswa. Pengguna bebas menentukan jumlah data, lalu menginput nilainya secara manual. Hasil akhirnya berupa rekapitulasi nilai yang disusun rapi berdasarkan urutan input.

Data disimpan menggunakan List 1 Dimensi karena kemampuannya dalam mengelola urutan data secara dinamis. Dengan struktur ini, nilai-nilai yang sejenis bisa dikelompokkan dengan mudah. Penambahan datanya sendiri menggunakan perintah append(), sedangkan untuk proses pemanggilan datanya dilakukan melalui mekanisme indeks.
  
## Source Code
<img width="1418" height="1394" alt="code_judul1" src="https://github.com/user-attachments/assets/a16e6eab-e93b-4bfe-a8f0-7dd239c4a8c3" />

## Penjelasan Logika Program:
**Penjelasan Logika Program (Per Baris):**
1. `def main():` : Mendefinisikan fungsi utama program dengan nama `main()`.
2. `print("=== Program Sederhana Pencatat Nilai ===")` : Mencetak judul program ke layar.
3. 
4. `daftar_nilai = []` : Membuat sebuah variabel `daftar_nilai` yang diinisialisasi sebagai List 1 Dimensi kosong untuk menyimpan data-data nilai nantinya.
5. 
6. `try:` : Memulai blok penanganan error (exception handling) untuk mencegah program berhenti *crash* jika pengguna memasukkan huruf saat diminta angka.
7. `jumlah = int(input("Masukkan jumlah nilai yang ingin diinput "))` : Meminta input dari pengguna, lalu secara paksa mengubah input tersebut menjadi tipe data integer dan menyimpannya di variabel `jumlah`.
8. `except ValueError:` : Menangkap error spesifik bertipe `ValueError`, yang muncul jika kode di baris sebelumnya gagal mengubah input huruf menjadi angka.
9. `print("Harap masukkan angka!")` : Menampilkan pesan peringatan kepada pengguna karena input yang dimasukkan salah.
10. `return` : Menghentikan fungsi `main()` secara langsung dan keluar dari program karena terjadi error di pengaturan awal.
11. 
12. `for i in range(jumlah):` : Melakukan perulangan `for` mulai dari indeks 0 hingga batas variabel `jumlah` yang sudah diinputkan pengguna.
13. `while True:` : Memulai perulangan tak terbatas yang bertugas untuk terus-menerus meminta input pada indeks yang sama sampai pengguna memasukkan angka yang benar.
14. `try:` : Memulai blok penanganan error khusus untuk proses input nilai tiap mahasiswanya.
15. `nilai = int(input(f"Masukkan nilai ke-{i+1}: "))` : Meminta input nilai, mengubahnya ke integer, lalu menyimpannya di variabel `nilai`. Variabel `i` ditambah 1 agar tampilan urutan di layar mulai dari "ke-1", bukan "ke-0".
16. `daftar_nilai.append(nilai)` : Menggunakan metode `append()` untuk menyisipkan data `nilai` tersebut ke posisi ruang paling akhir di dalam List `daftar_nilai`.
17. `break` : Perintah untuk keluar secara paksa dari perulangan `while True` karena input sudah valid (berhasil melewati baris `append`).
18. `except ValueError:` : Menangkap error jika input yang dimasukkan ke variabel `nilai` bukan sebuah angka.
19. `print("Input tidak valid, silakan masukkan angka!")` : Menampilkan pesan error kepada pengguna agar mengulang input di urutan yang sama.
20. 
21. `print("\n--- Rekap Nilai Mahasiswa ---")` : Mencetak judul bagian output/rekap dengan memberikan enter `\n` di awal.
22. `if len(daftar_nilai) == 0:` : Memeriksa kondisi apakah panjang/jumlah elemen list `daftar_nilai` sama dengan 0 (kosong).
23. `print("Belum ada nilai yang dicatat.")` : Jika kondisi di atas benar, maka cetak pesan ini.
24. `else:` : Jika list tidak kosong (memiliki minimal 1 elemen), maka program akan mengeksekusi blok kode di bawah ini.
25. `for i in range(len(daftar_nilai)):` : Melakukan perulangan `for` sepanjang jumlah total elemen yang ada di dalam List `daftar_nilai`.
26. `print(f"Data indeks ke-[{i}]: {daftar_nilai[i]}")` : Mencetak nomor indeks `i` ke layar, diikuti dengan nilai elemen yang berada pada indeks tersebut menggunakan cara akses elemen `daftar_nilai[i]`.
27. 
28. `if __name__ == "__main__":` : Kondisi untuk memeriksa apakah file program Python ini dijalankan secara langsung.
29. `main()` : Memanggil dan mengeksekusi fungsi `main()` yang sudah dibuat di baris 1 untuk menjalankan seluruh alur program.

## Output Program
<img width="510" height="355" alt="Screenshot 2026-04-28 184645" src="https://github.com/user-attachments/assets/3048adb7-7f3d-4709-a8e2-374411750640" />

## Penjelasan Output:
Gambar di atas membuktikan bahwa program berjalan tanpa error. Awalnya, program meminta jumlah nilai yang ingin diinput (misalnya 5). Kemudian, program meminta input nilai sebanyak 5 kali (misalnya 80, 90, 75, 85, 80). Setelah semua data dimasukkan, program langsung menampilkan "Rekap Nilai Mahasiswa" dengan mencetak indeks List beserta isi datanya (contoh: Data indeks ke-[0]: 80, Data indeks ke-[1]: 90, dst). Program juga kebal terhadap error tipe data, jika kita memasukkan huruf saat diminta angka, program akan meminta input ulang berkat penanganan error (`try-except`).

## Link YouTube
https://youtu.be/WeyOzxU6asU
