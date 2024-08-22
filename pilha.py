def main():
    # Criação da pilha
    pilha = ['livro01', 'livro02', 'livro03', 'livro04']
    
    # ================================================

    # Método para exibir a quantidade de elementos na pilha
    def exibir_quantidade(pilha):
        quantidade_elementos = len(pilha)
        # len = leitura da quantidade de itens
        
        print("Quantidade de elementos na pilha:", quantidade_elementos)
    
    # ============================================================================

    # Método para exibir todos os elementos da pilha
    def mostrar_pilha(pilha):
        print("Elementos da pilha:")
        
        for elemento in pilha:
        # para cada item do array 
        
            print(elemento)
            # imprima (item)
    # =============================================================================
    
    # Método para verificar se um elemento está na pilha
    def pesquisar_elemento(pilha, elemento):
        if elemento in pilha:
            print(f"O elemento '{elemento}' está na pilha.")
        else:
            print(f"O elemento '{elemento}' não está na pilha.")
    
    # =====================================================
    
    # Obtendo o elemento no topo da pilha
    elemento_topo = pilha[-1]
    
    # Obtendo o identificador único (simulando o endereço de memória)
    endereco_memoria = id(elemento_topo)
       
    # Exibindo a quantidade de elementos na pilha
    print("1)")
    exibir_quantidade(pilha)
        
    # Exibindo o elemento e seu "endereço de memória"
    print("2)")
    print("Elemento no topo da pilha:", elemento_topo)
    print("Endereço de memória do elemento no topo:", endereco_memoria)
    
    # Chamando a função para mostrar todos os elementos da pilha
    print("3)")
    mostrar_pilha(pilha)
    
    # Testando a pesquisa de elementos
    print("4)")
    pesquisar_elemento(pilha, 'livro02')  # Elemento que está na pilha
    pesquisar_elemento(pilha, 'livro05')  # Elemento que não está na pilha

# Executando o código principal
if __name__ == "__main__":
    main()
