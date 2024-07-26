class CartItem:
    """
    class yang merepresentasikan item dalam keranjang belanja.
    Atribut:
        nama (str): Nama item.
        harga (float): Harga item.
    Metode:
        __init__(self, nama, harga): Inisialisasi item dengan nama dan harga.
    """
    def __init__(self, nama, harga): #  Inisialisasi objek CartItem dengan nama dan harga.
        self.nama = nama # input data berupa string
        self.harga = harga # input data berupa float

    def __str__(self): # Mengembalikan representasi string dari objek CartItem.
        return f"{self.nama}: Rp.{self.harga}" # str: String yang merepresentasikan nama dan harga item dalam format 'nama: Rp(rupiah).harga'.

class ShoppingCart:
    """
    class yang merepresentasikan keranjang belanja, Atribut: cart (list): Daftar item yang ada di keranjang belanja.
    """
    def __init__(self): # Metode inisialisasi objek ShoppingCart dengan keranjang yang masih kosong.
        self.cart = []

    def display_menu(self): # Menampilkan seluruh menu yang harus diisi oleh user
        print('''
              Selamat Datang di Keranjang Belanja Toko Makmur Serba Ada!''') 
        print("\nMenu:")
        print("1. Menambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang di Keranjang") 
        print("4. Lihat Total Belanja") 
        print("5. Exit")

    def add_item(self):
        '''Menu menambahkan item baru ke dalam keranjang, user diminta untuk memasukkan nama barang dan harga melalui input kemudian
        membuat objek CartItem baru lalu memasukkannya ke dalam keranjang '''    
        nama = input("Masukkan nama barang: ") # Baris 38 - 39  Membuat objek CartItem dengan nama dan harga yang dimasukkan user.
        harga = float(input("Masukkan harga: "))
        item = CartItem(nama, harga) # Baris 40 - 41 Menambahkan objek CartItem ke dalam atribut cart.
        self.cart.append(item)
        print(f"Barang {nama} berhasil dimasukkan ke keranjang.") # Menampilkan pesan bahwa barang berhasil dimasukkan ke keranjang.

    def remove_item(self): # Menu untuk menghapus item yang sudah di masukkan ke dalam keranjang
        '''Menghapus item dari keranjang belanja berdasarkan nama yang dimasukkan oleh pengguna.
        Kemudian, metode ini akan mengiterasi item-item dalam keranjang untuk menemukan item yang sesuai.'''
        nama = input("Masukkan nama barang yang ingin dihapus: ")
        for item in self.cart:
            if item.nama == nama: # Baris 56 -57 - Menghapus item jika nama yang sesuai dan ada didalam keranjang.
                self.cart.remove(item)
                print(f"Barang {nama} berhasil dihapus dari keranjang.")
                break
        else:
            print(f"Pilihan yang anda maksud {nama} tidak ada silahkan coba lagi.") # Menampilkan pesan kalau item yang ingin di hapus oleh user tapi item tersebut tidak ada di dalam keranjang

    def show_item_in_cart(self): # Menampilkan semua item yang sudah dimasukkan kedalam keranjang
        '''Menampilkan detail item dari keranjang belanja berdasarkan nama yang dimasukkan oleh pengguna.
        Kemudian, metode ini akan mengiterasi item-item dalam keranjang.'''  
        if not self.cart:
            for item in self.cart:
                print("Tidak ada barang didalam keranjang.")
        else:
            print("Barang di dalam keranjang")
            for item in self.cart:
                print(item)

    def total_price_item(self):
        '''Menghitung dan menampilkan total harga dari semua item yang ada di dalam keranjang belanja.
        Metode ini menjumlahkan harga dari setiap item yang ada di dalam keranjang belanja dan mencetak total harga tersebut dalam format 'Total belanja:'''
        total = sum(item.harga for item in self.cart)
        print(f"Total belanja: RP.{total}")

    def exit_program(self):  
        print('''
              Terima kasih telah belanja di toko makmur serba ada sampai jumpa! ''')

    def process_choice(self, choice):
        ''''metode ini digunakan untuk memproses pilihan menu yang diberikan oleh pengguna 
        dan menerima satu parameter, choice, yang merupakan pilihan menu dari pengguna dalam bentuk string.'''
        if choice == '1':
            self.add_item()
        elif choice == '2':
            self.remove_item()
        elif choice == '3':
            self.show_item_in_cart()
        elif choice == '4':
            self.total_price_item()
        elif choice == '5':
            self.exit_program()
        else:
            print("Masukkan pilihan dengan benar!")

def main():
    '''Fungsi utama untuk menjalankan program keranjang belanja.
    Loop akan terus berjalan hingga pengguna memilih untuk keluar dari program dengan memilih opsi '5'.'''
    shopping_cart = ShoppingCart()
    while True:
        shopping_cart.display_menu()
        choice = input("Pilih menu: ")
        shopping_cart.process_choice(choice)
        if choice == '5':
            break

if __name__ == "__main__":
    main()
    '''Variable untuk menyimpan nama app yang sedang di jalankan dan ini adalah sebagai program utama '''
