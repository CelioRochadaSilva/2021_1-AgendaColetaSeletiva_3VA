import os
def clear():
        try:
            lines = os.get_terminal_size().lines
        except AttributeError:
            lines = 130
        print()

def menu (): 
    print('=+' * 20)
    print('Sejam Bem vindo(a) Agenda!')
    print('Coleta seletiva!')
    
    print ('Escolha uma opção de 1 a 7 ') 
    print ('   |1| - Cadastrar cliente') # opção de cadastro para cliente com a função adicionar_cadastro com id
    print ('   |2| - Remover cliente') # remove cliente cadastrado com função remover_cadastro
    print ('   |3| - Buscar cliente: Id') # remove cliente cadastrado com função remover_cadastro
    print ('   |4| - Listar clientes cadastrados') # lista clientes cadastrado na lista
    print ('   |5| - Cadastrar coleta')#cadastra coleta
    print ('   |6| - Listar coletas') #lista coletas cadastrada
    print ('   |7| - Busca com Id coleta')# ecluir coleta cadastrada
    print ('   |8| - Excluir coleta')# ecluir coleta cadastrada
    print ('   |9| - Sair\n') # fecha o aplicativo
    print('=+' * 20)
    opt = input('Digite a opçao desejada: \n').strip() # entrada de dados
   
    return opt # retorna menu opçes
clear()

def adicionar_cliente():#adicionar cadastro cliente
    #id_cliente = 0
    idCliente = int(input('Digite o id do cliente: \n'))
      
    nome = input('Digite o nome do cliente ou da empresa: \n') 
    email = input('Digite o e-mail de contato: ')
    telefone = input('Digite o telefone: \n')
    endereco = input('Digite o endereço: \n')
    
    try: # tratamento de erro
        agenda = open("cliente.txt", "a") #w apaga a pode escrever    , encoding='utf-8'
        dados = f'{idCliente} | {nome} | {email} | {telefone} | {endereco}\n' # nao aceita f
    except:
        print("ERRO na gravação do cadastro do cliente !!!")
    
    agenda.write(dados)
    agenda.close()

   # remove cliente cadastrado informando o nome
def remover_cliente():
    nomeExcluido = input(f'Digite o nome deseja excluir: \n')
    agenda = open("cliente.txt", "r")
    excluirNome = [] # vaiavel auxiliar 1 guarda dados 
    aux = [] # vaiavel auxiliar 1 guarda dados 
    for x in agenda: # percorre a genda arquivo
        excluirNome.append(x)
    for x in range(0,len(excluirNome)):
        if nomeExcluido not in excluirNome[x]:
            aux.append(excluirNome[x])
    
    agenda = open("cliente.txt", "w")

    for x in aux:
        agenda.write(x)
    #print(f'Contato excluido com sucesso !!!')
    listar_clientes()
                
    agenda.close()

       
def buscar_clientes():
    nome = input(f'Digite o id do cliente para ser listado: \n')
    agenda = open("cliente.txt", "r") # exibe lista de clientes pelo Id 
    for contato in agenda:
        if nome in contato.split(" | ")[0]:
            print(contato)
    agenda.close()

def buscar_coletaSeletiva():
    nome = input(f'Digite o id do cliente para ser listado: \n')
    agenda = open("coleta.txt", "r") # exibe lista de clientes pelo Id 
    for contato in agenda:
        if nome in contato.split(" | ")[0]:
            print(contato)
    agenda.close()

def listar_clientes():
    agenda = open("cliente.txt", "r") # exibe lista de clientes
    
    for cliente in agenda:
        print(cliente ,'\n')
    agenda.close()
    

def adicionar_coleta():
    tcoleta=[]
    horacoleta=[]
    pcoleta=[]
    idCliente = int(input('Digite o id do cliente: \n')) #ok
    nome = input('Digite o nome do cliente: \n') 
    endereco = input('Digite o endereço: \n')
    telefone = input('Digite o telefone: \n')
    print ('Escolha a opção de coleta seletiva:') 
    print ('   |1ª| - Papel') 
    print ('   |2ª| - Vidro') 
    print ('   |3ª| - Metal') 
    print ('   |4ª| - Orgânico')
    print ('Digite sua opção: 1 a 4')
    print()
        
    tipoColeta = input('Digite o tipo de coleta: ')
    tipoColeta=tipoColeta.upper()
    tcoleta.append(tipoColeta)
    if tipoColeta == "1":
        tipoColeta ="Papel" # intenção adicionar texto
        tcoleta.append(tipoColeta) # falta inclementar 
        print('Opção de coleta registrada: ', tipoColeta)
    
    elif tipoColeta == "2":
        tipoColeta ="Vidro" # intenção adicionar texto
        tcoleta.append(tipoColeta)
        print('Opção de solicitação: registrada! ',tipoColeta)
    
    elif tipoColeta == "3":
        tipoColeta="Metal" # intenção adicionar texto
        tcoleta.append(tipoColeta)
        print('Opção de solicitação: registrada! ', tipoColeta)
    
    elif tipoColeta == "4":
        tipoColeta="Metal" # intenção adicionar texto
        tcoleta.append(tipoColeta)
        print('Opção de solicitação: registrada! ', tipoColeta)
            
    else:
             
        print('Opção de solicitação: não registrada! ') 
    #pass 
    # fazer implementação com lista para capitura escolha  lista = [papel,vidro,metal e organico]

    print ('Escolha o horário de atendimento!') 
    print ('   |1ª| - diurno') 
    print ('   |2ª| - Vespertino') 
    print ('   |3ª| - Noite') 
    print ('Digite sua opção: 1 a 3')
    horaColeta = input('Digite o tipo de coleta: \n')
    horaColeta=horaColeta.upper()
    horacoleta.append(horaColeta)
    if horaColeta == "1":
        horaColeta = "Diurno" # intenção adicionar texto

        pcoleta.append(horaColeta) 
        print('Horário registrado: ', horaColeta)
    
    elif horaColeta == '2':
        horaColeta ='Vespertino' # intenção adicionar texto
        pcoleta.append(horaColeta)
        print('Horário registrado: ', horaColeta)

    elif horaColeta == '3':
        horaColeta ='Noturno' # intenção adicionar texto
        pcoleta.append(horaColeta)
        print('Horário registrado:', horaColeta)
    else:
        print('Horário não registrado: ')

    
    # fazer implementação com lista para capitura escolha  lista = [diurno,vespertin,noturno]
    
    try: # tratamento de erro
        agenda = open("coleta.txt", "a") #w apaga a pode escrever    , encoding='utf-8'
        dados = f'{idCliente} | {nome} | | {endereco} | {telefone} | {tipoColeta} | {horaColeta} \n' # nao aceita f
    except:
        print("ERRO na gravação do cadastro do cliente !!!")
    
    agenda.write(dados)
    agenda.close()
         
    f = open("coleta.txt", "r") #  retirei a e col w não exibe lista de clientes encoding='utf-8'
       
    f.close()   
            
    f = open("coleta.txt", "a", encoding='utf-8') # não exibe lista de clientes
        
    f.close()


def listar_coleta():
    f = open("coleta.txt", "r", encoding='utf-8')
    for x in f:
        print('Tipo de coleta cadastrada: ', x)
        
    f.close()
    
   
def excluir_coletaSeletiva():
  
    nomeExcluido = input(f'Digite o nome deseja excluir: ')
    agenda = open("coleta.txt", "r")
    excluirNome = [] # vaiavel auxiliar 1 guarda dados 
    aux = [] # vaiavel auxiliar 1 guarda dados 
    for x in agenda: # percorre a genda arquivo
        excluirNome.append(x)
    for x in range(0,len(excluirNome)):
        if nomeExcluido not in excluirNome[x]:
            aux.append(excluirNome[x])
    
    agenda = open("coleta.txt", "w")

    for x in aux:
        agenda.write(x)
    
    listar_coleta()
                
    agenda.close()

def sair():
    exit()

opcao = menu() 
while opcao != '9': # fecha o aplicativo
    if opcao == '1': #adiciona cliente
        adicionar_cliente() 

    elif opcao == '2':  #remove cadastro cliente mas esta escrevendo também 
        remover_cliente() 

    elif opcao == '3': 
        buscar_clientes() # exibe lista d e clientes cadastrado
        
    elif opcao == '4': 
      
        listar_clientes() # exibe lista d e clientes cadastrado
        
        
    elif opcao == '5': # cadastra coleta
        adicionar_coleta()

    elif opcao == '6': # lista soicitações de coleta
        listar_coleta()
                        
    elif opcao == '7': # exclui coleta
        
        buscar_coletaSeletiva()

    elif opcao == '8': # exclui coleta
        
        excluir_coletaSeletiva()

    elif opcao == '9': # lista soicitações de coleta
            
        exit()
      
    
    else:
        print('Opçao inválida')
        
               
    opcao = menu() 

        



        


        


        

            



    

    




