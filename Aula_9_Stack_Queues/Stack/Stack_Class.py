class Stack():

    def __init__(self):
        self.__data = []

    def push(self, element):
        'Adiciona um elemento'
        self.__data.append(element)

    def pop(self):
        'Remove e retorna o último elemento da pilha'
        if self.is_empty():
            raise Exception('Stack is Empty')
        else:
            return self.__data.pop()

    def top(self):
        'Retorna o último elemento da pilha'
        if self.is_empty():
            raise Exception('Stack is Empty')
        else:
            return self.__data[-1]

    def is_empty(self):
        'Retorna true caso a pilha não contenha nenhum elemento'
        return self.__len__() == 0

    def __len__(self):
        'Retorna o tamanho da pilha'
        return len(self.__data)











