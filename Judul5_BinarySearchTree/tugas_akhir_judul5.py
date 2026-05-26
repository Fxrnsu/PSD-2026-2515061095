class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BSTDasar:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert_node(root.left, key)
        elif key > root.key:
            root.right = self.insert_node(root.right, key)
        return root

    def insert(self, key):
        self.root = self.insert_node(self.root, key)

    def search_node(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True
        if key < root.key:
            return self.search_node(root.left, key)
        return self.search_node(root.right, key)

    def search(self, key):
        return self.search_node(self.root, key)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key, end=" -> ")
        self.inorder(root.right)

    def find_min(self, root):
        if root is None:
            return -1
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    def find_max(self, root):
        if root is None:
            return -1
        current = root
        while current.right is not None:
            current = current.right
        return current.key


def main():
    print("=== Sistem Manajemen Kode Buku Perpustakaan ===")
    
    bst = BSTDasar() 
    
    print("\n[Memuat data kode buku ke dalam sistem...]")
    bst.insert(515)
    bst.insert(004)
    bst.insert(800)
    bst.insert(100)
    bst.insert(620)
    
    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tampilkan Katalog Buku Terurut (Inorder)")
        print("2. Cari Ketersediaan Kode Buku (Search)")
        print("3. Cek Kode Buku Terkecil (Min)")
        print("4. Cek Kode Buku Terbesar (Max)")
        print("5. Tambah Kode Buku Baru (Insert)")
        print("6. Tutup Sistem")
        
        try:
            pilihan = int(input("Pilih aksi (1-6): "))
        except ValueError:
            print("Harap masukkan angka!")
            continue
            
        if pilihan == 1:
            print("Katalog Kode Buku (Terkecil - Terbesar): ", end="")
            bst.inorder(bst.root)
            print("Batas Akhir")
            
        elif pilihan == 2:
            try:
                target = int(input("Masukkan kode buku yang dicari: "))
                if bst.search(target):
                    print(f"Data Ditemukan! Buku dengan kode {target} tersedia di rak.")
                else:
                    print(f"Data Tidak Ditemukan! Kode buku {target} belum terdaftar.")
            except ValueError:
                print("Input tidak valid!")
                
        elif pilihan == 3:
            print(f"Kode klasifikasi terkecil di perpustakaan: {bst.find_min(bst.root)}")
            
        elif pilihan == 4:
            print(f"Kode klasifikasi terbesar di perpustakaan: {bst.find_max(bst.root)}")
            
        elif pilihan == 5:
            try:
                baru = int(input("Masukkan Kode Buku Baru: "))
                bst.insert(baru)
                print(f"Kode buku {baru} berhasil ditambahkan ke dalam database!")
            except ValueError:
                print("Input tidak valid!")
                
        elif pilihan == 6:
            print("Mematikan sistem database perpustakaan. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()