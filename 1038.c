#include<stdio.h>

int main ()
{
    int Qtd=0, Cod=0;
    float V1=4.00, V2=4.50, V3=5.00, V4=2.00, V5=1.50, tot=0;

    scanf ("%d", &Cod);
    scanf("%d", &Qtd);
    /*printf ("%d", Qtd);
    printf ("%d", Cod);*/
    switch (Cod)
    {
    case 1 :
        tot = V1*Qtd;
    break;

    case 2 :
        tot = V2*Qtd;
    break;

    case 3 :
        tot = V3*Qtd;
    break;

    case 4 :
        tot = V4*Qtd;
    break;

    case 5 :
        tot = V5*Qtd;
    break;
    }
    printf("Total: R$ %.2f\n", tot);
    return 0;
}
