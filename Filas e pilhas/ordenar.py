from fila import *
from pilhaencadeada import *

class Ordena:

    def compara(self,fil1,pilh1,pilh2):

        pilh1.Empilhar(fil1.consultar());
        fil1.excluir();

        while (fil1.Tamanho() !=0):
            if (pilh1.Consultatopo() == None):
                pilh1.Empilhar(fil1.consultar());
                fil1.excluir();
                while(not pilh2.vazia()):
                    pilh1.Empilhar(pilh2.Consultatopo());
                    pilh2.Desempilhar();

            if (fil1.consultar()== None):
                while (not pilh2.vazia()):
                    pilh1.Empilhar(pilh2.Consultatopo());
                    pilh2.Desempilhar();
            else:
                if fil1.consultar()>=pilh1.Consultatopo():
                    pilh1.Empilhar(fil1.consultar());
                    fil1.excluir();
                    while (not pilh2.vazia()):
                        pilh1.Empilhar(pilh2.Consultatopo());
                        pilh2.Desempilhar();

                else:
                    while(fil1.consultar()<pilh1.Consultatopo()):

                        if (fil1.consultar()<pilh1.Consultatopo()):
                            pilh2.Empilhar(pilh1.Consultatopo());
                            pilh1.Desempilhar();
                            break;

                        if (pilh1.Consultatopo()==None):
                            pilh1.Empilhar(fil1.consultar());
                            fil1.excluir();
                            break;

                        else:
                            pilh1.Empilhar(fil1.consultar());
                            fil1.excluir();
                            break;

                        while(not pilh2.vazia()):
                            pilh1.Empilhar(pilh2.Consultatopo());
                            pilh2.Desempilhar();

        while (not pilh2.vazia()):
            pilh1.Empilhar(pilh2.Consultatopo());
            pilh2.Desempilhar();

        while(pilh1.Tamanho() !=0):
            pilh2.Empilhar(pilh1.Consultatopo());
            pilh1.Desempilhar();

        while (pilh2.Tamanho() != 0):
            fil1.inserir(pilh2.Consultatopo());
            pilh2.Desempilhar();

fila0=FilaEncadeada();
fila0.inserir(88);
fila0.inserir(6);
fila0.inserir(1);
fila0.inserir(7);
fila0.inserir(2);
fila1=Ordena();

pilha1=PilhaEnc();
pilha2=PilhaEnc();

fila1.compara(fila0,pilha1,pilha2);