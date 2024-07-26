import unittest
from Dani_app import CartItem, ShoppingCart  # Dari <module name> import <function name>


class TestShoppingCart(unittest.TestCase): # Kelas ini dibuat untuk menguji ShoppingCart dan CartItem.
    def setUp(self): # Menyiapkan instance/wujud baru dari ShoppingCart sebelum setiap metode tes dijalankan.
        self.cart = ShoppingCart()

    # Membuat item dan ditambahkan ke keranjang dan memverifikasi bahwa item telah ditambahkan ke keranjang
    def test_add_item(self):
        self.cart.add_item("Anggur", 10.0)
        self.assertEqual(len(self.cart.cart), 1)
        self.assertEqual(self.cart.cart[0].nama, "Anggur")
        self.assertEqual(self.cart.cart[0].harga, 10.0)

    # Menghapus item yang ada didalam keranjang dan memverifakasi bahwa item telah dihapus
    def test_remove_item(self):
        self.cart.add_item("Anggur", 10.0)
        self.cart.remove_item("Anggur")
        self.assertEqual(len(self.cart.cart), 0, "Item sudah dihapus dari keranjang")

    # Menghitung total item yang ada didalam keranjang dan memverifikasi seluruh total harga yang ada di dalam keranjang
    def test_total_price_item(self):
        self.cart.add_item("Anggur", 5.0)
        self.cart.add_item("Jeruk", 7.0)
        total = self.cart.calculate_total()
        self.assertEqual(total, 12.0, "Total belanja dari dalam keranjang")

class CartItem: # Kelas ini dibuat untuk menguji Cartitem
    def __init__(self, nama, harga): # Menyiapkan instance/wujud baru dari cartitem sebelum setiap metode tes dijalankan.
        self.nama = nama
        self.harga = harga

    def __str__(self):
        return f"{self.nama}: Rp.{self.harga}"

class ShoppingCart: # Kelas ini dibuat untuk menguji ShoppingCart dan CartItem.
    def __init__(self): # Menyiapkan instance/wujud baru dari ShoppingCart sebelum setiap metode tes dijalankan.
        self.cart = []

    def add_item(self, nama, harga):
        item = CartItem(nama, harga)
        self.cart.append(item)

    def remove_item(self, nama):
        for item in self.cart:
            if item.nama == nama:
                self.cart.remove(item)
                break

    def calculate_total(self):
        return sum(item.harga for item in self.cart)

if __name__ == "__main__":
    unittest.main(verbosity=2)    
    '''Mengeksekusi tes unit jika skrip dijalankan sebagai program utama serta menampilkan output mendetail
    karena menggunakan verbosity 2'''
