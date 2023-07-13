import re
from utils.grammar import Grammar


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
    r'^input$': 'input',
    r'^&&$':'and',
    r'^!=$':'diferente',
    r'^\|\|$':'or',
    r'^!$': 'not',
    r'^==$':'igual',
    r'^=$': 'assignment',
    r'^\+$': 'plus',
    r'^\-$': 'minus',
    r'^\*$':'mul',
    r'^\/$':'div',
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

            tokens = re.findall(r'\d+\.\d+|\w+|!=|==|<=|>=|<>|&&|\|\||[\(\)\[\]\{\};,!=+\-*/><]', line)
            # print(tokens)
            for t in tokens:
                found = False
                for regex, category in regex_table.items():
                    if re.fullmatch(regex, t):
                        token_sequence.append((category, t))
                        found = True
                        break
                if not found:
                    print('Erro léxico: ', t)
                    exit(0)

    token_sequence.append('$')
    return token_sequence