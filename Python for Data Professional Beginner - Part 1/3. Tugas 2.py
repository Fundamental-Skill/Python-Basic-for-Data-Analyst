"""
Tugas:
Aku diminta menghitung harga_setelah_potongan dan harga_final. 
harga_final diperoleh dengan mengalikan harga_setelah_potongan
dengan angka 1.1 karena PPN sebesar 10% (100% + 10% = 110% atau 1.1)
Aku menggunakan variabel harga_asli dengan nilai 20000 dan variabel potongan dengan nilai 2000.

"""

harga_asli = 20000
potongan = 2000

harga_final = (harga_asli - potongan) * 1.1

print(round(harga_final))
