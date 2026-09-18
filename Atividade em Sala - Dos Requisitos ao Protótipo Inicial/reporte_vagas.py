from datetime import datetime


def reportar_vaga(estacionamento, vaga, status, usuario):
    vaga = vaga.upper()
    status = status.lower()

    if vaga not in estacionamento.vagas:
        print(f"Erro: a vaga {vaga} não existe.")
        return False
    if status not in ("livre", "ocupada"):
        print("Erro: status deve ser 'livre' ou 'ocupada'.")
        return False

    estacionamento.vagas[vaga] = status
    estacionamento.historico.append({
        "vaga": vaga,
        "status": status,
        "usuario": usuario,
        "quando": datetime.now().isoformat(timespec="seconds"),
    })
    print(f"Usuário {usuario} reportou {vaga} como {status.upper()}.")
    return True

def reportar_interativo(estacionamento, usuario):
    print("\n=== Modo interativo de reporte (deixe a vaga em branco para sair) ===")
    while True:
        estacionamento.exibir_mapa()
        try:
            vaga = input("\nVaga a reportar (ex: A2): ").strip()
            if not vaga:
                break
            status = input("Status (livre/ocupada): ").strip()
        except EOFError:  # sem teclado disponível (execução automática)
            break
        reportar_vaga(estacionamento, vaga, status, usuario)
    print("Saindo do modo de reporte.")