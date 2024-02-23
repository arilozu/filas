#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NPALABRAS 5

// Escribe un programa que reciba 5 palabras,
// las guarde en una lista de punteros haciendo reserva dinámica
// de memoria con malloc y las ordene alfabéticamente.

int compararPalabras(const void *a, const void *b) {
    return strcmp(*(const char **)a, *(const char **)b);
}

int main(void) {
    // Defino el vector de punteros
    char *palabras[NPALABRAS];
    char auxiliar[15];
    int cont;

    // Defino el resto de las variables

    // Leo las palabras
    for (cont = 0; cont < NPALABRAS; cont++) {
        printf("\nEscriba la palabra %d: ", cont + 1);
        scanf(" %s", auxiliar);
        palabras[cont] = (char *)malloc((strlen(auxiliar) + 1) * sizeof(char));
        strcpy(palabras[cont], auxiliar);
    }

    // Muestro la lista tal cual
    printf("\n************************");
    printf("\n*  LISTA DE PALABRAS   *");
    printf("\n************************");
    for (cont = 0; cont < NPALABRAS; cont++) {
        printf("\n %s", palabras[cont]);
    }

    // Ordeno la lista alfabéticamente usando qsort
    qsort(palabras, NPALABRAS, sizeof(char *), compararPalabras);

    // Vuelvo a mostrar la lista
    printf("\n********************************");
    printf("\n*  LISTA DE PALABRAS ORDENADA  *");
    printf("\n********************************");
    for (cont = 0; cont < NPALABRAS; cont++) {
        printf("\n %s", palabras[cont]);
    }

    // Libero la memoria
    for (cont = 0; cont < NPALABRAS; cont++) {
        free(palabras[cont]);
    }

    return 0;
}
