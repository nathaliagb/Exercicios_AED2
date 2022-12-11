from pilhaencadeada import *
from pilhacontiguidade import *

class Pilhas(PilhaEnc, PilhaCont):
        def ComparaPilha(self, pilh1, pilh2):
                if pilh1.tamanho != pilh2.tamanho:
                        print("Pilhas diferetes!");
                        return False;


                for i in range(0, pilh1.tamanho):
                        if pilh1.Consultar(i) != pilh2.Consultar(i):
                                print("Pilhas diferentes!");
                                return False;

                print("Pilhas Iguais!");
                return True;


pilha1=PilhaCont(4);
pilha1.Empilhar(1);
pilha1.Empilhar(2);
pilha1.Empilhar(3);
pilha1.Empilhar(4);

pilha2=PilhaCont(4);
pilha2.Empilhar(1);
pilha2.Empilhar(2);
pilha2.Empilhar(3);
pilha2.Empilhar(4);


pilha3=Pilhas();

pilha3.ComparaPilha(pilha1,pilha2);
