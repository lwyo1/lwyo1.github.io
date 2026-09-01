#ifndef TOKEN_H
#define TOKEN_H


#include <string>
#include <ostream>

using namespace std;


class Token
{
public:
    string lexema;
    string tipo;
    int id;
    Token(string lexema, string tipo, int *id) //Construtor token
        :lexema(lexema), tipo(tipo), id(*id){};        
    
    string toString(){
        return "<"+tipo+", "+lexema+", "+ to_string(id) +">";
    }
};


#endif