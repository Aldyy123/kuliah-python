from colorama import Fore

pembeli = input("Nama pembeli: ")
jumlah_beli = int(input("Jumlah tiket: "))
phone = int(input("Phone: "))

print("""
    Nama jurusan Surabaya Kode SBY \n
    Nama jurusan Lampung Kode LMP \n
    Nama jurusan Bali Kode BL \n
""")
jurusan = input("Jurusan: ")
harga_tiket = 0

if jurusan == 'SBY':
    jurusan = "Surabaya"
    harga_tiket = 300000
elif jurusan == "BL":
    jurusan = "Bali"
    harga_tiket = 350000
elif jurusan == 'LMP':
    jurusan = "Lampung"
    harga_tiket = 500000
else:
    print("Jurusan yang anda pilih tidak ada")



potongan = 0

if jumlah_beli >= 3:
    potongan = harga_tiket * 0.10

total_harga = int((jumlah_beli * harga_tiket) - potongan )

print('Anda membeli {0} tiket Jurusan ke {1}, seharga Rp {3}{2}{4}'.format(jumlah_beli, jurusan, total_harga, Fore.GREEN, Fore.RESET))
uang = int(input('Masukan uang anda : '))

if uang <= total_harga:
    print('Maaf, uang anda kurang')
else:
    kembalian = uang - total_harga
    print("""
    ===================================================
    =============== Struk pembelian tiket =============
    ====================================================
    \t  Nama pembeli {3}{7}{4}
    \t  Tiket ke arah {3}{2}{4}
    \t  Total pembelian tiket anda : {3}{1}{4}
    \t  Total harganya adalah : Rp {3}{0}{4}
    \t  Uang anda senilai : Rp {3}{6}{4}
    \t  Kembalian yang anda terima : Rp {3}{5}{4}

    """.format(total_harga, jumlah_beli, jurusan, Fore.GREEN, Fore.RESET, kembalian, uang, pembeli))
    if potongan > 0:
        print('\t   Anda mendapat potongan senilai Rp {1}{0}{2}'.format(int(potongan), Fore.GREEN, Fore.RESET))

    print("""
    ================================================================
    ================================================================
    """)

