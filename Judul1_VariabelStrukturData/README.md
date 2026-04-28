# Judul Program
Program Sederhana Pencatat Nilai Mahasiswa

## Deskripsi Singkat
Program ini dibuat untuk mendata nilai mahasiswa. Pengguna bebas menentukan jumlah data, lalu menginput nilainya secara manual. Hasil akhirnya berupa rekapitulasi nilai yang disusun rapi berdasarkan urutan input.

Data disimpan menggunakan List 1 Dimensi karena kemampuannya dalam mengelola urutan data secara dinamis. Dengan struktur ini, nilai-nilai yang sejenis bisa dikelompokkan dengan mudah. Penambahan datanya sendiri menggunakan perintah append(), sedangkan untuk proses pemanggilan datanya dilakukan melalui mekanisme indeks.
  
## Source Code
<img width="1418" height="1394" alt="code_judul1" src="https://github.com/user-attachments/assets/a16e6eab-e93b-4bfe-a8f0-7dd239c4a8c3" />

## Penjelasan Logika Program:
1. `def main():`: Mendefinisikan fungsi utama program.
2. `daftar_nilai = []`: Menginisialisasi sebuah List 1 Dimensi kosong bernama `daftar_nilai` untuk menampung data yang akan diinput.
3. `try...except`: Blok ini digunakan untuk menangani error jika pengguna memasukkan selain angka saat ditanya jumlah nilai yang ingin dicatat.
4. `jumlah = int(input(...))`: Meminta pengguna memasukkan jumlah data dan mengubahnya menjadi tipe data integer.
5. `for i in range(jumlah):`: Memulai perulangan sebanyak `jumlah` yang diinputkan pengguna untuk meminta data nilai.
6. `while True:`: Perulangan tak terbatas (infinite loop) yang memastikan pengguna memasukkan tipe data angka yang benar untuk setiap nilai.
7. `nilai = int(input(...))`: Meminta input nilai dari pengguna.
8. `daftar_nilai.append(nilai)`: Jika input valid (angka), fungsi `append()` dipanggil untuk memasukkan nilai tersebut ke posisi paling akhir dari List `daftar_nilai`.
9. `break`: Keluar dari blok `while True` jika input valid, lalu lanjut ke perulangan `for` berikutnya.
10. `if len(daftar_nilai) == 0:`: Mengecek apakah List kosong menggunakan fungsi `len()`.
11. `for i in range(len(daftar_nilai)):`: Jika List ada isinya, program melakukan perulangan sepanjang jumlah elemen di dalam List.
12. `print(...)`: Mencetak data ke layar dengan mengakses isi List menggunakan indeksnya, yaitu `daftar_nilai[i]`.

## Output Program
<img width="510" height="355" alt="Screenshot 2026-04-28 184645" src="https://github.com/user-attachments/assets/3048adb7-7f3d-4709-a8e2-374411750640" />

## Penjelasan Output:
Gambar di atas membuktikan bahwa program berjalan tanpa error. Awalnya, program meminta jumlah nilai yang ingin diinput (misalnya 5). Kemudian, program meminta input nilai sebanyak 5 kali (misalnya 80, 90, 75, 85, 80). Setelah semua data dimasukkan, program langsung menampilkan "Rekap Nilai Mahasiswa" dengan mencetak indeks List beserta isi datanya (contoh: Data indeks ke-[0]: 80, Data indeks ke-[1]: 90, dst). Program juga kebal terhadap error tipe data, jika kita memasukkan huruf saat diminta angka, program akan meminta input ulang berkat penanganan error (`try-except`).

## Link YouTube

