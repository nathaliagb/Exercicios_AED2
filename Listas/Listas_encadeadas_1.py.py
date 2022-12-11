# Exercício Listas Encadeadas - Algoritmos e Estruturas de Dados II
# Implemente o TAD Lista por encadeamento contendo as seguintes operações:
# Cria
# Insere (valor, posição)
# Remove (posição)
# Posição (valor)
# Valor (posição)
# Destroi
# Os elementos da lista podem ser valores do tipo inteiro.

class Node:
    def __init__(self, dado):
        self.dado= dado;
        self.proximo= None;


class ListaEncadeada:
    def __init__(self):
        self.inicio = None;

    def vazia(self):
        return self.inicio==None;

    def adiciona(self, posicao, elemento):
        if (posicao>0):
            novo_no=Node(elemento);
            if(posicao==1):
                novo_no.proximo=self.inicio;
                self.inicio=novo_no;
            else:
                aux=self.inicio;
                i=1;
                while (i<posicao -1 and aux != None):
                    aux= aux.proximo;
                    i +=1;
                if (aux != None):
                    novo_no.proximo = aux.proximo;
                    aux.proximo = novo_no;

    def remove(self,posicao):
        if (not self.vazia() and posicao>0):
            if(posicao==1):
                self.inicio=self.inicio.proximo;
            else:
                aux=self.inicio;
                i=1;
                anterior= None;
                while (i<posicao and aux != None):
                    anterior = aux;
                    aux=aux.proximo;
                    i+=1;
                if (aux!=None):
                    anterior.proximo=aux.proximo;

    def buscaPosicao(self,valor):
        aux= self.inicio;
        i=1;
        while (aux!= None):
            if(aux.dado == valor):
                return i;
            aux=aux.proximo;
            i+=1;
        return 0;

    def buscaValor(self, posicao):
        if(posicao>0):
            aux= self.inicio;
            i=1;
            while(i<posicao and aux !=None):
                aux= aux.proximo;
                i+=1;
                if (i==posicao and aux != None):
                    return aux.dado;
        return print("Valor não encontrado");

    def imprimir (self):
        aux= self.inicio;
        while (aux!=None):
            print (aux.dado.getNumero(),"\n");
            aux = aux.proximo;

    def destroi (self):
        self.dado=None;
        self.proximo=None;
        self.inicio=None;


class Lista:

    def __init__(self, numero):
        self.numero = numero;

    def getNumero(self):
        return self.numero;

    def setNumero(self, numero):
        self.numero= numero;


numero1=Lista(4);
numero2=Lista(8);
numero3=Lista(12);
numero4=Lista(6);

lista1= ListaEncadeada();
lista1.adiciona(1,numero1);
lista1.adiciona(2,numero2);
lista1.adiciona(3,numero3);

lista1.imprimir();

lista1.remove(2);
lista1.adiciona(2,numero4);
lista1.imprimir();

lista1.destroi();
