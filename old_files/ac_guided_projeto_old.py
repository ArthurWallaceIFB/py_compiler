import re
from grammar import Grammar
from token_sequence import token_sequence
from guided_ll1 import guided_ll1_parser


def print_grammar(G: Grammar):
    print("\n\n --- GRAMMAR --- \n\n")
    print('Terminais:', ' '.join([x for x in G.terminals()]), '\n')
    print('Não-terminais:', ' '.join([X for X in G.nonterminals()]), '\n')
    # print(G.productions())
    print('Produções:', ' '.join(
        ['id: ' + str(p) + ' ' + str(G.lhs(p)) + '->' + str(G.rhs(p)) for p in G.productions()]))
    print("\n\n --- FIM GRAMMAR --- \n\n")

def create_ac_grammar() -> Grammar:
    G = Grammar()
    G.add_terminal('float')
    G.add_terminal('int')
    G.add_terminal('print')
    G.add_terminal('id')
    G.add_terminal('assign')
    G.add_terminal('plus')
    G.add_terminal('minus')
    G.add_terminal('times')
    G.add_terminal('divide')
    G.add_terminal('inum')
    G.add_terminal('fnum')
    G.add_terminal('if')
    G.add_terminal('else')
    G.add_terminal('equal')
    G.add_terminal('notEqual')
    G.add_terminal('greaterThan')
    G.add_terminal('lessThan')
    G.add_terminal('greaterThanOrEqual')
    G.add_terminal('lessThanOrEqual')
    G.add_terminal('$')
    G.add_terminal('open_paren')
    G.add_terminal('close_paren')
    G.add_terminal('open_bracket')
    G.add_terminal('close_bracket')
    G.add_terminal('while')
    G.add_nonterminal('S')
    G.add_nonterminal('Dcls')
    G.add_nonterminal('Dcl')
    G.add_nonterminal('Stmts')
    G.add_nonterminal('Stmt')
    G.add_nonterminal('Expr')
    G.add_nonterminal('Val')
    G.add_nonterminal('Else')
    G.add_nonterminal('Comp')
    G.add_nonterminal('CompOp')
    G.add_nonterminal('Expressao_aritmetica')
    G.add_nonterminal('T')
    G.add_nonterminal('T2')
    G.add_nonterminal('E2')
    G.add_nonterminal('F')
    G.add_production('S', ['Dcls', 'Stmts', '$'])
    G.add_production('Dcls', ['Dcl', 'Dcls'])
    G.add_production('Dcls', [])
    G.add_production('Dcl', ['float', 'id'])
    G.add_production('Dcl', ['int', 'id'])
    G.add_production('Stmts', ['Stmt', 'Stmts'])
    G.add_production('Stmts', [])
    G.add_production('Stmt', ['id', 'assign', 'Val', 'Expressao_aritmetica'])
    G.add_production('Stmt', ['print', 'Val'])
    G.add_production('Stmt', ['print', 'Val', 'Expressao_aritmetica'])
    G.add_production('Stmt', ['if', 'Comp', 'open_bracket', 'Stmts', 'close_bracket', 'Else'])
    G.add_production('Else', ['else', 'open_bracket', 'Stmts', 'close_bracket'])
    G.add_production('Else', [])
    G.add_production('Stmt', ['while', 'Comp', 'open_bracket', 'Stmts', 'close_bracket'])
    # G.add_production('Expr', ['plus', 'Val', 'Expr'])
    # G.add_production('Expr', ['minus', 'Val', 'Expr'])
    # G.add_production('Expr', ['times', 'Val', 'Expr'])
    # G.add_production('Expr', ['divide', 'Val', 'Expr'])
    # G.add_production('Expr', [])
    G.add_production('Expressao_aritmetica', ['T','E2'])
    G.add_production('E2', [])
    G.add_production('E2', ['plus', 'T', 'E2'])
    G.add_production('E2', ['minus', 'T', 'E2'])
    G.add_production('T',['F', 'T2'])
    G.add_production('T2',['times', 'F','T2'])
    G.add_production('T2',['divide', 'F','T2'])
    G.add_production('T2',[])
    G.add_production('F',[])
    G.add_production('F', ['open_paren', 'Expressao_aritmetica', 'close_paren'])
    G.add_production('F', ['Expressao_aritmetica'])
    G.add_production('Val', ['id'])
    G.add_production('Val', ['inum'])
    G.add_production('Val', ['fnum'])
    G.add_production('Comp', ['Val', 'CompOp', 'Val'])
    G.add_production('CompOp', ['equal'])
    G.add_production('CompOp', ['notEqual'])
    G.add_production('CompOp', ['greaterThan'])
    G.add_production('CompOp', ['lessThan'])
    G.add_production('CompOp', ['greaterThanOrEqual'])
    G.add_production('CompOp', ['lessThanOrEqual'])

    return G



regex_table = {
    r'^decimal$': 'float',
    r'^inteiro$': 'int',
    r'^imprimir$': 'print',
    ##r'^[a-z][a-z0-9]*$': 'id',
    r'^[a-zA-Z]$' : 'id',
    r'^=$':'assign',
    r'^\+$': 'plus',
    r'^\-$': 'minus',
    r'^\*$': 'times',
    r'^\/$': 'divide',
    r'^[0-9]+$': 'inum',
    r'^[0-9]+\.[0-9]+$': 'fnum',
    r'^se$': 'if',
    r'^entao$': 'else',
    r'^enquanto$': 'while',
    r'^\{$': 'open_bracket',
    r'^\}$': 'close_bracket',
    r'^\($': 'open_paren',
    r'^\)$': 'close_paren',
    r'^==$': 'equal',
    r'^!=$': 'notEqual',
    r'^>$': 'greaterThan',
    r'^<$': 'lessThan',
    r'^>=$': 'greaterThanOrEqual',
    r'^<=$': 'lessThanOrEqual',
}


def lexical_analyser(filepath) -> str:
    with open(filepath,'r') as f:
        token_sequence = []
        tokens = []
        for line in f:
            line = line.strip()  
            if not line:
                continue
            tokens = tokens + line.split(' ')
        for t in tokens:
            found = False
            for regex,category in regex_table.items():
                if re.match(regex,t):
                    token_sequence.append(category)
                    found=True
            if not found:
                print('Lexical error: ',t)
                exit(0) 
    token_sequence.append('$')
    return token_sequence


if __name__ == '__main__':
    filepath = 'programa_teste.ac'
    tokens = lexical_analyser(filepath)
    print(tokens, 'tokens')
    ts = token_sequence(tokens)
    print(ts)
    G = create_ac_grammar()
    print_grammar(G)
    parser = guided_ll1_parser(G)
    parser.parse(ts)
