class SymbolTable:
    
    
    def __init__(self):
        self.variables_address = 16
        # Create a table for labelled symbols
        self.labels_table = {}  
        # Create a table for variables
        self.variables_table = {}
        # Create a table for predefined symbols
        self.predefined_symbols_table = {'R0':0, 'R1':1, 'R2':2, 'R3':3, 'R4':4, 'R5':5,
                                         'R6':6, 'R7':7, 'R8':8, 'R9':9, 'R10':10, 'R11':11,
                                         'R12':12, 'R13':13, 'R14':14, 'R15':15, 'SCREEN':16384,
                                         'KBD':24576, 'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4,}
        
    def get_predefined_symbol(self, line):
        return self.predefined_symbols_table[self.clean_variable(line)]
    
    def get_labelled_symbol(self, line):
        return self.labels_table[self.clean_variable(line)]
    
    def get_variable(self, line):
        return self.variables_table[self.clean_variable(line)]
    
    def in_predefined_table(self, line):
        if self.clean_variable(line) in self.predefined_symbols_table:
            return True
        return False
    
    def in_labelled_symbols(self, line):
        if self.clean_variable(line) in self.labels_table:
            return True
        return False
    
    def in_variables_table(self, line):
        if self.clean_variable(line) in self.variables_table:
            return True
        return False
    
    def add_to_labels(self, line, addr):
        label = self.clean_label(line)
        self.labels_table[label] = addr + 1
        
    def clean_label(self, line):
        return line[1:-1]
    
    def add_to_variables(self, line):
        variable = self.clean_variable(line)
        self.variables_table[variable] = self.variables_address
        self.increment_address()
    
    def clean_variable(self, line):
        return line[1:]
    
    def increment_address(self):
        self.variables_address += 1