from csv import reader
from collections import defaultdict
import time

from pathlib import Path

path_do_txt = "Data\weather_stations.csv"
def processar_temperaturas(path_do_txt: Path):
    print("iniciando o processamento do arquivo.")

    start_time = time.time() #tempo de inicio

    temperatura_por_station = defaultdict(list)

    with open(path_do_txt,'r',encoding="utf-8") as file:
        _reader = reader(file,delimiter= ';')
        for row in _reader:
            nome_da_station,temperatura = str(row[0]),float(row[1])
            temperatura_por_station[nome_da_station].append(temperatura)
    print( "Dados carregados,calculando estatísticas...")

    #Dicionario para armazenar os resultados calculados
    Results = {}

    for station,temperatures in temperatura_por_station.items():
        min_temp = min(temperatures)
        mean_temp = sum(temperatures)/len(temperatures)
        max_temp = max(temperatures)
        Results[station] = (min_temp,mean_temp,max_temp)

    print("Estatística calculada,ordenando...")
    #ordenando os resultados pelo nome da estação
    sorted_results = dict(sorted(Results.items()))

    # formatando os resultados para exibição
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
                         for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    return formatted_results


if __name__ == "__main__":
    path_do_csv = "data/measurements.txt"

    print("Iniciando o processamento do arquivo.")
    start_time = time.time()  # Tempo de início

    resultados = processar_temperaturas(path_do_csv)

    end_time = time.time()  # Tempo de término

    for station, metrics in resultados.items():
        print(station, metrics, sep=': ')

    print(f"\nProcessamento concluído em {end_time - start_time:.2f} segundos.")    