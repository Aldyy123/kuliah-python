def selectionSort(val):
    for isi in range(len(val) - 1, 0, -1):
        Max=0
        for lokasi in range(1, isi+1):
            if val[lokasi]>val[Max]:
                Max = lokasi
        
        temp = val[isi]
        val[isi] = val[Max]
        val[Max] = temp

daftarAngka = [7,4,5,9,8,2,1]
selectionSort(daftarAngka)
print(daftarAngka)
print('Selection sort')

def bubleSort(val):
    for passNum in range(len(val) - 1,0, -1 ):
        for i in range(passNum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp

angka = [2,4,3,6,8,7,1]
bubleSort(angka)
print(angka)
print('Buble Sort')

def insertionSort(val):
    for index in range(1, len(val)):
        valueaktif = val[index]
        posisi = index

        while posisi > 0 and val[posisi -1]>valueaktif:
            val[posisi] = val[posisi-1]
            posisi = posisi-1
        
        val[posisi] = valueaktif

daftarAngka = [2,4,6,3,2,9,8]
insertionSort(daftarAngka)
print(daftarAngka)
print('Insertion sort')