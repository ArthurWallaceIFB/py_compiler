
from functions.compiler import Compiler
from functions.lexico_ac_guided import lexical_analyser
from utils.predict import predict_algorithm
from utils.token_sequence import token_sequence

compiler = Compiler()

def Programa(ts: token_sequence, p: predict_algorithm) -> None:
    compiler.clear_result_file()
    print("\n\n\n ------- Programa\n\n\n")
    pred = p.predict(0)
    if ts.peek() in  p.predict(0): #'Declaracoes','Bloco','$'
        Declaracoes(ts, p)
        Bloco(ts, p)
        ts.match('$')
        compiler.emit_code("STOP")
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
        type = Tipo(ts, p)
        var_name = ts.getValue()
        compiler.insert_into_symbol_table(var_name,type)
        compiler.emit_code('PUSHIMM 0')
        Identificador(ts, p)
    else:
        CompilationError(pred)

def Tipo(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(4).union(p.predict(5))
    if ts.peek() in p.predict(4):  # int
        ts.match('int')
        return('int')
    elif ts.peek() in p.predict(5):  # float
        ts.match('float')
        return('float')
    else:
        CompilationError(pred)
        
def Bloco(ts: token_sequence, p: predict_algorithm) -> None:
    print("Bloco")
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
    elif ts.peek() in p.predict(13):  # Estrutura_repeticao
        Estrutura_repeticao(ts, p)
    elif ts.peek() in p.predict(12):  # Estrutura_decisao
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
        var_name = Identificador(ts, p)
        ts.match('assignment')
        Expressao_aritmetica(ts, p)
        var_address = compiler.get_var_address(var_name)
        compiler.emit_code('STOREOFF '+str(var_address))
    else:
        CompilationError(pred)

def Identificador(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(17)
    var_name = ts.getValue()
    if ts.peek() in p.predict(17): #id
        ts.match('id')
        return var_name
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
        ts.match('and')
    else:
        CompilationError(pred)

def Logica_or(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(29)
    if ts.peek() in p.predict(29):
        ts.match('or')
    else:
        CompilationError(pred)

def Logica_not(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(30)
    if ts.peek() in p.predict(30):
        ts.match('not')
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
        compiler.emit_code('ADD')
    elif ts.peek() in p.predict(41):  # - T E2
        ts.match('minus')
        T(ts, p)
        E2(ts, p)
        compiler.emit_code('SUB')
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
        compiler.emit_code('TIMES')
    elif ts.peek() in p.predict(44):  # / F T2
        ts.match('div')
        F(ts, p)
        T2(ts, p)
        compiler.emit_code('DIV')
    elif ts.peek() in p.predict(45):  # Vazio
        return
    else:
        CompilationError(pred)

def F(ts: token_sequence, p: predict_algorithm) -> None:
    pred = p.predict(46).union(p.predict(47)).union(p.predict(48)).union(p.predict(49))
    if ts.peek() in p.predict(46):  # inum
        num_value = ts.getValue()
        ts.match('inum')
        compiler.emit_code('PUSHIMM '+num_value)
    elif ts.peek() in p.predict(47):  # fnum
        ts.match('fnum')
    elif ts.peek() in p.predict(48):  # id
        var_name = ts.getValue()
        ts.match('id')
        var_address = compiler.get_var_address(var_name)
        compiler.emit_code('PUSHOFF '+ str(var_address))
    elif ts.peek() in p.predict(49):  # ( Expressao_aritmetica )
        ts.match('lparen')
        Expressao_aritmetica(ts, p)
        ts.match('rparen')
    else:
        CompilationError(pred)


def CompilationError(pred):
    print("Compilation error! Expected", pred)
    exit()