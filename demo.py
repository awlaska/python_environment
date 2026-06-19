# numero = 2

# print(numero)
# print(type(numero))

# numerox = "2"

# print(numerox)
# print(type(numerox))

# numero : int = 2
# numerox : str = "2"

# numero = "cibersegurança"

# print(numero)
# print(type(numero))

# numero : float = 0.8

# validado : bool = False
# print(f"Variável validade {validado} - type {type(validado)}")

# print(2+2)
# print("a" + "b")


# try:
#     print(2 + "a")
# except Exception as e:
#     print(f"Erro: {e}")
#     print(str(2) + "a")

# print("a" > "b")

# print(1!=2)

# if 2 > 1:
#     print("2>1")
# elif 2 < 1:
#     print("2<1")
# else:
#     print("Falso")

# for i in range(2,10,3):
#     print(i)

# print("While Loop")
# i = 0
# while i < 3:
#     print(i)
#     i += 1

# print("a += 2")
# a : int = 5
# a +=2
# print(a)


# print("Estruturas de Dados")
# tipos_de_ataques : list = ["brute force", "sql injection", "phishing"]

# print(tipos_de_ataques)
# print(type(tipos_de_ataques))

# for i in range(len(tipos_de_ataques)):
#     if tipos_de_ataques[i] == "brute force":
#         continue
#     print(f"Tipo de ataque {i} - {tipos_de_ataques[i]}")

# lista_vazia = list()


# dict
# key - value
# time_to_recover = {"brute force": 2,
#                    "sql injection": 3,
#                    "phishing": 4}

# print(time_to_recover)
# print(type(time_to_recover))

# print(f"time_to_recover keys: {time_to_recover.keys()}")
# print(f"time_to_recover values: {time_to_recover.values()}")

# print(f"time_to_recover phishing: {time_to_recover['phishing']}")

# tuplos tem de ser o mesmo tipo
# nos sets ele elimina os valores repetidos e ordena os valores

# new_tuple = ("aaaa", "zzzz", "bbbb", "aaaa", "yyyy")
# print(new_tuple)

# new_set = {"aaaa", "zzzz", "bbbb", "aaaa", "yyyy"}
# print(new_set)

# switch case
# value = 2
# match value:
#     case 1:
#         print("Valor é 1")
#     case 2:
#         print("Valor é 2")
#     case _:
#         print("Valor é diferente de 1 e 2")

alunos : list = [
    {"id" : 21312,
     "nota" : 20,
     "name" : "João"},
     {"id" : 21313,
     "nota" : 18,
     "name" : "Joana"},
     {"id" : 21314,
     "nota" : 16,
     "name" : "Julio"}
    ]

# 1 abordagem
tamanho_da_lista = len(alunos)
print(f"Tamanho da lista: {tamanho_da_lista}")

for i in range(tamanho_da_lista):
    print(f"Valor do i: {i}")
    if alunos[i]["name"] == "Joana":
        print(f"Aluno encontrado: {alunos[i]["nota"]}")

# 2 abordagem
for aluno in alunos:
    if aluno["name"] == "Joana":
        print(f"Aluno encontrado: {aluno["nota"]}")

