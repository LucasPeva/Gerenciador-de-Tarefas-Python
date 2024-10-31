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

# Função: Listar tarefas pendentes
# Lista as tarefas que tem a bool 'concluida' = False
# Tá fora de ordem do main() pq eu fiz na ordem errada, ops

def listarTarefasPendentes(tarefas):
    print("\nTarefas Concluídas:")
    for i, tarefa in enumerate(tarefas):
        if not tarefa['concluida']:
            print(f"{i}: {tarefa['descricao']} (Prazo: {tarefa['prazo']}, Prioridade: {tarefa['prioridade']})")

# Função: Remove uma tarefa
# Pois é, isso mesmo

def removerTarefa(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
    else:
        print("Índice inválido.")
        
# Função para filtrar tarefas por prioridade
# Recebe a prioridade e retorna as que tem prioridade igual

def filtrarTarefasPorPrioridade(tarefas, prioridade):
    print(f"\nTarefas com prioridade {prioridade}:")
    for i, tarefa in enumerate(tarefas):
        if tarefa['prioridade'] == prioridade:
            print(f"{i}: {tarefa['descricao']} (Prazo: {tarefa['prazo']}, Concluída: {'Sim' if tarefa['concluida'] else 'Não'})")