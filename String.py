kalimat = input('Input kalimat: ')

karakter = ''.join(kalimat.split())
print(f'Jumlah karakter (tanpa spasi) adalah: {len(karakter)}')

kapital = kalimat.upper()
print(f'Kalimat user kapital: {kapital}')

huruf_vokal = ['A', 'I', 'U', 'E', 'O']
jumlah_vokal = 0

for i in huruf_vokal:
    jumlah_vokal += kapital.count(i)

print(f'Jumlah vokal dalam kalimat ada: {jumlah_vokal}')