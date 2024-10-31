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
