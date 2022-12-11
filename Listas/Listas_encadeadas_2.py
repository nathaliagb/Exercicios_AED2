#Altere a definição do TAD ListaEncadeada implementando:
# um método que retorne o número de elementos;
# um método que receba uma segunda listas encadeada como argumento e retorne um valor lógico indicando se as listas são iguais;
# um método que imprima os valores de uma lista encadeada de trás para frente.

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

    def tamanho (self):
        aux=self.inicio;
        i=0;
        while(aux!=None):
            i+=1;
            aux = aux.proximo;
        return i;

    def comparar(self,list1, list2):
        tamanho1 = list1.tamanho();
        tamanho2 = list2.tamanho();
        if (tamanho1 != tamanho2):
            print("Listas Diferentes");
            return False;
        else:
            aux1 = list1.inicio;
            aux2 = list2.inicio;
            x = 0;
            for i in range(tamanho1):
                if (aux1.dado != aux2.dado):
                    x+=1;
                aux1 = aux1.proximo;
                aux2 = aux2.proximo;
            if (x > 0):
                print("Listas Diferentes");
                return False;
            else:
                print("Listas iguais");
                return True;

    def inverter(self,list1):
        tamanho = list1.tamanho();
        aux = list1.inicio;
        listaaux=[];
        x=0;
        for i in range(tamanho):
            x=aux.dado;
            aux=aux.proximo;
            listaaux.append(x);

        print(listaaux[::-1]);

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

lista2=ListaEncadeada();
lista2.adiciona(1,numero2);
lista2.adiciona(2,numero4);

print("Número de elementos: "+str(lista2.tamanho()));

lista3=ListaEncadeada();
lista3.adiciona(1,numero1);
lista3.adiciona(2,numero2);
lista3.adiciona(3,numero3);

lista1.comparar(lista1,lista3);
lista2.comparar(lista2,lista3);

lista1.inverter(lista1);