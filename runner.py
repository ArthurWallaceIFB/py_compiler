from functions.create_grammar import create_grammar
from functions.lexico_ac_guided import lexical_analyser
from functions.sintatico_recursive_descendant import Programa
from utils.guided_ll1 import guided_ll1_parser
from utils.predict import predict_algorithm
from utils.token_sequence import token_sequence



if __name__ == '__main__':
    filepath = './tests/programa_teste_2.ac'
    tokens = lexical_analyser(filepath)
    G = create_grammar()
    parser = guided_ll1_parser(G)
    parser.parse(token_sequence(tokens))
    predict_alg = predict_algorithm(G) 
    ts = token_sequence(tokens)
    Programa(ts,predict_alg)
    print("\n✅ Compilação concluída com sucesso! ✅\n")
    
