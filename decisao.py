# ============================================================
# decisao.py
# Responsável pela TOMADA DE DECISÃO AUTOMATIZADA.
# É o "cérebro" do sistema: diante de alertas, ele age.
# Simula respostas inteligentes sem intervenção humana.
# ============================================================

from alertas import NIVEL_CRITICO, NIVEL_AVISO


def decidir_sobre_energia(dados, alertas):
    """
    Se a energia estiver crítica, o sistema decide quais
    módulos desligar para preservar os essenciais.
    """
    acoes = []

    if dados["energia"] < 10:
        acoes.append({
            "prioridade": "URGENTE",
            "acao": "🔌 Desligando módulos não essenciais (entretenimento, pesquisa secundária).",
            "motivo": f"Energia em {dados['energia']}% — abaixo do limite crítico de 10%."
        })
        acoes.append({
            "prioridade": "URGENTE",
            "acao": "🔆 Redirecionando toda energia para: suporte à vida, comunicação e propulsão.",
            "motivo": "Protocolo de emergência energética ativado."
        })

    elif dados["energia"] < 25:
        acoes.append({
            "prioridade": "ALTA",
            "acao": "💡 Reduzindo iluminação interna ao mínimo operacional.",
            "motivo": f"Energia em {dados['energia']}% — modo de economia ativado."
        })

    # Verifica se os painéis solares estão gerando o suficiente
    if dados["potencia_solar"] < dados["consumo_atual"] * 0.5:
        acoes.append({
            "prioridade": "ALTA",
            "acao": "🔄 Reorientando painéis solares para maximizar captação de energia.",
            "motivo": f"Geração solar ({dados['potencia_solar']}W) muito abaixo do consumo ({dados['consumo_atual']}W)."
        })

    return acoes


def decidir_sobre_temperatura(dados):
    """Ações automáticas para controle térmico da nave."""
    acoes = []

    if dados["temperatura"] > 120:
        acoes.append({
            "prioridade": "URGENTE",
            "acao": "❄️ Ativando sistema de resfriamento de emergência (nível máximo).",
            "motivo": f"Temperatura em {dados['temperatura']}°C — limite crítico ultrapassado."
        })
        acoes.append({
            "prioridade": "URGENTE",
            "acao": "🛡️ Ativando escudos térmicos adicionais nos painéis eletrônicos.",
            "motivo": "Proteção de hardware crítico contra superaquecimento."
        })

    elif dados["temperatura"] > 80:
        acoes.append({
            "prioridade": "ALTA",
            "acao": "❄️ Aumentando ventilação interna e ativando resfriamento passivo.",
            "motivo": f"Temperatura em {dados['temperatura']}°C — zona de atenção."
        })

    elif dados["temperatura"] < -40:
        acoes.append({
            "prioridade": "URGENTE",
            "acao": "🔥 Ativando aquecedores de emergência nos compartimentos críticos.",
            "motivo": f"Temperatura em {dados['temperatura']}°C — risco de congelamento de sistemas."
        })

    return acoes


def decidir_sobre_comunicacao(dados):
    """Ações para restaurar ou proteger a comunicação."""
    acoes = []

    if not dados["comunicacao"]:
        acoes.append({
            "prioridade": "URGENTE",
            "acao": "📡 Iniciando varredura de frequências para localizar sinal da Terra.",
            "motivo": "Comunicação completamente perdida."
        })
        acoes.append({
            "prioridade": "URGENTE",
            "acao": "🔁 Reiniciando módulo de comunicação (tentativa 1 de 3).",
            "motivo": "Protocolo de recuperação de comunicação ativado."
        })

    elif dados["qualidade_sinal"] < 30:
        acoes.append({
            "prioridade": "ALTA",
            "acao": "📡 Reposicionando antena direcional para melhorar qualidade do sinal.",
            "motivo": f"Qualidade do sinal em {dados['qualidade_sinal']}%."
        })

    return acoes


def decidir_sobre_modulos(dados):
    """Ações de resposta para falhas nos módulos."""
    acoes = []

    for nome, status in dados["modulos"].items():
        if status == "falha":
            acoes.append({
                "prioridade": "URGENTE",
                "acao": f"🔧 Iniciando diagnóstico automático do {nome}.",
                "motivo": f"{nome} reportou falha crítica."
            })
            # Se o módulo solar falhou, precisa compensar com outros
            if "Solar" in nome:
                acoes.append({
                    "prioridade": "ALTA",
                    "acao": f"⚡ Redistribuindo carga energética dos demais painéis solares.",
                    "motivo": f"Compensando perda de geração do {nome}."
                })

    return acoes


def decidir_sobre_combustivel(dados):
    """Ações relacionadas ao nível de combustível."""
    acoes = []

    if dados["combustivel"] < 15:
        acoes.append({
            "prioridade": "URGENTE",
            "acao": "🚀 Calculando rota de retorno de emergência à base.",
            "motivo": f"Combustível em {dados['combustivel']}% — missão em risco."
        })
        acoes.append({
            "prioridade": "URGENTE",
            "acao": "📋 Notificando centro de controle sobre situação crítica de combustível.",
            "motivo": "Protocolo de emergência de recursos ativado."
        })

    return acoes


def tomar_todas_decisoes(dados, alertas):
    """
    Função principal: consolida todas as decisões em uma lista
    ordenada por prioridade (URGENTE primeiro).
    """
    todas_acoes = []

    todas_acoes += decidir_sobre_energia(dados, alertas)
    todas_acoes += decidir_sobre_temperatura(dados)
    todas_acoes += decidir_sobre_comunicacao(dados)
    todas_acoes += decidir_sobre_modulos(dados)
    todas_acoes += decidir_sobre_combustivel(dados)

    # Ordena por prioridade (URGENTE antes de ALTA)
    ordem = {"URGENTE": 0, "ALTA": 1, "MEDIA": 2}
    todas_acoes.sort(key=lambda a: ordem.get(a["prioridade"], 3))

    return todas_acoes


def gerar_status_geral(alertas):
    """
    Com base nos alertas, determina o status geral da missão.
    Retorna um texto e um ícone representativos.
    """
    criticos = sum(1 for a in alertas if a["nivel"] == "CRITICO")
    avisos   = sum(1 for a in alertas if a["nivel"] == "AVISO")

    if criticos > 0:
        return "🔴 SITUAÇÃO CRÍTICA", criticos
    elif avisos > 0:
        return "🟡 ATENÇÃO NECESSÁRIA", avisos
    else:
        return "🟢 MISSÃO ESTÁVEL", 0
