import csv
import time
import os
import requests
from services import EvolutionAPI

# --- Configurações ---
# Caminho do arquivo CSV com os contatos
CSV_PATH = 'teste wzap Python - Página1.csv'
# Tempo de espera entre mensagens (em segundos)
TIMER_SECONDS = 420
# Arquivo para salvar números com erro
ERROR_FILE_PATH = 'wrong_numbers.csv'
# --- Fim das Configurações ---

evo_client = EvolutionAPI()

# Prepara o arquivo de erros com cabeçalho, se não existir
if not os.path.exists(ERROR_FILE_PATH):
    with open(ERROR_FILE_PATH, 'w', newline='', encoding='utf-8') as error_file:
        writer = csv.writer(error_file)
        writer.writerow(['nome', 'whatsapp', 'error_response'])

with open(CSV_PATH, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nome = row['nome'].split()[0]
        whatsapp = "55" + row['@whatsapp']

        # This is an example message; customize as needed, for our case, its a refinance offer to the Safra bank
        target_message = f"""Oi {nome}, Boa Tarde!

        Como você está? Lembra de mim?

        Passando para comunicar que houve atualização com a *REDUÇÃO DE TAXA DE JUROS* no banco *SAFRA*, e muito provavelmente você poderá reduzir a taxa do seu empréstimo consignado e ainda ter um bom valor de troco liberado.

        *Caso queira fazer uma simulação e validar o valor, digite*
        1 - Quero simular 😁
        2 - Não, obrigado 👍
        3 - Não sou a pessoa, obrigado 😓"""
        
        try:
            print(f"--- Preparing to send to {whatsapp} ---")
            print(f"Message content:\n{target_message}")
            response = evo_client.send_message(number=whatsapp, text=target_message)

            # Verifica se a mensagem foi enviada com sucesso (lógica da API)
            if 'key' not in response:
                raise Exception(f"API Error: {response}")

            print(f"Enviado para {nome} ({whatsapp}): {response}")
            print(f"Aguardando {TIMER_SECONDS} segundos antes do próximo envio...")
            time.sleep(TIMER_SECONDS)

        except (requests.exceptions.RequestException, Exception) as e:
            error_message = str(e)
            print(f"Falha ao enviar para {nome} ({whatsapp}): {error_message}")
            # Salva o número com erro no arquivo
            with open(ERROR_FILE_PATH, 'a', newline='', encoding='utf-8') as error_file:
                writer = csv.writer(error_file)
                writer.writerow([nome, whatsapp, error_message])
            continue  # Pula para o próximo número
