import csv
import re

usuarios = "database_generated.csv"
numeros = r"\(\d{2}\)\s\d{5}-\d{4}"

with open(usuarios, 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:

        for coluna in linha:
                resultado = re.findall(numeros, coluna)
            # Exibe todos os números encontrados na coluna
                for numero in resultado:
                    print(numero)
        
        # Exibir  ocorrências de nomes que contenha 'Carlos' na primeira coluna
        if re.search("Carlos", linha[0]):
            print(linha)
            