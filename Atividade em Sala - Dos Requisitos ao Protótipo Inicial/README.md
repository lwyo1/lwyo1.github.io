# Protótipo: App de Vagas de Estacionamento
Aluno: Luiz Bonfá dos Santos (RA a2669609)
Protótipo em Python, via linha de comando, que simula um app para consultar e atualizar vagas de um estacionamento.
Requisitos cobertos (lista completa em REQUISITOS.md):
- R3, Login único: pede RA e senha só na primeira vez e reaproveita a sessão salva (login.py).
- R1, Mapa de vagas: mostra vagas livres e ocupadas e o total disponível (mapa_vagas.py).
- R2, Reporte manual: um usuário altera o status de uma vaga e outro usuário vê a mudança (reporte_vagas.py).
Como executar: `python main.py` (Python 3.8+, sem dependências). Rode duas vezes para ver o login reaproveitado; apague `dados/sessao.json` para repetir o primeiro login.