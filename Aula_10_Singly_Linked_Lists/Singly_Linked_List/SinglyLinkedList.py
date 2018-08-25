from Aula_10_Singly_Linked_Lists.Singly_Linked_List.Node import Node


class SinglyLinkedList:
    __head: Node

    def __init__(self):
        self.__head = None
        self.__tail = None


    def add_head(self, value):
        'Adiciona um elemento no inicio da lista'
        node = Node(value, None)

        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            node.set_next_element(self.__head)
            self.__head = node

    def add_tail(self, value):
        'Adiciona um elemento no final da lista'
        node = Node(value, None)

        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.set_next_element(node)
            self.__tail = node

    def remove_head(self):
        'Remove o elemento no inicio da lista'

        if self.__head is None:
            raise Exception("Empty.")

        self.__head = self.__head.get_next_element()


    def get_head(self):
        'Retorna o elemento do inicio da lista'
        return self.__head


    def get_tail(self):
        'Retorna o elemento do final da lista'
        return self.__tail


    def print(self):
        'Imprime a lista'
        node = self.__head

        while node is not None:
            print(node.get_value())
            node = node.get_next_element()

    def exercicio(self, value, position):
        'Adicione um elemento em um lugar determinado da lista. Valor a ser inserido informado no parâmetro value. Posição informada no parâmetro position'
        pass