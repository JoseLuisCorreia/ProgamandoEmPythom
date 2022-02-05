import emoji
salario = 8000
aumento = salario * (10/100)

novo = salario + aumento

cargo = 'DIRETOR'

print(novo)

if salario < 9000: print('É menor')
else: print('É superior')

print(len(cargo)) #(A função len serve para informar quantos caracteres a palavra tem)


print(emoji.emojize('Olá :thumbs_up:')) #(Usando emoji)

frase = 'Oi vida'

print(frase)

frase = frase.rstrip() #(O rstrip serve para eliminar os espaçoes no fim do texto)

print(frase[2:8:2]) #(Esta função traz as letras encontradas nas posições escolhidas pelo programador)

print(len(frase)) #(A função len serve para informar quantos caracteres o texto tem, incluíndo espaços)

print(frase.count('i')) #(Esta função informa quantas letras tem no texto, isso a partir da letra escohida)

print(frase.find('vid')) #(Esta função mostra em que posição(numeral) se iniciou a palavra escolhida)

print(frase.upper()) #(Esta fução deixa o texto em maiúsculo (aqui está apenas printando em maiúsculo))

frase = frase.upper()  #(Esta fução deixa o texto em maiúsculo)

print(frase.strip()) #(Aqui o strip retira os epaços do início e fim da frase)

