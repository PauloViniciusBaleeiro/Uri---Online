#include<stdio.h>

int main()
{
double A, B, C;
{
    scanf("%lf", &A);
    scanf("%lf", &B);
    scanf("%lf", &C);
    A=(A/10)*2;
    B=(B/10)*3;
    C=(C/10)*5;
    printf("MEDIA = %.1f\n", A+B+C);
}
return 0;
}
