#ifndef LEXICO_H
#define LEXICO_H

#include <string>
#include <memory>
#include <cctype>
#include "leitorarquivo.h"
#include "token.h"

using namespace std;

class Lexico{
    private:
        LeitorArquivo *arq;
        int *id;

    public:
        Lexico(string arquivo){
            id = new int(0); 
            arq = new LeitorArquivo(arquivo);//Código fonte que recebeu como entrada
        }

        Token* proximoToken(){ //metodo principal - implementar automatos para reconhecer os lexemas e tokens
            int c;

            char ch;
            int estado = 1; //Estado inicial do automato

            while (c = arq->lerProxCaracter() != -1){//Enquanto estiver lendo o código
                ch = c;
                
                if(isspace(ch)){ // Se o caractere for branco
                    continue; // Ignora o restante dos comandos da iteração
                }

                switch(ch){
                    case '<':  
                        estado = 2; break;
                    case '=':
                        if(estado == 1)  estado = 5; break;
                        if(estado == 2)  (*id)++; estado = 3;  return new Token("<=", "OpRelMenorIgual", id);
                        if(estado == 5)  (*id)++; estado = 6;  return new Token("==", "OpRelIgual", id);
                        if(estado == 7)  (*id)++; estado = 8;  return new Token(">=", "OpRelMaiorIgual", id);
                        if(estado == 10) (*id)++; estado = 11; return new Token("!=", "OpRelDif", id);

                    case '>':
                        estado = 7; break;
                    case '!':
                        estado = 10;
                    default:
                        if(estado == 2) (*id)++; estado = 4; arq->devolverCaracter(); return new Token("<", "OpRelMenor", id);
                        if(estado == 7) (*id)++; estado = 9; arq->devolverCaracter(); new Token(">", "OpRelMaior", id); //Nesse caso tem que voltar
                        //Ele tem a devolução pois precisa verificar se é avulso ou nao, caso seja avulso, ele já 
                    
                }
            }
            
        }


};
#endif