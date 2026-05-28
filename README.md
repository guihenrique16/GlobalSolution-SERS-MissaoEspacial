# Sistema de Monitoramento Energético Espacial — Missão Alpha

> **Global Solution — Ciência da Computação | FIAP**  
> Tema: Soluções em Energias Renováveis e Sustentáveis aplicadas à Missão Espacial Experimental

---

## Descrição do Projeto

Este projeto implementa um **sistema inteligente de monitoramento** para controle operacional de uma missão espacial simulada. A solução interpreta dados em tempo real de sensores virtuais, detecta situações críticas automaticamente e toma decisões corretivas sem intervenção humana.

A proposta conecta conceitos de **energias renováveis** (geração solar, balanço energético) com **tecnologia computacional aplicada**, simulando desafios reais enfrentados por engenheiros de sistemas espaciais modernos.

---

## Funcionalidades Implementadas

| Funcionalidade | Descrição |
|---|---|
| - Monitoramento em tempo real | Temperatura, energia, comunicação, pressão, radiação e combustível |
| - Balanço energético | Comparação entre geração solar e consumo da nave |
| - Geração de alertas | 3 níveis: CRÍTICO 🔴, AVISO 🟡 e INFO ⚪ |
| - Tomada de decisão | Ações automáticas proporcionais à gravidade de cada situação |
| - Visualização organizada | Painel com barras de progresso, ícones e indicadores visuais |
| - Relatório final | Resumo consolidado de alertas ao término da sessão |

---

## Estrutura do Projeto

```
missao_espacial/
│
├── main.py               # Orquestrador principal — ponto de entrada
├── dados_simulados.py    # Geração dos dados simulados da missão
├── alertas.py            # Análise de dados e geração de alertas
├── decisao.py            # Tomada de decisão automatizada
├── visualizacao.py       # Exibição organizada dos dados no terminal
└── README.md             # Documentação do projeto
```

### Responsabilidade de cada arquivo

- **`dados_simulados.py`** — Simula os sensores da nave, gerando valores aleatórios realistas para cada parâmetro. Inclui cenários forçados (crítico e normal) para fins de demonstração.

- **`alertas.py`** — Age como um "monitor inteligente": recebe os dados e verifica cada parâmetro contra limites definidos, retornando alertas classificados por gravidade.

- **`decisao.py`** — Interpreta os alertas e gera ações corretivas automáticas — como acionar resfriamento de emergência, redistribuir energia ou calcular rota de retorno.

- **`visualizacao.py`** — Responsável pela interface visual no terminal: painel de dados, barra de progresso, listagem de alertas e ações.

- **`main.py`** — Conecta todos os módulos e executa o loop de monitoramento com intervalo configurável entre ciclos.

---

## Conceitos de Energia Aplicados

O sistema aplica diretamente conceitos de energias renováveis e sustentabilidade:

- **Geração solar** — O módulo rastreia a potência gerada pelos painéis solares em Watts
- **Balanço energético** — Compara geração vs. consumo, alertando sobre déficits
- **Eficiência energética** — Em situações críticas, o sistema prioriza e desliga módulos não essenciais
- **Sustentabilidade da missão** — Combustível e energia são recursos monitorados para garantir a viabilidade contínua da operação

---

## Como Executar

### Pré-requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa — usa apenas módulos da biblioteca padrão do Python (`random`, `time`, `os`, `datetime`)

### Executando o projeto

```bash
# 1. Clone o repositório
git clone https://github.com/SEU-USUARIO/missao-espacial-alpha.git

# 2. Entre na pasta do projeto
cd missao-espacial-alpha

# 3. Execute o programa principal
python main.py
```

### Configurações disponíveis (em `main.py`)

```python
TOTAL_CICLOS     = 8      # Número de ciclos de monitoramento
INTERVALO_CICLOS = 4      # Segundos entre cada leitura
MODO_DEMO        = True   # Alterna entre cenários para demonstração
```

---

## Exemplos de Saída

### Situação Normal 🟢
```
============================================================
 SISTEMA DE MONITORAMENTO — MISSÃO ESPACIAL ALPHA
============================================================
   Data/Hora:     28/05/2026  14:30:00
   Ciclo Atual:   #3
   Status Geral:  🟢 MISSÃO ESTÁVEL

    Temperatura:        22.5 °C     🟢
    Energia:            85.0 %  [██████░░] 🟢
    Comunicação:      ATIVA  (92% sinal)

  ✅  Nenhum alerta — todos os sistemas operam normalmente.
```

### Situação Crítica 🔴
```
   Status Geral:  🔴 SITUAÇÃO CRÍTICA

    Temperatura:       148.3 °C     🔴
    Energia:             8.1 %  [░░░░░░░░] 🔴

  [CRÍTICO] 🔴 Temperatura CRÍTICA: 148.3°C — Risco de dano aos equipamentos!
  [CRÍTICO] 🔴 Energia CRÍTICA: 8.1% — Risco de desligamento total!

  [URGENTE]  Ativando sistema de resfriamento de emergência.
  [URGENTE]  Desligando módulos não essenciais.
```

---

## Arquitetura da Solução

```
Dados Simulados ──▶ Análise de Alertas ──▶ Tomada de Decisão ──▶ Visualização
(dados_simulados)     (alertas.py)           (decisao.py)        (visualizacao.py)
        └──────────────────────────────────────────────────────▶ Relatório Final
```

O fluxo segue o padrão **ETL adaptado**: Extração (dados) → Transformação (alertas + decisões) → Carregamento (visualização).

---

## Parâmetros Monitorados e Limites

| Parâmetro | Aviso | Crítico |
|---|---|---|
| Temperatura | > 80°C ou < -10°C | > 120°C ou < -40°C |
| Energia | < 25% | < 10% |
| Qualidade do sinal | < 30% | Comunicação perdida |
| Radiação | > 15 mSv/h | > 30 mSv/h |
| Pressão interna | < 95 kPa | < 90 kPa |
| Combustível | < 30% | < 15% |

---

## Integrantes do Grupo

| Nome Completo | RM |
|---|---|
| [Nome do Integrante 1] | [RM] |
| [Nome do Integrante 2] | [RM] |
| [Nome do Integrante 3] | [RM] |

---

## Vídeo de Demonstração

 [Assistir no YouTube](https://youtu.be/SEU-LINK-AQUI)

---

## Entregáveis

- [x] Repositório público no GitHub com código-fonte
- [x] README organizado com documentação completa
- [x] Vídeo demonstrativo no YouTube (não listado, até 3 min)
- [x] Arquivo `.txt` de entrega com nomes e links

---

*Projeto desenvolvido para a Global Solution — FIAP, 2025.*  
*Ciência da Computação — Turmas 1CC*
