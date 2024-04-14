def menu():
    print("*" * 50)
    print("JOGO DA FORCA".center(50))
    print("=" * 50)
    print("*  Você terá 10 tentativas, depois ...  *".center(50))
    print("-" * 50)


# O prgrama acima não consegue ser chamado sozinho
# para executar diretamante precisamos colocar o codifo abaixo no final

if __name__ == "__main__":
    menu()

# desta maneira ele pode ser chamado em outro programa e também pode
# ser usado sozinho
