#Implemente:
# todas as operações básicas do TAD Tabela por contiguidade física;
# uma nova operação de inserção ordenada e o algoritmo de busca binária;
# um programa que importe a classe e teste todos os métodos. 

class Tabela:
    def __init__(self, tamanho, busca):
        self.tamanho = tamanho
        self.busca = busca
        self.chave = [None] * tamanho
        self.elemento = [None] * tamanho
        self.count = 0

    def BuscaSeq(self, chave):
        busca = None
        for i in range(self.count):
            if (chave == self.chave[i]):
                busca = i
        if (busca != None):
            return busca
        else:
            return -1

    def BuscaBin(self, chave):
        comeco = 0
        fim = self.count - 1
        while (comeco <= fim):
            total = (comeco + fim) // 2
            if (self.chave[total] == chave):
                return total
            elif (self.chave[total] > chave):
                fim = total - 1
            else:
                comeco = total + 1
        return -1

    def Cheia(self):
        if (self.count == self.tamanho):
            return True
        else:
            return False

    def Vazia(self):
        if (self.count == 0):
            return True
        else:
            return False

    def Insere(self, chave, elemento):
        if (self.Cheia()):
            return None
        else:
            if (self.count == 0):
                self.chave[0] = chave
                self.elemento[0] = elemento
                self.count = self.count + 1
                for i in range(1, self.tamanho):
                    self.chave[i] = 0
            else:
                self.chave[self.count] = chave
                self.elemento[self.count] = elemento
                self.count = self.count + 1
        self.Ordenar()

    def Ordenar(self):
        for i in range(self.count):
            chaveaux = self.chave
            elemaux = self.elemento[i]
            j = i
            while ((j > 0) and (chaveaux < self.chave[j - 1])):
                self.chave[j] = self.chave[j - 1]
                self.elemento[j] = self.elemento[j - 1]
                j = j - 1
            self.chave[j] = chaveaux
            self.elemento[j] = elemaux

    def Destroi(self):
        for i in range(self.count):
            self.chave[i] = None
            self.elemento[i] = None
        self.count = 0

