'''[URI – 1018 (Adaptada)] Cédulas
Escreva um programa para ler um valor inteiro. A seguir, calcule o menor número de notas
possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a
relação de notas necessárias.'''
vlr = int(input('Digite o valor: '))
cem = int(vlr / 100)
rc = vlr % 100
cq = int(rc / 50)
rcq = rc % 50
vt = int(rcq / 20)
rvt = rcq % 20
dz = int(rvt / 10)
rdz = rvt % 10
cc = int(rdz / 5)
rcc = rdz % 5
ds = int(rcc / 2)
rds = int(rcc % 2)
um = rds

print(cem,'notas de 100')
print(cq,'notas de 50')
print(vt,'notas de 20')
print(dz,'notas de 10')
print(cc,'notas de 5')
print(ds,'notas de 2')
print(um,'moeda de 1')

          
