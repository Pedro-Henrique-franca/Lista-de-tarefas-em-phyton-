import json
import os

ARQUIVO = "tarefas.json"

def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)

def salvar(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=2)

def adicionar(tarefas):
    nome = input("Tarefa nova: ")
    tarefas.append({"nome": nome, "feito": False})
    salvar(tarefas)

def listar(tarefas):
    for i, t in enumerate(tarefas):
        status = "✔️" if t["feito"] else "❌"
        print(f"{i} - {t['nome']} ({status})")

def concluir(tarefas):
    listar(tarefas)
    n = int(input("Qual tarefa marcar como feita? "))
    tarefas[n]["feito"] = True
    salvar(tarefas)

def main():
    tarefas = carregar()
    while True:
        print("\n1-Adicionar | 2-Listar | 3-Concluir | 4-Sair")
        op = input("> ")
        if op == "1": adicionar(tarefas)
        elif op == "2": listar(tarefas)
        elif op == "3": concluir(tarefas)
        elif op == "4": break

main()
