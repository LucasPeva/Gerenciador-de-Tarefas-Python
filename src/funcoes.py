# Funcção: Adicionar tarefa
# Adiciona uma tarefa nova a partir dos argumentos entreges

def adicionarTarefa(tarefas, descricao, prazo, prioridade):
    tarefa = {
        'descricao': descricao,
        'prazo': prazo,
        'prioridade': prioridade,
        'concluida': False
    }
    tarefas.append(tarefa)

# Função: Marcar tarefa como concluída
# Atualiza a condição de conclusão da tarefa na lista

def marcarConcluida(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True
    else:
        print("Índice inválido.")

# Função: Listar tarefas concluidas
# Lista as tarefas que tem a bool 'concluida' = True

def listarTarefasConcluidas(tarefas):
    print("\nTarefas Concluídas:")
    for i, tarefa in enumerate(tarefas):
        if tarefa['concluida']:
            print(f"{i}: {tarefa['descricao']} (Prazo: {tarefa['prazo']}, Prioridade: {tarefa['prioridade']})")

