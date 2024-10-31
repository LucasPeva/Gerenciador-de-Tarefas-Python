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

def marcar_concluida(tarefas, indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True
    else:
        print("Índice inválido.")
