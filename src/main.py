# Importa as funções necessárias para o programa, usa o wildcard pra manter os nomes
# do arquivo funcoes.py
from funcoes import *

print('Gerenciador de tarefas em python.')
print('Bem vindo!')

def main():
    
    # Variaveis globais
    tarefas = {} # Placeholder pra armazenar as tarefas, talvez dá um erro insano

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar Tarefa")
        print("2. Marcar Tarefa como Concluída")
        print("3. Listar Tarefas Pendentes")
        print("4. Listar Tarefas Concluídas")
        print("5. Remover Tarefa")
        print("6. Filtrar Tarefas por Prioridade")
        print("7. Sair")

        try:
            opcao = int(input("> "))
        
            if opcao == '1':
                descricao = input("Descrição da tarefa: ")
                prazo = input("Prazo (YYYY-MM-DD): ")
                prioridade = input("Prioridade (alta, média, baixa): ")
                adicionarTarefa(tarefas, descricao, prazo, prioridade)

            elif opcao == '2':
                indice = int(input("Índice da tarefa a ser marcada como concluída: "))
                marcarConcluida(tarefas, indice)

            elif opcao == '3':
                listarTarefasPendentes(tarefas)

            elif opcao == '4':
                listarTarefasConcluidas(tarefas)

            elif opcao == '5':
                print('Tarefa removida')

            elif opcao == '6':
                print('Tarefas filtradas por prioridade')

            elif opcao == '7':
                print('Programa encerrado.')
                break

            else:
                print('ERRO: Opção inválida. Tente novamente.')

        except ValueError:
            print('ERRO: Opção inválida. Tente novamente.')

        except KeyboardInterrupt:
            print('Programa encerrado.')
            break

if __name__ == '__main__':
    main()