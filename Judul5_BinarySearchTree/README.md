# Judul Program
Sistem Manajemen Kode Buku Perpustakaan

## Deskripsi Singkat
Program ini berfungsi untuk mencatat, mencari, dan mengurutkan kode buku di sebuah perpustakaan.

## Source Code
<img width="1678" height="4928" alt="codeta5" src="https://github.com/user-attachments/assets/35d15d7e-9002-466b-a2f3-9d8f11301d3a" />

**Penjelasan Logika Program:**
1. `class Node:` : Mendeklarasikan kelas `Node` yang berfungsi sebagai cetakan dasar untuk membuat setiap simpul di dalam pohon biner.
2. `def __init__(self, key):` : Konstruktor inisialisasi saat sebuah node baru dibuat.
3. `self.key = key` : Variabel untuk menyimpan nilai data utama.
4. `self.left = None` dan `self.right = None` : Saat simpul baru dibuat, pointer ke anak kiri dan anak kanan secara *default* dikosongkan karena belum memiliki cabang.

5. `class BSTDasar:` : Kelas utama yang memuat kerangka pohon dan metode-metode algoritmanya.
6. `def __init__(self): self.root = None` : Saat objek pohon biner pertama kali dibuat, akarnya (`root`) ditetapkan kosong.
7. 
8. `def insert_node(self, root, key):` : Fungsi rekursif yang bertugas mencari posisi yang tepat untuk menyisipkan node baru.
9. `if root is None: return Node(key)` : Ini adalah batas rekursi. Jika posisi yang sedang dicek kosong, maka buat dan letakkan node baru di posisi tersebut.
10. `if key < root.key:` : Jika kode buku baru lebih kecil dari kode buku di node saat ini.
11. `root.left = self.insert_node(root.left, key)` : Panggil kembali fungsinya secara rekursif untuk masuk dan mengecek subpohon sebelah kiri.
12. `elif key > root.key:` : Jika kode buku baru lebih besar dari node saat ini.
13. `root.right = self.insert_node(root.right, key)` : Panggil kembali fungsinya secara rekursif untuk masuk ke subpohon sebelah kanan.
14. `return root` : Mengembalikan struktur node agar pohon tetap tersambung utuh setelah rekursi selesai.
15. 
16. `def insert(self, key):` : Fungsi pembungkus (*wrapper*). Tujuannya agar saat dipanggil di menu utama, pengguna cukup mengetik `bst.insert(nilai)` tanpa perlu repot-repot mengirimkan parameter `root`.

15. `def search_node(self, root, key):` : Fungsi rekursif untuk melacak keberadaan data kode buku.
16. `if root is None: return False` : Jika penelusuran sudah sampai di ujung daun dan data tidak ada, kembalikan nilai False (Gagal).
17. `if root.key == key: return True` : Jika nilai node saat ini sama persis dengan yang dicari, kembalikan True (Sukses).
18. `if key < root.key: return self.search_node(root.left, key)` : Jika target pencarian lebih kecil, abaikan cabang kanan dan terus cari hanya di cabang kiri.
19. `return self.search_node(root.right, key)` : Jika target lebih besar, cari hanya di cabang kanan.
20. `def search(self, key):` : Fungsi pembungkus (*wrapper*) pencarian untuk menu utama.

21. `def inorder(self, root):` : Fungsi penelusuran *Inorder* untuk mencetak data. Aturannya: Kiri -> Akar -> Kanan.
22. `if root is None: return` : Batas rekursi penelusuran.
23. `self.inorder(root.left)` : Telusuri terus secara paksa ke cabang paling kiri terlebih dahulu.
25. `print(root.key, end=" -> ")` : Setelah mentok di kiri, cetak nilainya ke layar.
26. `self.inorder(root.right)` : Setelah mencetak akar kiri, baru telusuri cabang kanan. Hasilnya data akan tercetak otomatis berurutan dari kecil ke besar.
27. 
28. `def find_min(self, root):` : Fungsi pencari nilai terkecil.
29. `while current.left is not None: current = current.left` : Program melakukan perulangan (`while`) yang terus bergeser ke penunjuk anak sebelah kiri sampai mentok. Node paling ujung kiri adalah nilai terkecil.
30. 
31. `def find_max(self, root):` : Fungsi pencari nilai terbesar.
32. `while current.right is not None: current = current.right` : Program dipaksa terus bergeser ke cabang kanan mentok untuk mendapatkan nilai maksimum.

30. `def main():` : Tempat berjalannya antarmuka terminal program.
31. `bst = BSTDasar()` : Menginstansiasi objek dari kelas BSTDasar.
32. `bst.insert(...)` : Memasukkan 5 data kode buku agar pohon biner langsung terbentuk tanpa perlu input manual di awal.
33. `while True:` : Memulai perulangan tanpa henti agar menu terus muncul setelah suatu aksi selesai dilakukan.
34. `try-except ValueError:` : Sistem penanganan *error*. Jika pengguna iseng memasukkan tipe data huruf/string pada *input* menu atau input pencarian, program tidak akan mengalami *crash/force close*, melainkan mencetak peringatan.
35. `if pilihan == 1:` hingga `elif pilihan == 6:` : Struktur kontrol pencabangan kondisi untuk merespons masukan pengguna dan memanggil fungsi-fungsi BST yang sesuai.
36. 
## Output Program
<img width="601" height="206" alt="image" src="https://github.com/user-attachments/assets/aba57a1d-67ba-4ae1-a83b-3f64a4158661" />
<img width="496" height="68" alt="image" src="https://github.com/user-attachments/assets/30536913-dd43-4061-818b-494af3995079" />
<img width="326" height="57" alt="image" src="https://github.com/user-attachments/assets/5196824e-51b3-4603-a271-2eda703924bb" />
<img width="323" height="52" alt="image" src="https://github.com/user-attachments/assets/9d7abb25-12a8-4f1e-9048-fd94def204b9" />

**Penjelasan Output:**
Ketika menu 1 dipilih, program menampilkan kode-kode buku yang tadinya tidak teratur menjadi terurut dari nilai yang paling kecil (40) ke yang paling besar (800). Ketika menu 2 dipilih dan dimasukkan angka 515, algoritma BST memproses dengan cepat dan mencetak bahwa buku tersebut tersedia di rak. Pemilihan menu 3 dan 4 mencetak simpul paling ujung kiri dan simpul paling ujung kanan di pohon.

## Link YouTube
https://youtu.be/krCapVAhDn4
