#Funcionalidades Obrigatórias (O que o sistema deve fazer)

#O sistema deve rodar no terminal através de um menu interativo e permitir:

#Cadastrar Aluno: Guardar nome, idade, turma e uma lista de notas. (Atenção: o sistema deve validar para não aceitar notas menores que 0 ou maiores que 10).

#Listar Alunos: Exibir na tela todos os alunos cadastrados com suas respectivas médias e situação.

#Editar Aluno: Permitir alterar as notas ou dados de um aluno já existente.

#Remover Aluno: Excluir um aluno do sistema.

#Cálculo de Média e Situação: O sistema deve calcular a média aritmética automaticamente e definir o status do aluno: 

#Média maior ou igual a 7.0: Aprovado

#Média entre 5.0 e 6.9: Recuperação

#Média menor que 5.0: Reprovado

# (
# e para eu (igor) nao esquer os riquisitos da recoperacao.
#tem poucos lansamento no github pois so quosiquir botar o codico so acora. 
#descupa si nao tiver muitos lanamento no github .
# e eu jatha vasido um pouco em casa . asinado (igor carlos da silva)
# )


import json

import os

ARQUIVO = "alunos.json"


def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_dados(alunos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)


def calcular_media(notas):
    return sum(notas) / len(notas)


def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def ler_notas():
    notas = []

    quantidade = int(input("Quantidade de notas: "))

    for i in range(quantidade):
        while True:
            nota = float(input(f"Nota {i+1}: "))

            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")

    return notas


def cadastrar(alunos):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    turma = input("Turma: ")
    notas = ler_notas()

    alunos.append({
        "nome": nome,
        "idade": idade,
        "turma": turma,
        "notas": notas
    })

    salvar_dados(alunos)
    print("Aluno cadastrado com sucesso!")


def listar(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n--- LISTA DE ALUNOS ---")

    for i, aluno in enumerate(alunos):
        media = calcular_media(aluno["notas"])
        print(f"\n{i+1}. {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Turma: {aluno['turma']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao(media)}")


def editar(alunos):
    listar(alunos)

    if not alunos:
        return

    indice = int(input("\nNúmero do aluno: ")) - 1

    if 0 <= indice < len(alunos):

        aluno = alunos[indice]

        aluno["nome"] = input(f"Nome ({aluno['nome']}): ") or aluno["nome"]

        idade = input(f"Idade ({aluno['idade']}): ")
        if idade:
            aluno["idade"] = int(idade)

        aluno["turma"] = input(f"Turma ({aluno['turma']}): ") or aluno["turma"]

        alterar = input("Deseja alterar as notas? (s/n): ").lower()

        if alterar == "s":
            aluno["notas"] = ler_notas()

        salvar_dados(alunos)
        print("Aluno atualizado!")

    else:
        print("Aluno não encontrado.")


def remover(alunos):
    listar(alunos)

    if not alunos:
        return

    indice = int(input("\nNúmero do aluno: ")) - 1

    if 0 <= indice < len(alunos):
        removido = alunos.pop(indice)
        salvar_dados(alunos)
        print(f"{removido['nome']} removido com sucesso!")
    else:
        print("Aluno não encontrado.")


def menu():

    alunos = carregar_dados()

    while True:

        print("\n===== MENU =====")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Editar")
        print("4 - Remover")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar(alunos)

        elif opcao == "2":
            listar(alunos)

        elif opcao == "3":
            editar(alunos)

        elif opcao == "4":
            remover(alunos)

        elif opcao == "5":
            print("Encerrando...")
            break

        else:
            print("Opção inválida! Tente novamente.")

menu()

# o código funciona todos os requisitos
# como o sistema deve rodar no terminal através de um menu interativo e permitir cadastrar, listar, editar e remover alunos, além de calcular a média e situação dos alunos.
# o sistema também valida as notas para não aceitar valores menores que 0 ou maiores que 10.
# o sistema salva os dados em um arquivo JSON para persistência.
# o código está organizado em funções para facilitar a manutenção e a leitura.
# o sistema utiliza a biblioteca json para manipulação de arquivos e a biblioteca os para verificar a existência do arquivo.
# fim do código