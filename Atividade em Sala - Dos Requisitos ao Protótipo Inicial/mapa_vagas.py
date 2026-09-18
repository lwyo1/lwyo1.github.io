#Implementa mapa de vagas
class Estacionamento:
    def __init__(self):
        self.vagas = {
            "A1": "livre", "A2": "ocupada", "A3": "livre", "A4": "ocupada",
            "B1": "ocupada", "B2": "livre", "B3": "ocupada", "B4": "livre",
        }
        self.historico = []
        pass

    def contar_livres(self):
        return sum(1 for status in self.vagas.values() if status == "livre")

    def exibir_mapa(self):
        fileiras = {}
        for codigo, status in self.vagas.items():
            fileiras.setdefault(codigo[0], []).append(f"[{codigo}: {status.upper()}]")

        for fileira in sorted(fileiras):
            print(f"Fileira {fileira}: " + " ".join(fileiras[fileira]))
        print(f"Vagas livres: {self.contar_livres()} de {len(self.vagas)}")