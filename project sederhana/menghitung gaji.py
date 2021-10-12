gaji_pokok = int(input('Gaji pokok : '))
jam_kerja = int(input('Masukan Jam kerja : '))


gaji_pokok = gaji_pokok

tunjangan = gaji_pokok * 0.20
pajak = gaji_pokok * 0.10

jam_kerja = (jam_kerja * 5) * 4


gaji_lembur = ''
total_gaji = ''
if jam_kerja > 200:
    gaji_lembur = 20000 * (jam_kerja - 160)
    total_gaji = gaji_pokok + gaji_lembur
    gaji_lembur = "Anda mendapatkan tambahan gaji lembur : Rp {}".format(gaji_lembur)
    total_gaji = "Total gaji serta lemburan anda senilai : Rp {}".format(total_gaji)


print("""
================================================================
====================== Hasil Gaji Karyawan =====================
================================================================

\t Mendapat tunjangan sebesar : Rp {1}
\t Anda terkena pajak sebesar : Rp {2}
\t Jam kerja anda selama bekerja yaitu : {3}
\t Gaji yang di terima anda : Rp {0}
\t {4}
\t {5}
=================================================================
=================================================================
""".format(gaji_pokok, int(tunjangan), int(pajak), jam_kerja, gaji_lembur, total_gaji))