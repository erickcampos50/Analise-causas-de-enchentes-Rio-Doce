#%%
import requests
from datetime import datetime, timedelta
import pandas as pd
import json
import time

# Define o intervalo de datas para iterar
start_date = datetime.strptime('2020-01-01', '%Y-%m-%d')
end_date = datetime.strptime('2023-12-31', '%Y-%m-%d')
interval = timedelta(days=90)

# Define o atraso entre as solicitações (em segundos)
request_delay = 2  # Ajuste conforme necessário para respeitar os limites da API

# Crie uma lista para armazenar os conteúdos da resposta
response_contents = []

# Itere sobre o intervalo de datas
current_date = start_date
while current_date <= end_date:
    # Formate a data atual como 'yyyy-mm-dd'
    formatted_date = current_date.strftime('%Y-%m-%d')
    
    # Faça uma solicitação à URL especificada
    url = 'https://www.snirh.gov.br/hidroweb/rest/api/documento/gerarTelemetricas?codigosEstacoes=185241570&tipoArquivo=3&periodoInicial={}&periodoFinal={}'.format(formatted_date, (current_date + interval).strftime('%Y-%m-%d'))
    print(url)
    
    try:
        response = requests.get(url)

        # Verifique o código de status da resposta
        if response.status_code == 200:
            # Converta a resposta JSON em um DataFrame
            data = json.loads(response.content)
            df = pd.DataFrame(data[0])

            # Expanda o JSON aninhado "medicoes" em colunas separadas
            df_medicoes = pd.json_normalize(df['medicoes'])
            df = pd.concat([df.drop(columns=['medicoes']), df_medicoes], axis=1)

            # Adicione o DataFrame à lista de conteúdos da resposta
            response_contents.append(df)
            print('Successfully retrieved data for {}'.format(formatted_date))
            
            # Salve o DataFrame combinado como CSV após cada iteração
            combined_df = pd.concat(response_contents, ignore_index=True)
            csv_file_name = 'Dados_HidroWEB.csv'
            combined_df.to_csv(csv_file_name, index=False)
            print('CSV data saved to {}'.format(csv_file_name))
        else:
            # Imprima uma mensagem de erro
            print('Error retrieving data for {}: {}'.format(formatted_date, response.status_code))
    
    except Exception as e:
        # Lidar com erros de conexão ou outras exceções
        print('An error occurred for {}: {}'.format(formatted_date, str(e)))

    # Aguarde um pouco antes da próxima solicitação
    time.sleep(request_delay)

    # Incremente a data atual pelo intervalo
    current_date += interval

# %%
