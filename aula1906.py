import os

for file in os.listdir():
    if os.path.isfile(os.path.abspath(file)):
        if file.endswith(".txt"):
            print(file)

f = open("ficheiro.txt", "w")

f.write("asdasd")

f.close()

with open("ficheiro.txt", "r") as file:
    print(file.readlines())