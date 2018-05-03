#include<stdio.h>

int main()
{
double A, B;
{
    scanf("%lf", &A);
    scanf("%lf", &B);
    A=(A/11)*3.5;
    B=(B/11)*7.5;
    printf("MEDIA = %.5f", A+B);
}
return 0;
}
