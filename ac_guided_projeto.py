import re
from grammar import Grammar
from token_sequence import token_sequence
from guided_ll1 import guided_ll1_parser



def create_ac_grammar()->Grammar:
    G = Grammar()

    G.add_terminal('float')
    G.add_terminal('int')
    G.add_terminal('id')
    G.add_terminal('assignment')
    G.add_terminal('plus')
    G.add_terminal('minus')
    G.add_terminal('mul')
    G.add_terminal('div')
    G.add_terminal('inum')
    G.add_terminal('fnum')
    G.add_terminal('nomeVariavel')
    G.add_terminal('lbracket')   #[
    G.add_terminal('rbracket')   #]
    G.add_terminal('lbrace')     #{
    G.add_terminal('rbrace')     #}
    G.add_terminal('lparen')     #(
    G.add_terminal('rparen')  #;
    G.add_terminal('comma')       #,
    G.add_terminal('maior')       #
    G.add_terminal('maiorIgual')
    G.add_terminal('menor')
    G.add_terminal('menorIgual')
    G.add_terminal('igual')
    G.add_terminal('if')
    G.add_terminal('else')
    G.add_terminal('while')
    G.add_terminal('endWhile')
    G.add_terminal('do')
    G.add_terminal('endIf')
    G.add_terminal('diferente')
    G.add_terminal('print')
    G.add_terminal('$')
    G.add_terminal('then')
    G.add_terminal('input')




    G.add_nonterminal('Programa')
    G.add_nonterminal('Declaracoes')
    G.add_nonterminal('Declaracao')
    G.add_nonterminal('Declaracao_Variaveis')
    G.add_nonterminal('Instrucao_Repeitcao')
    G.add_nonterminal('Atribuicao')
    G.add_nonterminal('Instrucao_Condicional')
    G.add_nonterminal('Bloco')
    G.add_nonterminal('Tipo')
    G.add_nonterminal('Expressao')
    G.add_nonterminal('Expressao_Aritmetica')
    G.add_nonterminal('T')
    G.add_nonterminal('T2')
    G.add_nonterminal('E2')
    G.add_nonterminal('F')
    G.add_nonterminal('Comando')
    G.add_nonterminal('Comandos')
    G.add_nonterminal('Senao')
    G.add_nonterminal('Estrutura_repeticao')
    G.add_nonterminal('Estrutura_decisao')
    G.add_nonterminal('Expressao_comparativa')
    G.add_nonterminal('Expressao_aritmetica')
    G.add_nonterminal('Comparacao')
    G.add_nonterminal('Constante')
    G.add_nonterminal('Operacao')
    G.add_nonterminal('Identificador')
    G.add_nonterminal('Instrucao_print')
    G.add_nonterminal('Entao')
    G.add_nonterminal('Leitura')

    G.add_production('Programa', ['Declaracoes','Bloco','$'])
    G.add_production('Declaracoes', ['Declaracao', 'Declaracoes'])
    G.add_production('Declaracoes', [])
    G.add_production('Declaracao', ['Tipo', 'Identificador'])

    G.add_production('Tipo', ['int'])
    G.add_production('Tipo', ['float'])
    G.add_production('Bloco',['Comando','Comandos'])
    G.add_production('Comandos',['Comando','Comandos'])
    G.add_production('Comandos',[])
    G.add_production('Comando',['Atribuicao'])
    G.add_production('Comando',['Instrucao_print'])
    G.add_production('Comando',['Leitura'])
    G.add_production('Comando',['Estrutura_decisao'])
    G.add_production('Comando',['Estrutura_repeticao'])
    G.add_production('Leitura',['input','lparen','Identificador','rparen'])
    G.add_production('Instrucao_print', ['print', 'lparen', 'Identificador','rparen'])

    G.add_production('Atribuicao', ['Identificador', 'assignment', 'Expressao_aritmetica'])

    G.add_production('Identificador',['id'])

    G.add_production('Estrutura_repeticao',['while','lparen','Expressao_comparativa','rparen','do','Bloco','endWhile'])
    G.add_production('Estrutura_decisao', ['if', 'lparen', 'Expressao_comparativa', 'rparen', 'then', 'Bloco', 'Senao','endIf'])
    G.add_production('Senao', [])
    G.add_production('Senao', ['else','Bloco'])

    G.add_production('Expressao_aritmetica', ['T','E2'])
    G.add_production('E2', [])
    G.add_production('E2', ['plus', 'T', 'E2'])
    G.add_production('E2', ['minus', 'T', 'E2'])
    G.add_production('T',['F', 'T2'])
    G.add_production('T2',['mul', 'F','T2'])
    G.add_production('T2',['div', 'F','T2'])
    G.add_production('T2',[])
    G.add_production('F',['inum'])
    G.add_production('F',['fnum'])
    G.add_production('F',['id'])
    G.add_production('F', ['lparen', 'Expressao_aritmetica', 'rparen'])

    G.add_production('Expressao_comparativa', ['Expressao_aritmetica', 'Comparacao', 'Expressao_aritmetica'])
    G.add_production('Comparacao', ['maior'])
    G.add_production('Comparacao', ['maiorIgual'])
    G.add_production('Comparacao', ['menor'])
    G.add_production('Comparacao', ['menorIgual'])
    G.add_production('Comparacao', ['igual'])
    G.add_production('Comparacao', ['diferente'])
    return G




regex_table = {
    r'^float$': 'float',
    r'^int$': 'int',
    r'^endWhile$': 'endWhile',
    r'^do$':'do',
    r'^while$':'while',
    r'^if$':'if',
    r'^else$':'else',
    r'^endIf$':'endIf',
    r'^then$':'then',
    r'^print$': 'print',
    r'^=$': 'assignment',
    r'^\+$': 'plus',
    r'^\-$': 'minus',
    r'^\*$':'mul',
    r'^\/$':'div',
    r'^==$':'igual',
    r'^>$' :'maior',
    r'^>=$':'maiorIgual',
    r'^<=$':'menorIgual',
    r'^<$':'menor',
    r'^[0-9]+$': 'inum',
    r'^[0-9]+\.[0-9]+$': 'fnum',
    r'^\($':'lparen',
    r'^\)$':'rparen',
    r'^[a-z][a-z0-9]*$': 'id',
}

def lexical_analyser(filepath) -> str:
    with open(filepath, 'r') as f:
        token_sequence = []
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Use expressões regulares para identificar os tokens
            tokens = re.findall(r'\w+|==|<=|>=|<>|[\(\)\[\]\{\};,=+\-*/><]', line)

            print(tokens, '\n')
            for t in tokens:
                found = False
                for regex, category in regex_table.items():
                    if re.fullmatch(regex, t):
                        token_sequence.append(category)
                        found = True
                        break
                if not found:
                    print('Erro léxico: ', t)
                    exit(0)

    token_sequence.append('$')
    return token_sequence

# def lexical_analyser(filepath) -> str:
#     with open(filepath,'r') as f:
#         token_sequence = []
#         tokens = []
#         for line in f:
#             line = line.strip()  
#             if not line:
#                 continue
#             tokens = tokens + line.split(' ')
#         for t in tokens:
#             found = False
#             for regex,category in regex_table.items():
#                 if re.match(regex,t):
#                     token_sequence.append(category)
#                     found=True
#             if not found:
#                 print('Lexical error: ',t)
#                 exit(0) 
#     token_sequence.append('$')
#     return token_sequence


if __name__ == '__main__':
    filepath = 'programa_teste.ac'
    tokens = lexical_analyser(filepath)
    print(tokens, 'tokens')
    ts = token_sequence(tokens)
    print(ts)
    G = create_ac_grammar()
    parser = guided_ll1_parser(G)
    parser.parse(ts)
