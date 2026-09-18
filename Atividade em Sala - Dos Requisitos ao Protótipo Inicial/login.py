import json
import os
from datetime import datetime
from getpass import getpass

ARQUIVO_SESSAO = os.path.join("dados", "sessao.json")


def garantir_login():
    #Retorna o RA do usuário logado. Só pede login se não houver sessão salva.
    if os.path.exists(ARQUIVO_SESSAO):
        with open(ARQUIVO_SESSAO, "r", encoding="utf-8") as f:
            sessao = json.load(f)
        print(f"Sessão encontrada: {sessao['ra']}. Login não necessário.")
        return sessao["ra"]

    print("Necessário realizar seu login!")
    ra = input("RA: ").strip()
    senha = getpass("Senha: ")

    if not ra or not senha:
        raise ValueError("RA e senha não podem ser vazios.")

    os.makedirs("dados", exist_ok=True)
    sessao = {"ra": ra, "login_em": datetime.now().isoformat(timespec="seconds")}
    with open(ARQUIVO_SESSAO, "w", encoding="utf-8") as f:
        json.dump(sessao, f)

    print(f"Login realizado. Sessão salva para {ra}.")
    return ra


def encerrar_sessao():
    #Apaga a sessão (útil para repetir a demonstração do zero).
    if os.path.exists(ARQUIVO_SESSAO):
        os.remove(ARQUIVO_SESSAO)