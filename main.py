# ============================================================
# main.py
# Arquivo PRINCIPAL — ponto de entrada do sistema.
# Orquestra todos os outros módulos: coleta dados,
# gera alertas, toma decisões e exibe na tela.
# ============================================================

import time
from dados_simulados import gerar_dados_missao, gerar_cenario_critico, gerar_cenario_normal
from alertas import gerar_todos_alertas, contar_por_nivel
from decisao import tomar_todas_decisoes, gerar_status_geral
from visualizacao import (
    limpar_tela, exibir_cabecalho, exibir_dados_principais,
    exibir_modulos, exibir_alertas, exibir_acoes,
    exibir_rodape, exibir_resumo_final
)


# ──────────────────────────────────────────────
# CONFIGURAÇÕES DA SESSÃO DE MONITORAMENTO
# Altere esses valores para personalizar a simulação
# ──────────────────────────────────────────────
TOTAL_CICLOS     = 8      # Quantos ciclos de monitoramento executar
INTERVALO_CICLOS = 4      # Segundos entre cada leitura de dados
MODO_DEMO        = True   # True = alterna entre cenários para demonstração


def escolher_cenario(ciclo):
    """
    No modo demonstração, alterna entre cenários diferentes
    para mostrar todas as funcionalidades do sistema.
    """
    if MODO_DEMO:
        if ciclo in [2, 5]:
            return gerar_cenario_critico()    # Força situação crítica
        elif ciclo in [1, 4, 7]:
            return gerar_cenario_normal()     # Força cenário estável
        else:
            return gerar_dados_missao()       # Dados aleatórios
    else:
        return gerar_dados_missao()           # Sempre aleatório


def iniciar_sistema():
    """Exibe a tela de inicialização do sistema."""
    limpar_tela()
    print("=" * 60)
    print()
    print("     🚀  SISTEMA DE MONITORAMENTO ENERGÉTICO ESPACIAL")
    print("         Missão Alpha — Módulo de Controle Inteligente")
    print()
    print("=" * 60)
    print()
    print("  Iniciando subsistemas...")
    time.sleep(1)
    print("  ✅ Módulo de dados simulados       [OK]")
    time.sleep(0.5)
    print("  ✅ Módulo de geração de alertas    [OK]")
    time.sleep(0.5)
    print("  ✅ Módulo de tomada de decisão     [OK]")
    time.sleep(0.5)
    print("  ✅ Módulo de visualização          [OK]")
    time.sleep(0.5)
    print()
    print("  Sistema pronto. Iniciando monitoramento...")
    time.sleep(2)


def executar_monitoramento():
    """
    Função principal de monitoramento.
    Loop que executa cada ciclo: lê dados → analisa → decide → exibe.
    """

    # Inicializa contadores do relatório final
    historico = {"CRITICO": 0, "AVISO": 0, "INFO": 0}

    iniciar_sistema()

    for ciclo in range(1, TOTAL_CICLOS + 1):

        # ── ETAPA 1: Coleta de dados ──────────────────────────
        dados = escolher_cenario(ciclo)

        # ── ETAPA 2: Análise e geração de alertas ────────────
        alertas = gerar_todos_alertas(dados)
        contagem = contar_por_nivel(alertas)

        # Acumula no histórico para o relatório final
        for nivel, qtd in contagem.items():
            historico[nivel] += qtd

        # ── ETAPA 3: Tomada de decisão automatizada ───────────
        acoes = tomar_todas_decisoes(dados, alertas)
        status_geral, _ = gerar_status_geral(alertas)

        # ── ETAPA 4: Visualização ─────────────────────────────
        limpar_tela()
        exibir_cabecalho(ciclo, status_geral)
        exibir_dados_principais(dados)
        exibir_modulos(dados["modulos"])
        exibir_alertas(alertas)
        exibir_acoes(acoes)

        # Não exibe rodapé de "próximo ciclo" no último
        if ciclo < TOTAL_CICLOS:
            exibir_rodape(INTERVALO_CICLOS)
            time.sleep(INTERVALO_CICLOS)
        else:
            print("\n  🏁  Último ciclo concluído.\n")

    # ── ETAPA 5: Relatório final ──────────────────────────────
    exibir_resumo_final(historico, TOTAL_CICLOS)


# ──────────────────────────────────────────────────────────────
# Ponto de entrada: só executa se rodar este arquivo diretamente
# (não quando importado por outro módulo)
# ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    try:
        executar_monitoramento()
    except KeyboardInterrupt:
        print("\n\n  ⏹️  Monitoramento interrompido pelo operador.")
        print("  Sistema encerrado com segurança.\n")
