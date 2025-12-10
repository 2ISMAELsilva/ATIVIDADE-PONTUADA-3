# ANTONIO ISMAEL DA SILVA CERQUEIRA
# ANDRÉ CONCEIÇÃO DOS SANTOS

import os
from dataclasses import dataclass

os.system('cls || clear')

# LISTAS
lista_avioes = []
lista_reservas = []
LIMITE_RESERVAS = 10

# CLASSES

@dataclass
class Aviao:
    numero: str
    assentos: int

    def mostrar_dados_aviao(self):
        print(f"Número do Avião: {self.numero}")
        print(f"Assentos Disponíveis: {self.assentos}")

@dataclass
class Reserva:
    numero_aviao: str
    nome_passageiro: str

    def mostrar_dados_reserva(self):
        print(f"Avião: {self.numero_aviao}")
        print(f"Passageiro: {self.nome_passageiro}")


# FUNÇÕES AUXILIARES

def verificar_lista_vazia_avioes(lista):
    if not lista:
        print("\n Não há aviões cadastrados.")
        return True
    return False

def verificar_lista_vazia_reservas(lista):
    if not lista:
        print("\n Não há reservas cadastradas.")
        return True
    return False


# FUNÇÕES AVIÕES 

def adicionar_aviao(lista):
    print("\n---- Cadastrar Avião ----")
    numero = input("Número do Avião: ")
    assentos = int(input("Quantidade de Assentos: "))

    aviao = Aviao(numero, assentos)
    lista.append(aviao)

    print(f"\nAvião {numero} cadastrado com sucesso!\n")


def listar_avioes(lista):
    print("\n--- Lista de Aviões Cadastrados ---")
    if verificar_lista_vazia_avioes(lista):
        return

    for aviao in lista:
        print("\n------------------------------------")
        aviao.mostrar_dados_aviao()
    print("------------------------------------\n")


def buscar_aviao(lista, numero):
    for aviao in lista:
        if aviao.numero == numero:
            return aviao
    return None


def atualizar_aviao(lista):
    print("\n--- Atualizar Avião ---")
    numero = input("Digite o número do avião: ")

    aviao = buscar_aviao(lista, numero)

    if aviao is None:
        print(" Avião não encontrado!")
        return

    print("\nDeixe em branco para manter o valor atual.")

    novo_numero = input(f"Número ({aviao.numero}): ") or aviao.numero
    novos_assentos = input(f"Assentos ({aviao.assentos}): ") or aviao.assentos

    aviao.numero = novo_numero
    aviao.assentos = int(novos_assentos)

    print("\nDados do avião atualizados com sucesso!\n")


def excluir_aviao(lista):
    print("\n--- Excluir Avião ---")
    numero = input("Digite o número do avião: ")

    aviao = buscar_aviao(lista, numero)

    if aviao is None:
        print(" Avião não encontrado!")
        return

    lista.remove(aviao)
    print("\n✔ Avião removido com sucesso!\n")


# FUNÇÕES RESERVAS 

def adicionar_reserva():
    print("\n---- Reservar Passagem ----")

    if len(lista_reservas) >= LIMITE_RESERVAS:
        print(" LIMITE DE 10 RESERVAS ATINGIDO!")
        return

    numero_aviao = input("Número do avião: ")

    aviao = buscar_aviao(lista_avioes, numero_aviao)
    if aviao is None:
        print(" Avião não existe!")
        return

    if aviao.assentos <= 0:
        print(" Não há assentos disponíveis!")
        return

    nome = input("Nome do passageiro: ")

    reserva = Reserva(numero_aviao, nome)
    lista_reservas.append(reserva)

    aviao.assentos -= 1

    print("\n Reserva realizada com sucesso!\n")


def listar_reservas(lista):
    print("\n--- Lista de Reservas Cadastradas ---")
    if verificar_lista_vazia_reservas(lista):
        return

    for reserva in lista:
        print("\n------------------------------------")
        reserva.mostrar_dados_reserva()
    print("------------------------------------\n")


def buscar_reservas_por_passageiro(nome):
    return [r for r in lista_reservas if r.nome_passageiro.lower() == nome.lower()]


def buscar_reservas_por_aviao(numero):
    return [r for r in lista_reservas if r.numero_aviao == numero]


def consultar_reserva_passageiro():
    print("\n--- Consultar Reservas por Passageiro ---")
    nome = input("Nome do passageiro: ")

    achados = buscar_reservas_por_passageiro(nome)

    if not achados:
        print(" Nenhuma reserva encontrada!")
        return

    print("\nReservas encontradas:")
    for r in achados:
        print("\n------------------------------------")
        r.mostrar_dados_reserva()
    print("------------------------------------\n")


def consultar_reserva_aviao():
    print("\n--- Consultar Reservas por Avião ---")
    numero = input("Número do avião: ")

    achados = buscar_reservas_por_aviao(numero)

    if not achados:
        print(" Nenhuma reserva para este avião!")
        return

    print("\nReservas encontradas:")
    for r in achados:
        print("\n------------------------------------")
        r.mostrar_dados_reserva()
    print("------------------------------------\n")


# MENUS ------------------------------------------------------------

def menu_avioes():
    print("\n=========== SISTEMA DE AVIÕES ===========")
    print("1 - Adicionar Avião")
    print("2 - Listar Aviões")
    print("3 - Atualizar Avião")
    print("4 - Excluir Avião")
    print("5 - Sair")
    print("=============================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_aviao(lista_avioes)
    elif opcao == "2":
        listar_avioes(lista_avioes)
    elif opcao == "3":
        atualizar_aviao(lista_avioes)
    elif opcao == "4":
        excluir_aviao(lista_avioes)
    elif opcao == "5":
        print("Voltando ao menu principal...")
    else:
        print("❗ Opção inválida!")


def menu_reservas():
    print("\n=========== SISTEMA DE RESERVAS ===========")
    print("1 - Fazer Reserva")
    print("2 - Listar Reservas")
    print("3 - Consultar por Passageiro")
    print("4 - Consultar por Avião")
    print("5 - Sair")
    print("===============================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_reserva()
    elif opcao == "2":
        listar_reservas(lista_reservas)
    elif opcao == "3":
        consultar_reserva_passageiro()
    elif opcao == "4":
        consultar_reserva_aviao()
    elif opcao == "5":
        print("Voltando ao menu principal...")
    else:
        print(" Opção inválida!")


# EXECUÇÃO ---------------------------------------------------------

while True:
    print("\n=========== SWEET FLIGHT ===========")
    print("1 - Menu Aviões")
    print("2 - Menu Reservas")
    print("3 - Sair")
    print("=======================================")

    op = input("Escolha: ")

    if op == "1":
        menu_avioes()
    elif op == "2":
        menu_reservas()
    elif op == "3":
        print("Encerrando o sistema...")
        break
    else:
        print(" Opção inválida!")
