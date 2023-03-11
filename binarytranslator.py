'''
This class is going to do the translation from assembly to binary
'''

class BinaryTranslator:
    
    def __init__(self):
        self.comp_bits = {'0'  :'0101010',
                          '1'  :'0111111',
                          '-1' :'0111010',
                          'D'  :'0001100',
                          'A'  :'0110000',
                          '!D' :'0001101',
                          '!A' :'0110001',
                          '-D' :'0001111',
                          '-A' :'0110011',
                          'D+1':'0011111',
                          'A+1':'0110111',
                          'D-1':'0001110',
                          'A-1':'0110010',
                          'D+A':'0000010',
                          'D-A':'0010011',
                          'A-D':'0000111',
                          'D&A':'0000000',
                          'D|A':'0010101',
                          'M'  :'1110000',
                          '!M' :'1110001',
                          '-M' :'1110011',
                          'M+1':'1110111',
                          'M-1':'1110010',
                          'D+M':'1000010',
                          'D-M':'1010011',
                          'M-D':'1000111',
                          'D&M':'1000000',
                          'D|M':'1010101'}
        
        self.dest_bits = {''   :'000',
                          'M'  :'001',
                          'D'  :'010',
                          'MD' :'011',
                          'A'  :'100',
                          'AM' :'101',
                          'AD' :'110',
                          'AMD':'111'}
        
        self.jump_bits = {''   :'000',
                          'JGT':'001',
                          'JEQ':'010',
                          'JGE':'011',
                          'JLT':'100',
                          'JNE':'101',
                          'JLE':'110',
                          'JMP':'111'}
    
    def translate_A_instruction(self, symbol):
        binary = '0{0:015b}'.format(int(symbol))
        return binary
    
    def translate_C_instruction(self, symbol):
        # if the second or third value is a '='
        # split it to the portion before and after the equals
        if symbol[1] == '=' or symbol[2] == '=':
            symbols = symbol.split('=')
            dest = self.dest_bits[symbols[0]]
            comp = self.comp_bits[symbols[1]]
            jump = '000'
            binary = '111' + comp + dest + jump
            return binary
        if symbol[1] == ';': 
            symbols = symbol.split(';')
            dest = self.dest_bits['']
            comp = self.comp_bits[symbols[0]]                  # TODO: May need to change
            jump = self.jump_bits[symbols[1]]
            binary = '111' + comp + dest + jump
            return binary