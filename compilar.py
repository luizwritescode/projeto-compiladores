#TODO:
#   funcao proximo_simbolo() -> retornar proximo simbolo do texto fonte com base em magia negra
#       cada chamada dessa funcao pede 
#           1) posicao corrente do codigo fonte
#           2) codigo do atomo formado ( parametro de retorno )
#           3) indice da tabela de simbolos onde o atomo foi gravado 
#   implementar o limite de 35 caracteres para cada atomo
#   implementar a filtragem de comentarios (tem que ser na analise lexica, para persistir o numero correto de linhas )
#   Tabela de simbolos
#        - acertar o tipo do simbolo
#        - so armazenar 35 primeiros carecteres validos
#   Tabela_Simbolos.gerar_tabela() -> arquivo .TAB
#   Analise_Lexica.gerar_analise() -> arquivo .LEX


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

# imprimir instrucoes de uso caso o usuario coloque o comando errado
if len(sys.argv) < 2  or '-h' in sys.argv or '--help' in sys.argv:
    imprimir_instrucoes()
    sys.exit()


#retorna o conteudo do arquivo em uma string grande
#se o arquivo nao for encontrado, termina a execução
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

# Declaracao de estrutura de um Identifier contem
# id
# lexeme
# codigo 
# qnt. antes do truncamento
# qnt. depois do truncamento
# tipo
# numero da linha que foi encontrado pelas primeiras cinco vezes

class Identifier: 
    def __init__(self, _id, _lexeme, _codigo, _qtat, _qtdt, _tipo, _linha):
        self.id = _id
        self.lexeme = _lexeme
        self.codigo = _codigo
        self.qtat = _qtat
        self.qtdt = _qtdt
        self.tipo = _tipo
        self.linha = _linha

# Declaracao de estrutura de um Atomo contem
# lexeme
# codigo 
# indice na tabela de simbolos

class Atomo:
    def __init__(self, _lexeme, _codigo, _idx_tabela_simbolos):
        self.lexeme = _lexeme
        self.codigo = _codigo
        self.idx_tabela_simbolos = _idx_tabela_simbolos

# Declaracao de estrutura da Tabela de Simbolos contem
# valores: uma lista de Identifiers
# funcao que adciona Identifiers a lista se nao existirem
# funcao que procurar o simbolo e retorna o indice
class Tabela_Simbolos:
    def __init__(self):
        self.values = []

    #tem que ver se isso funciona
    def append(self, identifier):
        for _simbolo in self.values:
             if _simbolo.lexeme == identifier.lexeme: 
                return
        
        self.values.append(identifier)

    def procurar_simbolo(self, simbolo):
        if simbolo in self.values:
            return self.values.index(simbolo)
        else: 
            return '-'

    def gerar_tabela(self):
        return
            
# Declaracao de estrutura da Analise Lexica contem
# valores: uma lista de Atomos
# funcao que adciona Atomos a 
# funcao que procurar o simbolo e retorna o indice
class Analise_Lexica:
    def __init__(self):
        self.values = []

    def append(self, atomo):
        self.values.append(atomo)

    def gerar_analise(self):
        return

analise_lexica = Analise_Lexica()
tabela_simbolos = Tabela_Simbolos()
atomos = atomos.atomos

#######################################################
#faz magica com os automatos e retorna o proximo simbolo
def proximo_simbolo(texto):
    return texto
#######################################################


def main():

    path = sys.argv[1]
    
    arquivo = ler_arquivo(path)

    #identifica simbolos e corta eles do buffer do arquivo ate ficar vazio
    while( len(arquivo) > 0 ):

        simbolo = proximo_simbolo(arquivo)

        #todo atomo precisa ser adcionado a analise lexica
        analise_lexica.append( 
            Atomo(
                simbolo, 
                atomos[str.capitalize(simbolo)],
                tabela_simbolos.procurar_simbolo(simbolo)
                )
            )
        #se nao for o ultimo simbolo, corta ele do arquivo
        if len(simbolo) < len(arquivo):
            arquivo = arquivo[ len(simbolo) : ]
        # tem que rever essa logica aqui parcero
        else:
            arquivo = ""

    # Gera arquivo .TAB
    # Gera arquivo .LEX

    #ggwp



if __name__ == "__main__":
    main()
