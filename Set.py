setA = {1, 2, 3, 4, 5}  
setB = {4, 5, 6, 7, 8}

setC = setA.union(setB)
print(f'Gabungan dari setA dan setB: {setC}')

irisan = []
for i in setA:
    if i in setB:
        irisan += [i]

print(f'Irisan dari setA dan setB: {irisan}')

selisihA = setA - setB
selisihB = setB - setA
print(f'Selisih setA - setB: {selisihA}')
print(f'Selisih setA - setB: {selisihB}')