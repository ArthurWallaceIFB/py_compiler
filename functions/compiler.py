import os


class Compiler:
    def __init__(self):
        self.symbols_table = []
        self.address = 0
        self.labelCount = 0

    def insert_into_symbol_table(self, var_name, tipo):
        print('symbols_table: ', self.symbols_table)
        self.symbols_table.append({'var_name': var_name, 'type': tipo, 'address': self.address})
        self.address += 1
        print('symbols_table depois: ', self.symbols_table)

    def emit_code(self, code):
        with open("./results/resultado.sam", 'a') as f:
            f.write(code + '\n')

    def clear_result_file(self):
        if os.path.exists("./results/resultado.sam"):
            os.remove("./results/resultado.sam")
            return
        else:
            print("\n\n\nResult file not found!\n\n\n")

    def get_var_address(self, var_name):
        for x in self.symbols_table:
            if x['var_name'] == var_name:
                return x['address']
    
    def generate_label(self):
        self.labelCount += 1
        return f"label_{self.labelCount}"