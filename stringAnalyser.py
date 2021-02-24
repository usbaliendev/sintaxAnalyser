'''
PAL - Primeira producao de atividade de laboratorio
Analisador de String de Caracteres
Aluno: Angelo Soares Dorfey
Disciplina: Construcao de compliladores
Data: 23/02/21
'''

import re

string = str(input("Digite uma string a ser analisada: "))

identifChar = re.findall(r'([\w\S])', string)
identifSpace = re.findall(r'\s', string)
identifTodos = re.findall(r'[\s\S]', string)
reSub = re.sub(r'\s', '', string)

print('1. - Total de caracteres encontrados: ', len(identifChar))
print('2. - Total de espaços em branco encontrados: ', len(identifSpace))
print('3. - Total de caracteres e espaços: ', len(identifTodos))
print('4. – ', reSub)
