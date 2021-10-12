harga_satuan = int(input("Masukan Harga satuan produk: "))
banyak_produk = int(input("Banyak produk: "))

gaji = 5000000

total_harga_produk = harga_satuan * banyak_produk

if banyak_produk > 100:
    bonus = total_harga_produk * 0.20
else:
    bonus = total_harga_produk * 0.10

total_gaji = gaji + bonus

print("""
================================================================
====================== Gaji Salesman ===========================
================================================================

\t Gaji pokok anda : Rp {0}
\t Anda berhasil menjual produk dengan total {1} pcs
\t Total harga produk yang berhasil di jual yaitu Rp {2}
\t Bonus selama anda mejual produk yaitu {3}
\t Total gaji dan bonus yang anda terima sebesar : {4}
""".format(gaji, banyak_produk, total_harga_produk, int(bonus), int(total_gaji)))