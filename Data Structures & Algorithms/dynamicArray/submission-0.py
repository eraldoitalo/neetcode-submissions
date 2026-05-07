class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int: #apenas pegar o calor do arr
        return self.arr[i]

    def set(self, i: int, n: int) -> None: #setar um valor ao index
        self.arr[i] = n 

    def pushback(self, n: int) -> None: # inserir um valor n a ultima posição do array
        if self.length == self.capacity:
            self.resize()

        # inserir a proxima posicao vazia 
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int: # remover o ultimo elemento do array 
        if self.length > 0: #se self.length for maior q 0 
            self.length -= 1 # exclua o ultimo elemento 
        return self.arr[self.length] # retorna o ultimo elemento exlcuido
 

    def resize(self) -> None: # criar um novo array com dupla capacidade 
        self.capacity = 2 * self.capacity # multiplicando a capacidade
        new_arr = [0] * self.capacity

        for i in range(self.length): 
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int: # descobrir o tamanho do vetor
        return self.length
    
    def getCapacity(self) -> int: # descobrir a capacidade do vetor
        return self.capacity
