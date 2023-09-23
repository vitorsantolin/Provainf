a = []
#Topo da matriz indicando as colunas
interface  = (" Nome:        Nota1:    Nota2:    Nota3:    Média:")
print(interface)
#Impressão da matriz com "0"
for linha in range(11):
    a = a + [[float(0)]*11]
linha = 0
while linha < 11:
    coluna = 0
    while coluna < 5:
        """if coluna == 0:

            print("\n")"""
        #Linha vazia pra dar um espaço entre o topo e os nomes
        a[0][0] = ''
        a[0][1] = ''
        a[0][2] = ''
        a[0][3] = ''
        a[0][4] = ''
        #Nomes adicionados na coluna(0)
        a[1][0] = 'Júlio | '
        a[2][0] = 'Saulo | '
        a[3][0] = 'Lohan | '
        a[4][0] = 'Lucas | '
        a[5][0] = 'Pedro | '
        a[6][0] = 'Caleb | '
        a[7][0] = 'André | '
        a[8][0] = 'Jesus | '
        a[9][0] = 'David | '
        a[10][0]= 'Elias | '
        #Imprimindo a matriz com os nomes
        print(format(a[linha][coluna]), end = '       ')
        coluna+=1
    print("\n")

    linha+=1
    #nota_adicionada = 0
cont = 0
while True:
    menu = input("[1]Inserir nota \n[2]Imprimir matriz \n[3]Voltar \n[4]Sair : ") #Menu de opcoes
    
    if menu == "1": #Opcao de inserir valor na matriz
        #nota1 = nota_adicionada
        
        indice_linha = int(input("Digite a linha que deseja adicionar nota")) #Indice da linha que o valor será inserido
        indice_coluna = int(input("Digite a coluna que deseja adicionar nota"))#Índice da coluna que o valor será inserido
        if a[indice_linha][indice_coluna] != 0: #Condição pra verificar se já tem alguma nota nessa posição
            nota_lançada=input("Nota já lançada, deseja alterar? (s/n)")
            if nota_lançada == "s":
                nota_adicionada = float(input("Digite a nota a ser adicionada"))
            elif nota_lançada == "n":
                continue
        elif a[indice_linha][indice_coluna] == 0: #Condição para caso não tenha nenhum valor na posicao
            nota_adicionada = float(input("Digite a nota a ser adicionada"))
        a[indice_linha][indice_coluna] = nota_adicionada #Mudando valor da matriz a partir dos "inputs"

        
    elif menu == "2":
        #Topo da matriz
        print(" Nome:         Nota1:     Nota2:     Nota3:      Média:")
        
        a[indice_coluna][4] = ((a[1][indice_coluna])+(a[2][indice_coluna])+(a[indice_coluna][3]))/3 # Ta dando errado
        #A média é calculada no primeiro valor dado e depois não se atualiza a medida que vao sendo 
        #adicionados novos valores na mesma linha
        print()
        linha = 0
        #Impressão da matriz já com os novos valores
        while linha < 11:
            coluna = 0
            while coluna < 5:
                print(format(a[linha][coluna]), end = '        ')
                coluna+=1
            print()
            linha+=1
            
        cont+=1
    #Condição de "Voltar"
    elif menu == "3":
        continue
    #Condição de "Sair"
    elif menu == "4":
        break
        

        