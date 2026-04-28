from colorama import Fore, Style, init

# Inicializa o colorama
init()

def definir_cor_nivel(nivel):
    """
    Função responsável por retornar a cor correspondente 
    ao nível do reservatório.
    """
    if nivel == "Nível 1":
        return Fore.RED
    elif nivel == "Nível 2":
        return Fore.YELLOW
    elif nivel == "Nível 3":
        return Fore.GREEN
    elif nivel == "Nível 4":
        return Fore.CYAN
    elif nivel == "Nível 5":
        return Fore.BLUE
    else:
        return Style.RESET_ALL

def simular_monitoramento():
    # Lista de dicionários representando os níveis e situações do reservatório
    dados_reservatorio = [
        {"nivel": "Nível 1", "situacao": "Muito baixo (crítico)"},
        {"nivel": "Nível 2", "situacao": "Baixo"},
        {"nivel": "Nível 3", "situacao": "Médio"},
        {"nivel": "Nível 4", "situacao": "Alto"},
        {"nivel": "Nível 5", "situacao": "Muito alto (alerta)"}
    ]

    print("--- SISTEMA DE MONITORAMENTO DE RESERVATÓRIO ---")
    
    # Percorre a lista para exibir as mensagens coloridas
    for item in dados_reservatorio:
        cor = definir_cor_nivel(item["nivel"])
        print(f"{cor}{item['nivel']}: {item['situacao']}{Style.RESET_ALL}")

    print("------------------------------------------------")

# Execução do programa
if __name__ == "__main__":
    simular_monitoramento()