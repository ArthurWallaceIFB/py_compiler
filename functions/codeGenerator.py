symbols_table = []
address = 0


def insert_into_symbol_table(var_name,type):
    global address
    print('symbols_table: ', symbols_table)
    symbols_table.append({'var_name': var_name, 'type': type, 'address': address})
    address += 1
    print('symbols_table depois: ', symbols_table)
    return



def emit_code(code):
    f = open("./results/resultado.ac", 'a')
    f.write(code + '\n')
    f.close()
    return

def clear_result_file():
    return


def get_var_address(var_name):
    for x in symbols_table:
        if x['var_name'] == var_name:
            return x['address']