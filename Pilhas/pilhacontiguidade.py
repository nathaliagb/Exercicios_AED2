class PilhaCont:
    def __init__(self, tamanho):
        self.dado=[None]*tamanho;
        self.tamanho=tamanho;
        self.base=0;
        self.topo = self.base-1;

    def Empilhar (self,elemento):
        if(self.topo <self.tamanho):
            self.topo +=1;
            self.dado[self.topo] = elemento;

    def Desempilhar (self):
        if(self.topo<0):
            print("Pilha Vazia!");

        else:
            aux=self.dado[self.topo];
            self.dado[self.topo] = None;
            self.topo -=1;
            return aux;

    def ConsultaTopo (self):
        if self.topo >=self.base:
            print(self.dado[self.topo]);
            return self.dado[self.topo];

        else:
            print("Pilha Vazia!");

    def Modifica(self, novoElemento):
        if self.topo>=self.base:
            self.dado[self.topo] = novoElemento;
        else:
            print("Pilha Vazia!");

    def Destruir(self):
        self.dado = [None] * self.tamanho;
        self.base=0;
        self.tamanho=0;
        self.topo=self.base-1;
        print("Pilha Destruida")

    def Consultar(self,indice):
        return self.dado[indice];
