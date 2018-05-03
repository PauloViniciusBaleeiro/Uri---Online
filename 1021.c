#include<stdio.h>

int main (void)
{
    int cem, cinq, vinte, dez, cinco, dois, um;
    int aux, moedas;
    double val;

    scanf("%f", &val);
    aux = val;
    //moedas = val - aux;
    cem = aux/100;
    aux = aux%100;
    cinq = aux/50;
    aux = aux%50;
    printf("%d, %d", cem, cinq)




}
