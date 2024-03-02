import calculadora
def main():
    a = 2
    b = 3
    soma = calculadora.soma(a, b)
    print(f'{a}+{b}={soma}')
    subtracao = calculadora.subtraia(a, b)
    print(f'{a} - {b}={subtracao}')
     
main()