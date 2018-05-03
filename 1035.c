#include<stdio.h>

int main (void)
{
    int A, B, C, D;
    {

        scanf ("%i", &A);
        scanf ("%i", &B);
        scanf ("%i", &C);
        scanf ("%i", &D);

        if ((B>C)&&(D>A) && ((C+D)>(A+B)) && ((C>0) && (D>0)) && (A%2 == 0)) {
            printf("Valores aceitos\n");
        }
        else{
            printf("Valores nao aceitos\n");
        }

        return 0;
    }
}
