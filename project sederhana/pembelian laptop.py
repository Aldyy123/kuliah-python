pembeli = input("Nama pembeli: ")
jumlah_beli = int(input("Jumlah laptop: "))
phone = int(input("Phone: "))

print("""
\t  Jenis Laptop yang kami sediakan yaitu
\t  ACER, ASUS, LENOVO, HP
""")

type_laptop = input("Type laptop yang kamu pilih: ")

laptop = {
    "ACER" : 3500000,
    "ASUS" : 4000000,
    "LENOVO": 45000000,
    "HP" : 5000000,
}

harga_laptop = laptop[type_laptop]

if jumlah_beli >= 6:
    bonus = 'Anda mendapat bonus free Handphone'
elif jumlah_beli >= 3:
    bonus = 'Anda mendapat bonus free Headset'
else:
    bonus = 'Anda tidak mendapat bonus'

total_harga = jumlah_beli * harga_laptop
uang = int(input("Masukan uang anda: "))
kembalian = total_harga - uang

if uang < total_harga:
    print("Uang anda kurang")
else:
    print("""
    ----------------------------------------------------------------
    -------------------- Struk Pembelian ---------------------------
    ----------------------------------------------------------------

    \t  Nama pembeli : {} 
    \t  Anda membeli laptop : {}
    \t  Total pembelian : {}
    \t  Total harga laptop : Rp {}
    \t  {}
    """.format(pembeli, jumlah_beli, type_laptop, total_harga, bonus))
    