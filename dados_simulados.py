# ============================================================
# dados_simulados.py
# Responsável por GERAR os dados falsos da missão espacial.
# Em um sistema real, esses dados viriam de sensores físicos.
# Aqui usamos random para simular variações reais.
# ============================================================

import random

# Esses são os nomes dos módulos que existem na missão
MODULOS = ["Módulo Solar Alpha", "Módulo Solar Beta", "Propulsão", "Habitação", "Comunicação"]

def gerar_dados_missao():
    """
    Gera um dicionário com todos os dados simulados da missão.
    Cada chamada desta função = uma nova 'leitura de sensores'.
    """
    dados = {
        # Temperatura em graus Celsius (pode ser muito fria ou muito quente no espaço)
        "temperatura": round(random.uniform(-60, 160), 1),

        # Nível de energia da nave em percentual
        "energia": round(random.uniform(0, 100), 1),

        # Potência gerada pelos painéis solares em Watts
        "potencia_solar": round(random.uniform(0, 5000), 1),

        # Consumo atual de energia em Watts
        "consumo_atual": round(random.uniform(500, 4500), 1),

        # Comunicação com a Terra (True = funcionando, False = com falha)
        "comunicacao": random.choices([True, False], weights=[75, 25])[0],

        # Qualidade do sinal de comunicação em percentual
        "qualidade_sinal": round(random.uniform(0, 100), 1),

        # Status de cada módulo da missão
        "modulos": {
            modulo: random.choices(
                ["ativo", "inativo", "falha"],
                weights=[70, 20, 10]
            )[0]
            for modulo in MODULOS
        },

        # Nível de radiação no ambiente externo (mSv/h)
        "radiacao": round(random.uniform(0, 50), 2),

        # Pressão interna da nave (kPa) — normal é ~101 kPa
        "pressao_interna": round(random.uniform(85, 115), 1),

        # Quantidade de combustível restante (%)
        "combustivel": round(random.uniform(0, 100), 1),
    }

    return dados


def gerar_cenario_critico():
    """
    Gera propositalmente um cenário com múltiplos problemas.
    Útil para testar e demonstrar os alertas no vídeo.
    """
    dados = gerar_dados_missao()
    dados["temperatura"] = round(random.uniform(130, 160), 1)   # temperatura perigosa
    dados["energia"] = round(random.uniform(0, 15), 1)          # energia crítica
    dados["comunicacao"] = False                                  # comunicação perdida
    dados["combustivel"] = round(random.uniform(0, 10), 1)      # combustível baixo
    dados["pressao_interna"] = round(random.uniform(85, 90), 1) # pressão baixa
    return dados


def gerar_cenario_normal():
    """
    Gera propositalmente um cenário estável.
    Útil para mostrar o sistema funcionando sem alertas.
    """
    dados = gerar_dados_missao()
    dados["temperatura"] = round(random.uniform(15, 40), 1)
    dados["energia"] = round(random.uniform(70, 100), 1)
    dados["comunicacao"] = True
    dados["qualidade_sinal"] = round(random.uniform(80, 100), 1)
    dados["combustivel"] = round(random.uniform(70, 100), 1)
    dados["pressao_interna"] = round(random.uniform(98, 105), 1)
    return dados
