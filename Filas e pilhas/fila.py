from node import Nodo;

class FilaEncadeada:
    def __init__(self):
        self.inicio=None;
        self.fim=None;
        self.tamanho=0;

    def consultar(self):
        if (not self.vazia()):
            elemento= self.inicio.dado;
            return elemento;
        else:
            return False;

    def inserir(self, dado):
        novo=Nodo(dado);
        if self.vazia():
            self.inicio=novo;
            self.fim=novo;
        else:
            self.fim.proximo = novo;
            self.fim=novo;
        self.tamanho += 1;
        self.tamanho;

    def excluir(self):
        if(not self.vazia()):
            self.inicio=self.inicio.proximo;
            self.tamanho -= 1;
        if self.inicio==None:
            self.fim=None;
            self.tamanho=0;

    def destruir(self):
        while (not self.vazia()):
            self.excluir();
            print("Fila destruída!");

    def vazia(self):
        return self.fim==None;

    def Imprimir(self):
        aux = self.inicio;
        while (aux != None):
            print(aux.dado, "\n");
            aux = aux.proximo;

        if (self.vazia()):
            print("Fila vazia");

    def Tamanho(self):
        return (self.tamanho);

