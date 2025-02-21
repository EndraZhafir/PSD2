hari = ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')

pilih_hari = int(input('Input angka dari 1-7: '))

if 1 <= pilih_hari <= 7:
    print(hari[pilih_hari - 1])

else:
    print('User input salah.')