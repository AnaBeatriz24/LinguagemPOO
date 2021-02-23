from endereco import *

class Cliente():
    def __init__(self) -> None:
        print("\n+-------------------------------------------------------------+")

        self._nome = input("Digite nome seu nome: ")
        self._nome = self._nome.title()
        self._email = None

        try:
            self._telefone = int(input("Digite número para contato (sem espaços e/ou hífens): "))
        except:
            print('Somente números!')
            self._telefone = int(input("Digite número para contato (sem espaços e/ou hífens): "))
        
        while self._email == None:
            email = input("Digite seu email para contato: ")
            try:
                # verifica se o formato é válido
                x = email.split("@")
                x = email[1].split(".")
            except:
                print("Preste atenção ao digitar e insira seu email corretamente!!!")
            else:
                self._email = email

        self._endereco = Endereco()
        print("+-------------------------------------------------------------+\n")
