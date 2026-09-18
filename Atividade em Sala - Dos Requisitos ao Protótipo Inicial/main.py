import sys
from login import garantir_login, encerrar_sessao
from mapa_vagas import Estacionamento
from reporte_vagas import reportar_vaga, reportar_interativo

if "--sair" in sys.argv:
    encerrar_sessao()
    print("Sessão encerrada.")
    sys.exit()

print("=== R3: Login único ===")
usuario = garantir_login()

estacionamento = Estacionamento()

print("\n=== R1: Mapa de vagas ===")
estacionamento.exibir_mapa()

print("\n=== R2: Reporte manual ===")
reportar_vaga(estacionamento, "A2", "livre", usuario)
reportar_vaga(estacionamento, "Z9", "livre", usuario)  # vaga inexistente: erro tratado
print("\nMapa visto por outro usuário (aluno2):")
estacionamento.exibir_mapa()

if "--interativo" in sys.argv:
    reportar_interativo(estacionamento, usuario)