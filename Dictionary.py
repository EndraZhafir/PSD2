mahasiswa = {
    "2351345TK22456": "Fahim",
    "2467890KG25467": "Edelweis",
    "2245644SV23478": "Muhammad Hardiyanto"
}

x = input('Input NIM mahasiswa tanpa garis miring: ')
if x in mahasiswa:
        print(mahasiswa[x])
else:
    print('NIM mahasiswa tidak ditemukan.')