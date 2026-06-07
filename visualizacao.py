# ============================================================
# visualizacao.py
# Responsável por EXIBIR todas as informações na tela.
# Separa a lógica de exibição do restante do código —
# boa prática de programação (princípio da responsabilidade única).
# ============================================================

import os
from datetime import datetime
from alertas import NIVEL_CRITICO, NIVEL_AVISO, NIVEL_INFO


def limpar_tela():
    """Limpa o terminal para uma exibição mais organizada."""
    os.system('cls' if os.name == 'nt' else 'clear')


def linha(char="=", tamanho=60):
    """Retorna uma linha divisória estilizada."""
    return char * tamanho


def exibir_cabecalho(ciclo, status_geral):
    """Exibe o cabeçalho do painel com status geral da missão."""
    agora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")

    print(linha())
    print("  🛸  SISTEMA DE MONITORAMENTO — MISSÃO ESPACIAL ALPHA")
    print(linha())
    print(f"  📅 Data/Hora:     {agora}")
    print(f"  🔄 Ciclo Atual:   #{ciclo}")
    print(f"  📊 Status Geral:  {status_geral}")
    print(linha())


def exibir_dados_principais(dados):
    """Exibe o painel principal com todos os dados da missão."""
    print("\n  ┌─────────────────────────────────────────────────┐")
    print("  │             📋 DADOS DA MISSÃO                  │")
    print("  ├─────────────────────────────────────────────────┤")

    # Temperatura com indicador visual
    temp = dados["temperatura"]
    temp_icon = "🔴" if temp > 120 or temp < -40 else "🟡" if temp > 80 or temp < -10 else "🟢"
    print(f"  │  🌡️  Temperatura:       {temp:>8.1f} °C      {temp_icon}     │")

    # Energia com barra de progresso
    energia = dados["energia"]
    energia_icon = "🔴" if energia < 10 else "🟡" if energia < 25 else "🟢"
    barra_energia = gerar_barra_progresso(energia)
    print(f"  │  ⚡  Energia:          {energia:>7.1f} %  {barra_energia} {energia_icon}  │")

    # Geração e consumo solar
    print(f"  │  ☀️  Geração Solar:    {dados['potencia_solar']:>8.1f} W              │")
    print(f"  │  🔌  Consumo Atual:   {dados['consumo_atual']:>8.1f} W              │")

    # Comunicação
    com_status = "✅ ATIVA " if dados["comunicacao"] else "❌ FALHA "
    print(f"  │  📡  Comunicação:      {com_status}  ({dados['qualidade_sinal']:.0f}% sinal)     │")

    # Pressão interna
    pressao = dados["pressao_interna"]
    pressao_icon = "🔴" if pressao < 90 else "🟡" if pressao < 95 else "🟢"
    print(f"  │  💨  Pressão Interna: {pressao:>7.1f} kPa               {pressao_icon}  │")

    # Radiação
    rad = dados["radiacao"]
    rad_icon = "🔴" if rad > 30 else "🟡" if rad > 15 else "🟢"
    print(f"  │  ☢️  Radiação:        {rad:>8.2f} mSv/h           {rad_icon}  │")

    # Combustível
    comb = dados["combustivel"]
    comb_icon = "🔴" if comb < 15 else "🟡" if comb < 30 else "🟢"
    barra_comb = gerar_barra_progresso(comb)
    print(f"  │  🛢️  Combustível:      {comb:>7.1f} %  {barra_comb} {comb_icon}  │")

    print("  └─────────────────────────────────────────────────┘")


def gerar_barra_progresso(percentual, tamanho=8):
    """Gera uma barra visual de progresso em texto."""
    preenchido = int((percentual / 100) * tamanho)
    vazio = tamanho - preenchido
    return f"[{'█' * preenchido}{'░' * vazio}]"


def exibir_modulos(modulos):
    """Exibe o status de cada módulo da missão."""
    print("\n  ┌─────────────────────────────────────────────────┐")
    print("  │             ⚙️  STATUS DOS MÓDULOS               │")
    print("  ├─────────────────────────────────────────────────┤")

    icones_status = {
        "ativo":   "🟢 ATIVO   ",
        "inativo": "⚪ INATIVO ",
        "falha":   "🔴 FALHA   "
    }

    for nome, status in modulos.items():
        icone = icones_status.get(status, "❓")
        # Trunca o nome para manter alinhamento
        nome_fmt = nome[:25].ljust(26)
        print(f"  │  {icone}  {nome_fmt}     │")

    print("  └─────────────────────────────────────────────────┘")


def exibir_alertas(alertas):
    """Exibe todos os alertas gerados pelo sistema."""
    if not alertas:
        print("\n  ✅  Nenhum alerta detectado — todos os sistemas operam normalmente.\n")
        return

    print(f"\n  ┌─────────────────────────────────────────────────┐")
    print(f"  │        ⚠️  ALERTAS ATIVOS ({len(alertas)} detectados)           │")
    print(f"  ├─────────────────────────────────────────────────┤")

    for alerta in alertas:
        nivel = alerta["nivel"]
        prefixo = "  [CRÍTICO]" if nivel == NIVEL_CRITICO else "  [ AVISO ]" if nivel == NIVEL_AVISO else "  [  INFO ]"
        print(f"{prefixo} {alerta['icone']} {alerta['mensagem']}")

    print(f"  └─────────────────────────────────────────────────┘")


def exibir_acoes(acoes):
    """Exibe as ações automáticas que o sistema está tomando."""
    if not acoes:
        print("  🤖  Nenhuma ação automática necessária no momento.\n")
        return

    print(f"\n  ┌─────────────────────────────────────────────────┐")
    print(f"  │      🤖  AÇÕES AUTOMÁTICAS ({len(acoes)} em execução)        │")
    print(f"  ├─────────────────────────────────────────────────┤")

    for acao in acoes:
        print(f"  [{acao['prioridade']:<7}] {acao['acao']}")
        print(f"            ↳ Motivo: {acao['motivo']}")

    print(f"  └─────────────────────────────────────────────────┘")


def exibir_rodape(proximo_ciclo):
    """Exibe o rodapé com informações do próximo ciclo."""
    print(linha("-"))
    print(f"  ⏱️  Próxima leitura em {proximo_ciclo} segundos...  |  Pressione CTRL+C para encerrar")
    print(linha("-"))


def exibir_resumo_final(historico_alertas, total_ciclos):
    """Exibe um resumo ao final de todos os ciclos."""
    print("\n")
    print(linha("*"))
    print("  📊  RELATÓRIO FINAL DA SESSÃO DE MONITORAMENTO")
    print(linha("*"))
    print(f"  Total de ciclos executados:  {total_ciclos}")
    print(f"  Total de alertas críticos:   {historico_alertas['CRITICO']}")
    print(f"  Total de avisos gerados:     {historico_alertas['AVISO']}")
    print(f"  Total de informações:        {historico_alertas['INFO']}")
    print(linha("*"))
    print("  Missão encerrada. Dados registrados com sucesso.")
    print(linha("*"))
