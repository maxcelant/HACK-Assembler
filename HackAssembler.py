import sys
from asmparser import ASMParser    

def main():
    parser = ASMParser(sys.argv[1])
    parser.run()


if __name__ == '__main__':
    main()