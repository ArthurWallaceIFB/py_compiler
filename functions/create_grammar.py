from utils.grammar import Grammar

def print_grammar(G: Grammar) -> None:
    print("\n\n ------ GRAMÁTICA -------\n\n")
    print('Terminais:', ' '.join([x for x in G.terminals()]), '\n')
    print('Não-terminais:', ' '.join([X for X in G.nonterminals()]), '\n')
    print('Produções:', ' '.join(
        ['id: ' + str(p) + ' ' + str(G.lhs(p)) + '->' + str(G.rhs(p)) + '\n' for p in G.productions()]))
    print('\n\n')


def create_grammar()->Grammar:
    G = Grammar()
    G.add_production('Programa', ['Declaracoes','Bloco','$']) # 0
    G.add_production('Declaracoes', ['Declaracao', 'Declaracoes']) # 1
    G.add_production('Declaracoes', []) # 2
    G.add_production('Declaracao', ['Tipo', 'Identificador']) # 3
    G.add_production('Tipo', ['int']) # 4
    G.add_production('Tipo', ['float']) # 5
    G.add_production('Bloco',['Comando','Comandos']) # 6
    G.add_production('Comandos',['Comando','Comandos']) # 7
    G.add_production('Comandos',[]) # 8
    G.add_production('Comando',['Atribuicao']) # 9
    G.add_production('Comando',['Instrucao_print']) # 10
    G.add_production('Comando',['Leitura']) # 11
    G.add_production('Comando',['Estrutura_decisao']) # 12
    G.add_production('Comando',['Estrutura_repeticao']) # 13
    G.add_production('Leitura',['input','lparen','Identificador','rparen']) # 14
    G.add_production('Instrucao_print', ['print', 'lparen', 'Identificador','rparen']) # 15
    G.add_production('Atribuicao', ['Identificador', 'assignment', 'Expressao_aritmetica']) # 16
    G.add_production('Identificador',['id']) # 17
    G.add_production('Estrutura_repeticao',['while','lparen','Expressao_logica','rparen','do','Bloco','endWhile']) # 18
    G.add_production('Estrutura_decisao', ['if', 'lparen', 'Expressao_logica','rparen', 'then', 'Bloco', 'Senao','endIf']) # 19
    G.add_production('Senao', []) # 20
    G.add_production('Senao', ['else','Bloco']) # 21
    G.add_production('Expressao_logica',['Expressao_comparativa','Expressao_logica_2']) # 22
    G.add_production('Expressao_logica', ['Logica_not','Expressao_logica']) # 23
    G.add_production('Expressao_logica_2', ['Logica_and_or','Expressao_logica']) # 24
    G.add_production('Expressao_logica_2', []) # 25
    G.add_production('Logica_and_or',['Logica_and']) # 26
    G.add_production('Logica_and_or',['Logica_or']) # 27
    G.add_production('Logica_and',['and']) # 28
    G.add_production('Logica_or',['or']) # 29
    G.add_production('Logica_not',['not']) # 30
    G.add_production('Expressao_comparativa', ['Expressao_aritmetica', 'Comparacao', 'Expressao_aritmetica']) # 31
    G.add_production('Comparacao', ['maior']) # 32
    G.add_production('Comparacao', ['maiorIgual']) # 33
    G.add_production('Comparacao', ['menor']) # 34
    G.add_production('Comparacao', ['menorIgual']) # 35
    G.add_production('Comparacao', ['igual']) # 36
    G.add_production('Comparacao', ['diferente']) # 37
    G.add_production('Expressao_aritmetica', ['T','E2']) #38
    G.add_production('E2', []) #39
    G.add_production('E2', ['plus', 'T', 'E2']) #40
    G.add_production('E2', ['minus', 'T', 'E2']) #41
    G.add_production('T',['F', 'T2']) #42
    G.add_production('T2',['mul', 'F','T2']) #43
    G.add_production('T2',['div', 'F','T2']) #44
    G.add_production('T2',[]) #45
    G.add_production('F',['inum']) #46
    G.add_production('F',['fnum']) #47
    G.add_production('F',['id']) #48
    G.add_production('F', ['lparen', 'Expressao_aritmetica', 'rparen']) #49
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
    G.add_terminal('lparen')     #(
    G.add_terminal('rparen')  #;   #,
    G.add_terminal('maior')       #
    G.add_terminal('maiorIgual')
    G.add_terminal('menor')
    G.add_terminal('menorIgual')
    G.add_terminal('igual')
    G.add_terminal('diferente')
    G.add_terminal('and')
    G.add_terminal('or')
    G.add_terminal('not')
    G.add_terminal('if')
    G.add_terminal('else')
    G.add_terminal('endIf')
    G.add_terminal('then')
    G.add_terminal('while')
    G.add_terminal('do')
    G.add_terminal('endWhile')
    G.add_terminal('print')
    G.add_terminal('input')
    G.add_terminal('$')
    G.add_nonterminal('Programa')
    G.add_nonterminal('Bloco')
    G.add_nonterminal('Declaracoes')
    G.add_nonterminal('Declaracao')
    G.add_nonterminal('Identificador')
    G.add_nonterminal('Atribuicao')
    G.add_nonterminal('Tipo')
    G.add_nonterminal('Expressao')
    G.add_nonterminal('Expressao_Aritmetica')
    G.add_nonterminal('Expressao_logica')
    G.add_nonterminal('Logica_and_or')
    G.add_nonterminal('Logica_and')
    G.add_nonterminal('Logica_or')
    G.add_nonterminal('Logica_not')
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
    G.add_nonterminal('Instrucao_print')
    G.add_nonterminal('Leitura')
    G.add_nonterminal('Expressao_logica_2')
    return G