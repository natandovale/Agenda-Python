'''Variavel global'''
AGENDA={}




def mostrar_contatos():
    try:
        with open('database.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome = linha.strip().split(',')[0]
                telefone = linha.strip().split(',')[1]
                email = linha.strip().split(',')[2]
                endereco = linha.strip().split(',')[3]
                print('Nome:{}\nTelefone:{}\nEmail:{}\nEndereço:{}\n'.format(nome,telefone,email,endereco))
    except Exception as error:
        print(error)

def buscar_contato(contato):
    try:
        with open('database.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                if contato == linha.strip().split(',')[0]:
                    print("Ela existe")
                else:
                    print("Contato não existente!")
                
    except keyErrors:
        print()
        print('>>>>>>contato inexistente')
    except Exception as error:
        print('Erro inesperado ocorreu')
        print(error)
    
def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
    'telefone': telefone,
    'email': email,
    'endereco': endereco
    }
    salvar()
    print('>>>>>>Contato {} adicionado com sucesso!'.format(contato))
    

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print('>>>>>>Contato {} excluido com sucesso!'.format(contato))
        print()
    except keyErrors:
        print()
        print('>>>>>>contato inexistente')
    except Exception as error:
        print('Erro inesperado ocorreu')
        print(error)
        
def exportar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'a') as arquivo:
            
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato,telefone,email,endereco))
        print('>>>>>>Agenda exportada com sucesso')
    except:
        print('>>>>>>Algum erro ocorreu ao exportar contatos')
        
def importar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.strip().split(','))
    except FileNotFoundError:
            print('Arquivo não encontrado!')
    except Exception as error:
            print('>>>>>>Algum erro inesperado ocorreu')
            print(error)

def salvar():
    exportar_contatos('database.txt')
    
def carregar():
    importar_contatos('database.txt')


def imprimir_menu():
    print("--------MENU--------")
    print('1-Mostrar todos os contatos da agenda: ')
    print('2-Buscar  contatos da agenda: ')
    print('3-Incluir contatos: ')
    print('4-Editar contatos: ')
    print('5-Excluir contatos: ')
    print('6-Exportar contatos para arquivo: ')
    print('7-Importar contatos para arquivo: ')
    print('0-Fechar Agenda: ')

#inicio do programa


while True:
    imprimir_menu()

    opcao = input('Escolha uma opção:')

    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        try:
            print("---------------")
            contato = input('Digite o nome do contato: ')
            buscar_contato(contato) 
        except Exception as error:
            print('{} não existe!!'.format(contato))
            print(error)
    elif opcao == '3' or opcao =='4':
        contato = input('Digite o nome do contato: ')
        telefone = input('Digite o nome do telefone: ')
        email = input('Digite o nome do email: ')
        endereco = input('Digite o nome do endereço: ')
        incluir_editar_contato(contato, telefone, email,endereco)    
    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_arquivo = input("Digite o nome do arquivo corretamente: ")
        exportar_contatos(nome_arquivo)
    elif opcao == '7':
        nome_arquivo = input("Digite o nome do arquivo corretamente: ")
        importar_contatos(nome_arquivo)
    elif opcao == '0':
        print('Programa fechado!')
        break
    else:
        print('Opção invalida')














