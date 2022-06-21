import atomos
import os
import sys

def imprimir_instrucoes():
    print("\nEste é um Static Checker para linguagem DonkSoup2022-1 criada pelo professor da disciplina Compiladores Osvaldo Melo.")
    print("Ao executá-lo com um arquivo .dks, irá resultar em uma análise léxica e uma tabela de símbolos do texto fonte.\n")
    print("\tUso:   py compilar.py ARQUIVO")
    print("\nObs.\n - Caso o arquivo não se encontre na pasta atual, use o caminho absoluto.")
    print(" - Não é necessário especificar a extensão do arquivo.")
    print(" - Para exibir essa mensagem novamente execute o script com a opção -h ou --help.")

# imprimir instrucoes de uso caso o usuario entre o comando errado
if len(sys.argv) < 2  or '-h' in sys.argv or '--help' in sys.argv:
    imprimir_instrucoes()
    sys.exit()

def ler_arquivo(path):

    #procurando arquivo no caminho, parece que pro python o caminho nao eh case sensitive
    if os.path.isfile(path + ".DKS"):
        with open(path + ".DKS", 'r') as arquivo:
            conteudo = arquivo.read()
    else: 
        print("\n\tERRO - arquivo não encontrado\n")
        imprimir_instrucoes()
        sys.exit()
    
    return conteudo



def main():

    path = sys.argv[1]
    
    arquivo = ler_arquivo(path)

    print(arquivo)


if __name__ == "__main__":
    main()
