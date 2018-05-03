#include<stdio.h>
#include<math.h>

int main ()
{
    double A, B, C, Pi=3.14159;
    {
        scanf("%lf""%lf""%lf", &A, &B, &C);
        printf("TRIANGULO: %.3f\nCIRCULO: %.3f\nTRAPEZIO: %.3f\nQUADRADO: %.3f\nRETANGULO: %.3f\n", (A*C)/2.0, (C*C)*Pi, ((A+B)*C)/2.0, B*B, A*B);
    }
}
