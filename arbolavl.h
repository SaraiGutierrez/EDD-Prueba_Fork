#ifndef ARBOLAVL_H
#define ARBOLAVL_H
#include "nodoavl.h"

class ArbolAVL
{
public:
    ArbolAVL();
    ~ArbolAVL();
    void insertar(Proyecto* proy);
    void eliminar(Proyecto* proy);
    void inOrden(NodoAVL* raiz);
    NodoAVL* buscar(int id, string nombre);
    NodoAVL* getRoot();
    void reporteAVL();
    void reporteNivelDescendente();
    void reporteNivelAscendente();
protected:
    NodoAVL* root;
    int max(int a, int b);
    int altura(NodoAVL* n);
    NodoAVL* nuevoNodo(Proyecto* proy);
    NodoAVL* rotarDerecha(NodoAVL* y);
    NodoAVL* rotarIzquierda(NodoAVL* x);
    int getBalance(NodoAVL* n);
    NodoAVL* insertarProyecto(NodoAVL* nodo, Proyecto* proy);
    NodoAVL* eliminarProyecto(NodoAVL* raiz, Proyecto* proy);
    NodoAVL* buscarProyecto(NodoAVL* raiz, int id, string n);
    NodoAVL* nodoMenorValor(NodoAVL* nodo);
    string getDot();
    string dot(NodoAVL* raiz);
    NodoAVL* factorEquilibrio(NodoAVL* raiz);
    void ordenarNivelesParaReporte(ListaDobleCircular* list, NodoAVL* raiz);
};

private:
NodoAVL* primero;
NodoAVL* obtenerPrimero();
};

#endif // ARBOLAVL_H
