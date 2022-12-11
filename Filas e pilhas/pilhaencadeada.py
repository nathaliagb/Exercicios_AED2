from node import Nodo;

class PilhaEnc:
    def __init__(self):
        self.topo = None;
        self.tamanho=0;

    def vazia(self):
        return self.topo==None;

    def Empilhar(self, dado):
        self.dado=dado;
        novo= Nodo (dado);
        if(not self.vazia()):
            novo.proximo = self.topo;
        self.topo = novo;
        self.tamanho+=1;
        self.tamanho;

    def Desempilhar(self):
        if(not self.vazia()):
            aux=self.topo;
            self.topo = aux.proximo;
            del aux;
        else:
            print("Pilha Vazia!");
        self.tamanho-=1;

    def Consultatopo(self):
        if(not self.vazia()):
            return self.topo.dado;

    def Destruir(self):
        while (not self.vazia()):
            self.Desempilhar();
        print ("Pilha destruída!");

    def Tamanho(self):
        return (self.tamanho);

    def Imprimir(self):
        aux = self.topo;
        while (aux != None):
            print(aux.dado, "\n");
            aux = aux.proximo;

