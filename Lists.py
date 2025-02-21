user_input = input('Masukkan 5 angka (pisah dengan spasi): ')
list_angka = list(map(int, user_input.split()))

print(f'List input user: {list_angka}')

total = sum(list_angka)
print(f'Total jumlah: {total}')

terurut = sorted(list_angka)
print(f'List terurut: {terurut}')

terurut.pop()
print(terurut)