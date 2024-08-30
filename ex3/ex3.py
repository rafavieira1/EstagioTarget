import json

def carregar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as f:
        dados = json.load(f)
    return dados["faturamento_diario"]

def calcular_estatisticas(faturamento_diario):
    faturamento_filtrado = [faturamento for faturamento in faturamento_diario if faturamento > 0]
    
    menor_faturamento = min(faturamento_filtrado)
    maior_faturamento = max(faturamento_filtrado)
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
    dias_acima_da_media = sum(1 for faturamento in faturamento_filtrado if faturamento > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media
faturamento_diario = carregar_faturamento('d:\\Estagio\\CVs\\Estagio Target\\ex3\\faturamento.json')

menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_estatisticas(faturamento_diario)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
