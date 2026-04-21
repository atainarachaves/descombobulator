#!/usr/bin/env python3
"""
Demonstração manual do funcionamento do Descombobulator
Usando o exemplo do enunciado: resultado esperado "47"
"""

import sys
sys.setrecursionlimit(10**7)

# Criar o exemplo do enunciado
exemplo_entrada = """a memimomu
e mimomu
i mooo
u mimimi
o
m
"""

# Simular parse
regras = {}
linhas = exemplo_entrada.strip().split('\n')

for linha in linhas:
    partes = linha.split()
    if partes:  # Pular linhas vazias
        letra = partes[0]
        if len(partes) == 1:
            regras[letra] = ""
        else:
            regras[letra] = partes[1]

print("=" * 60)
print("DEMONSTRAÇÃO DO DESCOMBOBULATOR")
print("=" * 60)
print()

print("Entrada (tabela de regras):")
for letra in sorted(regras.keys()):
    if regras[letra]:
        print(f"  {letra} → {regras[letra]}")
    else:
        print(f"  {letra} → (terminal, permanece como '{letra}')")
print()

# Simular a expansão manual
print("Processo de expansão começando com 'a':")
print("-" * 40)

# Mostramos passo a passo
expansoes = {
    'a': 'memimomu',
    'e': 'mimomu',
    'i': 'mooo',
    'u': 'mimimi',
    'o': 'o',
    'm': 'm'
}

# Expansão nível 1
print("Nível 1: a")
print(f"  a → {expansoes['a']}")
print()

# Expansão nível 2
nivel2 = f"m{expansoes['e']}m{expansoes['i']}m{expansoes['o']}m{expansoes['u']}"
print("Nível 2: expandindo cada letra de 'memimomu'")
print(f"  m = m")
print(f"  e = mimomu")
print(f"  m = m")
print(f"  i = mooo")
print(f"  m = m")
print(f"  o = o")
print(f"  m = m")
print(f"  u = mimimi")
print(f"  Resultado: {nivel2}")
print(f"  Comprimento: {len(nivel2)}")
print()

# Agora usar o algoritmo de memoização para calcular o tamanho
print("-" * 40)
print("Algoritmo de cálculo de tamanho (sem gerar string):")
print()

memo = {}
visitando = set()

def tamanho(letra):
    """Calcula o tamanho final da expansão de uma letra"""
    
    # Verificar cache
    if letra in memo:
        print(f"  tamanho('{letra}') = {memo[letra]} (do cache)")
        return memo[letra]
    
    # Detectar ciclos
    if letra in visitando:
        raise Exception(f"Ciclo detectado em '{letra}'")
    
    visitando.add(letra)
    
    # Regra terminal
    if regras[letra] == "":
        res = 1
        print(f"  tamanho('{letra}') = 1 (terminal)")
    else:
        # Recursivo: soma dos tamanhos
        subtamanhos = []
        for c in regras[letra]:
            subt = tamanho(c)
            subtamanhos.append(subt)
        res = sum(subtamanhos)
        print(f"  tamanho('{letra}') = sum({' + '.join(str(s) for s in subtamanhos)}) = {res}")
    
    visitando.remove(letra)
    memo[letra] = res
    return res

# Calcular para 'a'
print("Calculando tamanho('a'):")
resultado = tamanho('a')

print()
print("=" * 60)
print(f"RESULTADO FINAL: {resultado} caracteres")
print("=" * 60)
print()

# Gerar a string real para validação
def gerar_string(letra):
    """Gera a string expandida (cuidado: pode consumir muita memória)"""
    if regras[letra] == "":
        return letra
    return "".join(gerar_string(c) for c in regras[letra])

string_real = gerar_string('a')
print(f"String gerada: {string_real}")
print(f"Comprimento real: {len(string_real)}")
print()
print(f"Validação: tamanho({resultado}) == len(string) ({len(string_real)}) ? {resultado == len(string_real)}")
