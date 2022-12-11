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
            return print(self.topo.dado);
        else:
            print("Pilha Vazia!");

    def Consultar(self,indice):
        if indice>self.tamanho:
            print("Índice maior que tamanho da Pilha");
            return False;

        aux=None;
        for i in range(0,self.tamanho-indice):
            if not aux:
                aux=self.topo;
            else:
                aux=aux.proximo;
            return aux.dado;

    def Destruir(self):
        while (not self.vazia()):
            self.Excluir();
        print ("Pilha destruída!");
