from symboltable import SymbolTable
from binarytranslator import BinaryTranslator

class ASMParser:
    
    def __init__(self, filename):
        self.filename = filename
        self.file_content = None
        self.symbol_table = SymbolTable()
        self.translator = BinaryTranslator()
        
    def run(self):
        self.open_file()
        self.first_pass()
        self.second_pass()
    
    def open_file(self):
        with open(self.filename, 'r') as file:
            self.file_content = file.readlines()
    
    # Add all labelled symbols to table
    def first_pass(self):
        line_count = 0
        for line in self.file_content:
            if self.is_comment(line) or line.isspace():
                continue
            line = self.strip_whitespace(line)
            if self.is_labelled_symbol(line):
                self.symbol_table.add_to_labels(line, line_count)
                continue
            line_count += 1
                
                
    def second_pass(self):
        f = open('Pong.hack', 'a')
        f.truncate(0) # Clear the file
        for line in self.file_content:
            if self.is_ignorable_line(line):
                continue
            line = self.remove_comments(line)
            translated_line = self.translate_instruction(line)
            f.write(translated_line + '\n')
        f.close()
            
    def is_ignorable_line(self, line):
        line = self.strip_whitespace(line)
        if line.isspace() or line == "": 
            return True
        if self.is_comment(line):
            return True
        if self.is_labelled_symbol(line): 
            return True
        return False
    
    def is_comment(self, line):
        if line[0] == '/':
            return True
        return False
    
    def remove_comments(self, line):
        index = line.find('//')
        if index != -1:
            line = line[:index]
        return line.strip()
    
    def strip_whitespace(self, line):
        return line.strip()
    
    def is_labelled_symbol(self, line):
        if line[0] == "(": 
            return True
        return False
    
    def translate_instruction(self, line):
        if self.is_A_instruction_type(line):
            symbol = self.handle_A_instruction(line)
            return self.translator.translate_A_instruction(symbol)
        return self.translator.translate_C_instruction(line)
    
    # Determine if it's a C or A instruction
    def is_A_instruction_type(self, line):
        if line[0] == '@': return True
        return False
    
    def handle_A_instruction(self, line):
        # We want to find it or create it, then return it
        # so that it can be translated
        symbol = None
        if self.symbol_table.is_simple_symbol(line):
            symbol = self.symbol_table.get_simple_symbol(line)
        elif self.symbol_table.in_predefined_table(line):
            symbol = self.symbol_table.get_predefined_symbol(line)
        elif self.symbol_table.in_labelled_symbols(line):
            symbol = self.symbol_table.get_labelled_symbol(line)
        elif self.symbol_table.in_variables_table(line):
            symbol = self.symbol_table.get_variable(line)
        else:
            self.symbol_table.add_to_variables(line)
            symbol = self.symbol_table.get_variable(line)
        return symbol