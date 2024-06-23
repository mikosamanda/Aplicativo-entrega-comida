import os

restaurantes = [{"nome": "Praça", "categoria":"Japonesa","ativo":False},
                {"nome": "Pizza Suprema", "categoria":"Italiana","ativo":True},
                {"nome": "Guaca mole", "categoria":"Mexicana","ativo":True}]


def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    print("""
      𝓢𝓪𝓫𝓸𝓻𝔃𝓲𝓷𝓱𝓸 𝓻𝓪́𝓹𝓲𝓭𝓸
      """)
def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")
def finalizar_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo("Finalizando app")
def voltar_ao_menu_principal():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input("\nDigite uma tecla para voltar a menu principal")
    main()
def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print("Opção invalida!\n")
    voltar_ao_menu_principal()
def exibir_subtitulo(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system("cls")
    linha = "*" * (len(texto)) 
    print(linha)
    print(texto) 
    print(linha)
    print()

def escolher_opcoes():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        opção_escolhida = int(input("Escolha uma opção:"))
        print(F"Você escolheu a opção {opção_escolhida}")

        if opção_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            listar_restaurantes()
        elif opção_escolhida == 3:
            alternar_estado_restaurante()
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo("Cadastrando restaurante")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar:")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}:")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
   
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo("Listanto restaurantes")
    print(f'{"Nome".ljust(23)} | {"Categoria".ljust(20)} | {"Status".ljust(25)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f" - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
   
    voltar_ao_menu_principal()

def  alternar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    exibir_subtitulo("Alternando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()
def main():
    ''' Função principal que inicia o programa '''
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
