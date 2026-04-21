import sys
import os
import time

sys.setrecursionlimit(10**7)

def resolver(caminho):
    regras = {}
    aparecem_direita = set()

    with open(caminho) as f:
        for linha in f:
            linha = linha.strip()
            # Ignorar linhas vazias e comentários
            if not linha or linha.startswith("//"):
                continue
            
            partes = linha.split()
            letra = partes[0]
            
            if len(partes) == 1:
                regras[letra] = ""
            else:
                regras[letra] = partes[1]
                for c in partes[1]:
                    aparecem_direita.add(c)

    # letra inicial: aquela que não aparece em nenhuma substituição (lado direito)
    # Se múltiplas: usar primeira em ordem alfabética para consistência
    todas = set(regras.keys())
    candidatas = sorted(todas - aparecem_direita)
    
    if not candidatas:
        raise Exception("Nenhuma letra inicial encontrada. Pode haver ciclo.")
    
    inicial = candidatas[0]

    memo = {}
    visitando = set()

    def tamanho(letra):
        if letra in memo:
            return memo[letra]

        if letra in visitando:
            raise Exception("Ciclo detectado")

        visitando.add(letra)

        if regras[letra] == "":
            res = 1
        else:
            res = sum(tamanho(c) for c in regras[letra])

        visitando.remove(letra)
        memo[letra] = res
        return res

    return tamanho(inicial)


def main():
    pasta = "casos"
    resultados = []

    for arquivo in sorted(os.listdir(pasta)):
        caminho = os.path.join(pasta, arquivo)
        inicio = time.time()
        resultado = resolver(caminho)
        fim = time.time()
        tempo_ms = (fim - inicio) * 1000
        resultados.append((arquivo, resultado, tempo_ms))
        print(f"{arquivo}: {resultado} (tempo: {tempo_ms:.2f}ms)")
    
    return resultados


if __name__ == "__main__":
    main()