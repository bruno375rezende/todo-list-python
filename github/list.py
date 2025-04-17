tarefas = []

def mostrar_menu():
    print("\n--- MENU TO-DO ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append({"descricao": tarefa, "concluida": False})
    print("Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa adicionada.")
        return
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas):
        status = "✔️" if tarefa["concluida"] else "❌"
        print(f"{i+1}. [{status}] {tarefa['descricao']}")

def concluir_tarefa():
    listar_tarefas()
    try:
        i = int(input("Número da tarefa concluída: ")) - 1
        tarefas[i]["concluida"] = True
        print("Tarefa marcada como concluída!")
    except:
        print("Entrada inválida.")

def remover_tarefa():
    listar_tarefas()
    try:
        i = int(input("Número da tarefa a remover: ")) - 1
        tarefa_removida = tarefas.pop(i)
        print(f"Tarefa '{tarefa_removida['descricao']}' removida.")
    except:
        print("Entrada inválida.")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")