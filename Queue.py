class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self._size = 0

    # Complexidade O[1]
    def push(self, elemento):  # Insere um elemento na pilha
        node = Node(elemento)
        if self.ultimo is None:
            self.ultimo = node
        else:
            self.ultimo.next = node
            self.ultimo = node

        if self.primeiro is None:
            self.primeiro = node

        self._size = self._size + 1

    # Complexidade O[1]
    def pop(self):  # remove o elemento do topo da pilha
        if self._size > 0:
            elemento = self.primeiro.data
            self.primeiro = self.primeiro.next
            self._size = self._size - 1
            return elemento
        raise IndexError("A fila está vazia")

    # Complexidade O[1]
    def peek(self):  # retorna o topo sem remover (Observar)
        if self._size > 0:
            elemento = self.primeiro.data
            return elemento
        raise IndexError("A fila está vazia")

    def __len__(self):   # Retorna o tamanho da lista
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            ponteiro = self.primeiro
            while ponteiro:
                r = r + str(ponteiro.data) + " "
                ponteiro = ponteiro.next
            return r
        return "A fila está vazia"

    def __str__(self):
        return self.__repr__()


'''
    COMANDOS PARA EXECUTAR EM TESTES
    
    fila = Fila()  # Cria a fila
    
    fila.push(3)
    fila.push(10)
    fila.push('Jose')
    fila.push(True)
    fila.push(10.5)  # Inserção de elementos da lista, na ordem de chegada.
    
    fila.pop()  # Remove o primeiro elemento da lista
    
    fila.peek()  # Ver o primeiro elemento da lista
    
    len(fila)  # Ve o tamanho da fila
    
    fila
    print(fila)  # Exibe em lista os elementos da fila
'''