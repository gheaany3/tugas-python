# 1. buat fungsi persegi panjang 
# 2. buat fungsi angka 125000 menjadi 125.000 (contoh)
# 3. buat fungsi cekstock(stok, jumlah) yang mengembalikan "true" jika stock masih ada, 
# jika tidak ada "false"

# nomor 1
def persegi_panjang(panjang, lebar):
    print(panjang * lebar)

persegi_panjang(20, 11)

# nomor 2
def format_rupiah(angka):
    return f"{angka:,}".replace(",", ".")

print(format_rupiah(125000))

# nomor 3
def cekstock(stok, jumlah):
    if stok >= jumlah:
        return True
    else:
        return False

print(cekstock(10, 5))  # True
print(cekstock(3, 5))   # False