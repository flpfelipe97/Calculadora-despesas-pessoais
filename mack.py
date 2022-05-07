QuantidadeAlunos = int(input("Quantos alunos?"))
TotalAlunos = 0
Nota = 0

while (TotalAlunos <= QuantidadeAlunos):
    x = int(input("qual a nota?"))
    Nota = Nota + x
    TotalAlunos = TotalAlunos + 1

print(Nota)