from utils.grammar import Grammar
from utils.predict import predict_algorithm


def is_ll1(G: Grammar, pred_alg: predict_algorithm) -> bool:
    #print("\n --- LL1 CHECK --- \n")
    for A in G.nonterminals():
        # print('Analysing',A)
        pred_set = set()
        for p in G.productions_for(A):
            #print(G.lhs(p),'->',G.rhs(p))
            #print('Predset',pred_set)
            pred = pred_alg.predict(p)
            #print('Pred',pred)
            if not pred_set.isdisjoint(pred):
                print('Problem here')
                return False
            pred_set.update(pred)
    return True