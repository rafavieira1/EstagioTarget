import json

def carregar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as f:
        dados = json.load(f)
    return dados

def calcular_percentual(faturamento):
    total_faturamento = sum(faturamento.values())
    percentual_estado = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}
    return percentual_estado

faturamento_estado = carregar_faturamento('d:/Estagio/CVs/Estagio Target/ex4/faturamento.json')

percentual = calcular_percentual(faturamento_estado)

print("Percentual de representação de cada estado:")
for estado, percent in percentual.items():
    print(f"{estado}: {percent:.2f}%")
