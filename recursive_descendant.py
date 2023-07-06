from ac_guided_projeto import lexical_analyser
from grammar import Grammar
from guided_ll1 import guided_ll1_parser
from predict import predict_algorithm
from token_sequence import token_sequence

def print_grammar(G: Grammar) -> None:
    print("\n\n ------ GRAMÁTICA -------\n\n")
    print('Terminais:', ' '.join([x for x in G.terminals()]), '\n')
    print('Não-terminais:', ' '.join([X for X in G.nonterminals()]), '\n')
    # print(G.productions())
    print('Produções:', ' '.join(
        ['id: ' + str(p) + ' ' + str(G.lhs(p)) + '->' + str(G.rhs(p)) + '\n' for p in G.productions()]))
    print('\n\n')

def create_example_grammar()->Grammar:
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

def CompilationError(pred):
    print("Compilation error! Expected", pred)
    exit()

def Programa(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(0)
    if ts.peek() in  p.predict(0): #'Declaracoes','Bloco','$'
        Declaracoes(ts, p)
        Bloco(ts, p)
        ts.match('$')
    else:
        CompilationError(pred)
    
def Declaracoes(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(1).union(p.predict(2))
    if ts.peek() in  p.predict(1): #'Declaracao', 'Declaracoes'
        Declaracao(ts, p)
        Declaracoes(ts, p)
    elif ts.peek() in p.predict(2): # []
        return
    else:
        CompilationError(pred)

def Declaracao(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(3)
    if ts.peek() in  p.predict(3): #'Tipo', 'Identificador'
        Tipo(ts, p)
        Identificador(ts, p)
    else:
        CompilationError(pred)

def Tipo(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(4).union(p.predict(5))
    if ts.peek() in p.predict(4):  # int
        ts.match('int')
    elif ts.peek() in p.predict(5):  # float
        ts.match('float')
    else:
        CompilationError(pred)
        
def Bloco(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(6)
    if ts.peek() in p.predict(6):  # 'Comando','Comandos'
        Comando(ts, p)
        Comandos(ts, p)
    else:
        CompilationError(pred)

def Comandos(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(7).union(p.predict(8))
    if ts.peek() in p.predict(7):  # 'Comando','Comandos'
        Comando(ts, p)
        Comandos(ts, p)
    elif ts.peek() in p.predict(8):  # []
        return
    else:
        CompilationError(pred)

def Comando(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(9).union(p.predict(10)).union(p.predict(11)).union(p.predict(12)).union(p.predict(13))
    if ts.peek() in p.predict(9):  # Atribuicao
        Atribuicao(ts, p)
    elif ts.peek() in p.predict(10):  # Instrucao_print
        Instrucao_print(ts, p)
    elif ts.peek() in p.predict(11):  # Leitura
        Leitura(ts, p)
    elif ts.peek() in p.predict(12):  # Estrutura_repeticao
        Estrutura_repeticao(ts, p)
    elif ts.peek() in p.predict(13):  # Estrutura_decisao
        Estrutura_decisao(ts, p)
    else:
        CompilationError(pred)

def Leitura(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(14)
    if ts.peek() in p.predict(14):  # 'input','lparen','Identificador','rparen'
        ts.match('input')
        ts.match('lparen')
        Identificador(ts, p)
        ts.match('rparen')
    else:
        CompilationError(pred)

def Instrucao_print(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(15)
    if ts.peek() in p.predict(15):  # 'print', 'lparen', 'Identificador','rparen'
        ts.match('print')
        ts.match('lparen')
        Identificador(ts, p)
        ts.match('rparen')
    else:
        CompilationError(pred)

def Atribuicao(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(16)
    if ts.peek() in p.predict(16):  # 'Identificador', 'assignment', 'Expressao_aritmetica'
        Identificador(ts, p)
        ts.match('assignment')
        Expressao_aritmetica(ts, p)
    else:
        CompilationError(pred)

def Identificador(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(17)
    if ts.peek() in p.predict(17): #id
        ts.match('id')
    else:
        CompilationError(pred)

def Estrutura_repeticao(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(18)
    if ts.peek() in p.predict(18): #'while','lparen','Expressao_logica','rparen','do','Bloco','endWhile'
        ts.match('while')
        ts.match('lparen')
        Expressao_logica(ts, p)
        ts.match('rparen')
        ts.match('do')
        Bloco(ts, p)
        ts.match('endWhile')
    else:
        CompilationError(pred)


def Estrutura_decisao(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(19)
    if ts.peek() in p.predict(19):
        ts.match('if')
        ts.match('lparen')
        Expressao_logica(ts, p)
        ts.match('rparen')
        ts.match('then')
        Bloco(ts, p)
        Senao(ts, p)
        ts.match('endIf')
    else:
        CompilationError(pred)

def Senao(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(20).union(p.predict(21))
    if ts.peek() in p.predict(20):  # Vazio
        return
    elif ts.peek() in p.predict(21):  # Senao
        ts.match('else')
        Bloco(ts, p)
    else:
        CompilationError(pred)

def Expressao_logica(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(22).union(p.predict(23))
    if ts.peek() in p.predict(22):
        Expressao_comparativa(ts, p)
        Expressao_logica_2(ts, p)
    elif ts.peek() in p.predict(23):
        Logica_not(ts, p)
        Expressao_logica(ts, p)
    else:
        CompilationError(pred)

def Expressao_logica_2(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(24).union(p.predict(25))
    if ts.peek() in p.predict(24):  # Expressao_logica_2
        Logica_and_or(ts, p)
        Expressao_logica(ts, p)
    elif ts.peek() in p.predict(25):  # Vazio
        return
    else:
        CompilationError(pred)

def Logica_and_or(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(26).union(p.predict(27))
    if ts.peek() in p.predict(26):  # Logica_and
        Logica_and(ts, p)
    elif ts.peek() in p.predict(27):  # Logica_or
        Logica_or(ts, p)
    else:
        CompilationError(pred)

def Logica_and(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(28)
    if ts.peek() in p.predict(28):
        ts.match('&&')
    else:
        CompilationError(pred)

def Logica_or(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(29)
    if ts.peek() in p.predict(29):
        ts.match('||')
    else:
        CompilationError(pred)

def Logica_not(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(30)
    if ts.peek() in p.predict(30):
        ts.match('!')
    else:
        CompilationError(pred)


def Expressao_comparativa(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(31)
    if ts.peek() in p.predict(31):
        Expressao_aritmetica(ts, p)
        Comparacao(ts, p)
        Expressao_aritmetica(ts, p)
    else:
        CompilationError(pred)


def Comparacao(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(32).union(p.predict(33)).union(p.predict(34)).union(p.predict(35)).union(p.predict(36)).union(p.predict(37))
    if ts.peek() in p.predict(32):  # maior
        ts.match('maior')
    elif ts.peek() in p.predict(33):  # maiorIgual
        ts.match('maiorIgual')
    elif ts.peek() in p.predict(34):  # menor
        ts.match('menor')
    elif ts.peek() in p.predict(35):  # menorIgual
        ts.match('menorIgual')
    elif ts.peek() in p.predict(36):  # igual
        ts.match('igual')
    elif ts.peek() in p.predict(37):  # diferente
        ts.match('diferente')
    else:
        CompilationError(pred)


def Expressao_aritmetica(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(38)
    if ts.peek() in p.predict(38):  # maior
        T(ts, p)
        E2(ts, p)
    else:
        CompilationError(pred)


def E2(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(40).union(p.predict(41)).union(p.predict(39))
    if ts.peek() in p.predict(40):  # + T E2
        ts.match('plus')
        T(ts, p)
        E2(ts, p)
    elif ts.peek() in p.predict(41):  # - T E2
        ts.match('minus')
        T(ts, p)
        E2(ts, p)
    elif ts.peek() in p.predict(39):  # Vazio
        return
    else:
        CompilationError(pred)


def T(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(42)
    if ts.peek() in p.predict(42):
        F(ts, p)
        T2(ts, p)
    else:
        CompilationError(pred)


def T2(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(43).union(p.predict(44)).union(p.predict(45))
    if ts.peek() in p.predict(43):  # * F T2
        ts.match('mul')
        F(ts, p)
        T2(ts, p)
    elif ts.peek() in p.predict(44):  # / F T2
        ts.match('div')
        F(ts, p)
        T2(ts, p)
    elif ts.peek() in p.predict(45):  # Vazio
        return
    else:
        CompilationError(pred)

def F(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(46).union(p.predict(47)).union(p.predict(48)).union(p.predict(49))
    if ts.peek() in p.predict(46):  # inum
        ts.match('inum')
    elif ts.peek() in p.predict(47):  # fnum
        ts.match('fnum')
    elif ts.peek() in p.predict(48):  # id
        ts.match('id')
    elif ts.peek() in p.predict(49):  # ( Expressao_aritmetica )
        ts.match('lparen')
        Expressao_aritmetica(ts, p)
        ts.match('rparen')
    else:
        CompilationError(pred)


# if __name__ == '__main__':
#     G = create_example_grammar()
#     print_grammar(G)
#     predict_alg = predict_algorithm(G) 
#     ts = token_sequence(['id', 'assignment', 'inum','$'])
#     Programa(ts,predict_alg)


if __name__ == '__main__':
    filepath = 'programa_teste.ac'
    tokens = lexical_analyser(filepath)
    print(tokens, 'tokens')
    ts = token_sequence(tokens)
    G = create_example_grammar()
    print_grammar(G)
    parser = guided_ll1_parser(G)
    parser.parse(ts)
    print("\n\n -------- FIM ANALISADOR LEXICO ----------- \n\n")
    print("\n\n tokens: ", tokens)
    predict_alg = predict_algorithm(G) 
    ts = token_sequence(tokens)
    Programa(ts,predict_alg)
    
# if __name__ == '__main__':
#     filepath = 'programa_teste.ac'
#     tokens = lexical_analyser(filepath)
#     print(tokens, 'tokens')
#     ts = token_sequence(tokens)
#     print(ts)
#     G = create_ac_grammar()
#     parser = guided_ll1_parser(G)
#     parser.parse(ts)
