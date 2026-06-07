# ============================================================
# alertas.py
# Responsável por ANALISAR os dados e gerar alertas.
# Funciona como um "médico dos dados": lê os valores e
# diz se algo está fora do normal.
# ============================================================


# Níveis de alerta (usados para classificar a gravidade)
NIVEL_INFO    = "INFO"
NIVEL_AVISO   = "AVISO"
NIVEL_CRITICO = "CRITICO"


def verificar_temperatura(temperatura):
    """Verifica se a temperatura está em níveis seguros."""
    alertas = []

    if temperatura > 120:
        alertas.append({
            "nivel": NIVEL_CRITICO,
            "icone": "🔴",
            "mensagem": f"Temperatura CRÍTICA: {temperatura}°C — Risco de dano aos equipamentos!"
        })
    elif temperatura > 80:
        alertas.append({
            "nivel": NIVEL_AVISO,
            "icone": "🟡",
            "mensagem": f"Temperatura ELEVADA: {temperatura}°C — Monitoramento redobrado necessário."
        })
    elif temperatura < -40:
        alertas.append({
            "nivel": NIVEL_CRITICO,
            "icone": "🔵",
            "mensagem": f"Temperatura MUITO BAIXA: {temperatura}°C — Risco de falha em sistemas eletrônicos!"
        })
    elif temperatura < -10:
        alertas.append({
            "nivel": NIVEL_AVISO,
            "icone": "🟡",
            "mensagem": f"Temperatura baixa: {temperatura}°C — Atenção aos sistemas de aquecimento."
        })

    return alertas


def verificar_energia(energia, potencia_solar, consumo_atual):
    """Verifica o nível de energia e o balanço energético."""
    alertas = []

    if energia < 10:
        alertas.append({
            "nivel": NIVEL_CRITICO,
            "icone": "🔴",
            "mensagem": f"Energia CRÍTICA: {energia}% — Risco de desligamento total da missão!"
        })
    elif energia < 25:
        alertas.append({
            "nivel": NIVEL_AVISO,
            "icone": "🟡",
            "mensagem": f"Energia BAIXA: {energia}% — Reduzir consumo imediatamente."
        })

    # Verifica se está consumindo mais do que gerando (balanço energético negativo)
    if consumo_atual > potencia_solar and energia < 50:
        deficit = round(consumo_atual - potencia_solar, 1)
        alertas.append({
            "nivel": NIVEL_AVISO,
            "icone": "⚡",
            "mensagem": f"Déficit energético de {deficit}W — Consumo supera geração solar."
        })

    return alertas


def verificar_comunicacao(comunicacao, qualidade_sinal):
    """Verifica o status da comunicação com a Terra."""
    alertas = []

    if not comunicacao:
        alertas.append({
            "nivel": NIVEL_CRITICO,
            "icone": "📡",
            "mensagem": "Comunicação com a Terra PERDIDA — Ativando protocolo de emergência."
        })
    elif qualidade_sinal < 30:
        alertas.append({
            "nivel": NIVEL_AVISO,
            "icone": "📶",
            "mensagem": f"Qualidade de sinal FRACA: {qualidade_sinal}% — Risco de perda de comunicação."
        })

    return alertas


def verificar_modulos(modulos):
    """Verifica o status de cada módulo da missão."""
    alertas = []

    for nome, status in modulos.items():
        if status == "falha":
            alertas.append({
                "nivel": NIVEL_CRITICO,
                "icone": "⚙️",
                "mensagem": f"FALHA DETECTADA no {nome} — Intervenção imediata necessária!"
            })
        elif status == "inativo":
            alertas.append({
                "nivel": NIVEL_INFO,
                "icone": "🔘",
                "mensagem": f"{nome} está INATIVO — Verificar se desativação foi intencional."
            })

    return alertas


def verificar_ambiente(radiacao, pressao_interna, combustivel):
    """Verifica condições ambientais e recursos da nave."""
    alertas = []

    if radiacao > 30:
        alertas.append({
            "nivel": NIVEL_CRITICO,
            "icone": "☢️",
            "mensagem": f"Nível de radiação PERIGOSO: {radiacao} mSv/h — Proteger tripulação!"
        })
    elif radiacao > 15:
        alertas.append({
            "nivel": NIVEL_AVISO,
            "icone": "⚠️",
            "mensagem": f"Radiação ELEVADA: {radiacao} mSv/h — Monitorar exposição."
        })

    if pressao_interna < 90:
        alertas.append({
            "nivel": NIVEL_CRITICO,
            "icone": "💨",
            "mensagem": f"Pressão interna CRÍTICA: {pressao_interna} kPa — Verificar vazamentos!"
        })
    elif pressao_interna < 95:
        alertas.append({
            "nivel": NIVEL_AVISO,
            "icone": "💨",
            "mensagem": f"Pressão interna BAIXA: {pressao_interna} kPa — Inspecionar vedações."
        })

    if combustivel < 15:
        alertas.append({
            "nivel": NIVEL_CRITICO,
            "icone": "🛢️",
            "mensagem": f"Combustível CRÍTICO: {combustivel}% — Avaliar retorno imediato!"
        })
    elif combustivel < 30:
        alertas.append({
            "nivel": NIVEL_AVISO,
            "icone": "🛢️",
            "mensagem": f"Combustível BAIXO: {combustivel}% — Planejar reabastecimento."
        })

    return alertas


def gerar_todos_alertas(dados):
    """
    Função principal: chama todas as verificações e retorna
    uma lista unificada de alertas, ordenada por gravidade.
    """
    todos_alertas = []

    todos_alertas += verificar_temperatura(dados["temperatura"])
    todos_alertas += verificar_energia(dados["energia"], dados["potencia_solar"], dados["consumo_atual"])
    todos_alertas += verificar_comunicacao(dados["comunicacao"], dados["qualidade_sinal"])
    todos_alertas += verificar_modulos(dados["modulos"])
    todos_alertas += verificar_ambiente(dados["radiacao"], dados["pressao_interna"], dados["combustivel"])

    # Ordena: CRITICO primeiro, depois AVISO, depois INFO
    ordem = {NIVEL_CRITICO: 0, NIVEL_AVISO: 1, NIVEL_INFO: 2}
    todos_alertas.sort(key=lambda a: ordem.get(a["nivel"], 3))

    return todos_alertas


def contar_por_nivel(alertas):
    """Retorna um resumo com a contagem de alertas por nível."""
    return {
        NIVEL_CRITICO: sum(1 for a in alertas if a["nivel"] == NIVEL_CRITICO),
        NIVEL_AVISO:   sum(1 for a in alertas if a["nivel"] == NIVEL_AVISO),
        NIVEL_INFO:    sum(1 for a in alertas if a["nivel"] == NIVEL_INFO),
    }
