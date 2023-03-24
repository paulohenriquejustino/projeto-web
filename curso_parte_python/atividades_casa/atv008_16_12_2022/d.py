

# Criando uma lista
listanotas = []
media = 0
soma = 0

# Usando for
for c in range(1,5):
    nota = float(input(f'Digite a nota do aluno: '))
    listanotas.append(nota)
    soma = soma + nota
    media = soma / 4
print(f'A média de notas do aluno é: {media:.2f}')

if media > 10:
    print(f'Aprovado!')
else:
    print(f'Reprovado')
  



   
                
                 
 


