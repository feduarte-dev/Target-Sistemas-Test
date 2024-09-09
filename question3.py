def analisar_faturamento(faturamento_diario):
    faturamento_validos = [f for f in faturamento_diario if f > 0]
    
    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)
    
    media_anual = sum(faturamento_validos) / len(faturamento_validos)
    
    dias_acima_da_media = sum(1 for f in faturamento_validos if f > media_anual)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

faturamento_diario = [0, 1500, 2000, 0, 0, 3000, 2500, 0, 4000, 1000]
menor, maior, dias_acima_media = analisar_faturamento(faturamento_diario)

print("Menor faturamento:", menor)
print("Maior faturamento:", maior)
print("Dias com faturamento acima da média:", dias_acima_media)