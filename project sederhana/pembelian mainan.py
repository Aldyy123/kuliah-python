# Menampilkan teks TOKO MAINAN ANAK
# Fungsi \t artinya new tab yang berfungsi memberikan spasi tab index ke dalam teks
# Fungsi \n artinya new line yang berfungsi membuat baris kosong di bawah teks
print('\t\t TOKO MAINAN ANAK \n')
print('\t\t ****************')

# Input() berfungsi untuk memasukan input dari users
# Contohnya ketika muncul di terminal, masukan nama Pembeli : ${Isikan nama yang di input saat muncul di terminal}
# variabel berfungsi untuk menyimpan menginisiasi data sementara
# contohnya name_buyer =  input('Masukan Nama Pembeli : ')
# name_buyer akan menyimpan input yang telah di masukan oleh users
name_buyer = input('Masukan Nama Pembeli : ')
toy_code = input('Masukan Kode Mainan : ')

# int() berfungsi untuk mengganti tipe data ke integer, karena tipe data bawaan input itu adalah string
# Maka input itu di convert ke tipe data int dengan menggunakan syntax int()
# Contohnya price = int(input('Masukan Harga : '))
# variabel price akan mengganti tipe data dari string ke int
price = int(input('Masukan Harga : '))
total_product = int(input('Masukan Jumlah Beli : '))

# Disini kalikan total_product dengan harga product
# Contohnya dengan cara total_product * price
# Fungsi bintang (*) pemprograman itu berfungsi untuk mengalikan bilangan intenger
total_price = total_product * price
print('====================================')

# Tampilkan datanya dengan menggunakan print()
# untuk menampilkan data user, gunakan tanda koma (,) di dalam print untuk menyambung datanya
# Contohnya print('Nama Pembeli\t = ', name_buyer)
# Hasilnya = Nama Pembeli   = Amalia
print('Nama Pembeli\t = ', name_buyer)
print('Kode Mainan\t = ', toy_code)
print('Harga\t = ', price)
print('Jumlah Beli\t = ', total_product)
print('Total\t = ', total_price)
