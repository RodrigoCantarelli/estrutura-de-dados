# Implementação de Heap de Mínimo
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, item):
        heapq.heappush(self.heap, item)

    def remover_raiz(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

    def consultar_raiz(self):
        return self.heap[0] if self.heap else None

    def imprimir(self):
        for i, val in enumerate(self.heap):
            esq = 2*i + 1
            dir = 2*i + 2
            print(f"Nó: {val}")
            if esq < len(self.heap):
                print(f"  Filho esquerdo: {self.heap[esq]}")
            if dir < len(self.heap):
                print(f"  Filho direito: {self.heap[dir]}")


# Implementação de Heap de Máximo
class MaxHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, item):
        heapq.heappush(self.heap, -item)

    def remover_raiz(self):
        if not self.heap:
            return None
        return -heapq.heappop(self.heap)

    def consultar_raiz(self):
        return -self.heap[0] if self.heap else None

    def imprimir(self):
        for i, val in enumerate(self.heap):
            esq = 2*i + 1
            dir = 2*i + 2
            print(f"Nó: {-val}")
            if esq < len(self.heap):
                print(f"  Filho esquerdo: {-self.heap[esq]}")
            if dir < len(self.heap):
                print(f"  Filho direito: {-self.heap[dir]}")


# Implementação simplificada de Heap de Fibonacci
class FibonacciHeapNode:
    def __init__(self, chave):
        self.chave = chave
        self.children = []
        self.parent = None
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.roots = []

    def inserir(self, chave):
        node = FibonacciHeapNode(chave)
        self.roots.append(node)
        if not self.min_node or chave < self.min_node.chave:
            self.min_node = node

    def consultar_raiz(self):
        return self.min_node.chave if self.min_node else None

    def imprimir(self):
        print("Raízes da Heap de Fibonacci:")
        for node in self.roots:
            print(f"  {node.chave}")
