# Sistem Pencarian Buku Perpustakaan 

## Deskripsi Singkat
Program ini adalah sistem manajemen pencarian buku perpustakaan menggunakan struktur data Hash Map. Sistem menggunakan kode buku sebagai Key dan judul buku sebagai Value untuk memungkinkan pencarian data dengan kompleksitas waktu O(1).

## Source Code
<img width="1924" height="5422" alt="ta6kode" src="https://github.com/user-attachments/assets/e5d18a5d-eff4-49ac-a129-ba931bd9e959" />

**Penjelasan Logika Program:**
* **Class SlotState & Slot:** Mendefinisikan struktur *node* dalam *array*. Setiap slot menyimpan kode buku (`key`), judul buku (`value`), dan status ketersediaan slot (`EMPTY`, `OCCUPIED`, atau `DELETED`).
* **Inisialisasi HashMap:** Membuat tabel *hash* (array) dengan kapasitas awal 10 slot kosong.
* **Fungsi `hash_function`:** Menghitung indeks array menggunakan operasi modulus (`key % ukuran_tabel`).
* **Fungsi `insert`:** Memasukkan data baru ke dalam tabel. Jika indeks hasil *hash* sudah terisi, algoritma *Linear Probing* akan menggeser pencarian ke indeks selanjutnya (`index + 1`) hingga menemukan slot berstatus `EMPTY` atau `DELETED`.
* **Fungsi `search`:** Mencari data berdasarkan *key*. Pencarian dimulai dari indeks hasil *hash* dan akan terus berlanjut hingga data ditemukan atau bertemu dengan slot `EMPTY`.
* **Fungsi `remove_key`:** Menghapus data buku secara logis dengan mengubah status slot menjadi `DELETED`. Data tidak dihapus secara fisik agar tidak memutus rantai pencarian *Linear Probing* untuk data lain.
* **Fungsi `main`:** Menjalankan program.

## Output 
<img width="467" height="418" alt="image" src="https://github.com/user-attachments/assets/05e1e3f5-2f53-4e1d-844d-0c3e169ae402" />
<img width="429" height="72" alt="image" src="https://github.com/user-attachments/assets/e671c522-c902-43e1-9e65-587929d99065" />
<img width="349" height="66" alt="image" src="https://github.com/user-attachments/assets/7c8f5ca9-b62e-4fd3-9da4-75e66b341f49" />
<img width="497" height="90" alt="image" src="https://github.com/user-attachments/assets/8bb3cd32-4c55-4d22-a87c-51706105c6f5" />
<img width="531" height="69" alt="image" src="https://github.com/user-attachments/assets/3f4f0d14-4f9a-4c82-bf79-ea7ec1860548" />


## Link YouTube
https://youtu.be/qhmJStWcQ8A
