list_mahasiswa = []

while True:
    print('''=== List Mahasiswa ===
1. Masukkan data
2. Menampilkan data
3. Keluar
======================''')
    x = int(input('Pilih menu: '))
    
    if x == 1:
        nama = input('Masukkan nama mahasiswa: ')
        NIM = (input('Masukkan NIM: '))
        daerah = input('Masukkan daerah asal: ')

        list_mahasiswa.append({'Nama': nama, 'NIM': NIM, 'Daerah asal': daerah})
        print('Data berhasil ditambahkan.')

    elif x == 2:
        print(f'Data mahasiswa: \n{list_mahasiswa}')

    elif x == 3:
        print('Terimakasih.')
        break

    else:
        print('Masukkan angka 1-3.')
