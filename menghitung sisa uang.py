# Uang ibu: 200000
# berat telur : 5
# harga telur 26000
# ongkos 3500
uang_ibu = int(input('Uang ibu : '))
ongkos_ibu = int(input('Ongkos ibu : '))
harga_telur = int(input('Harga telur : '))
berat_telur = int(input('Berat telur : '))


ongkos_pp = ongkos_ibu * 2
total_harga = berat_telur * harga_telur + ongkos_pp
sisa_uang =  uang_ibu % total_harga

print("Sisa uang ibu adalah:", sisa_uang)
