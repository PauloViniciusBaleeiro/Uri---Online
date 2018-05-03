#include<stdio.h>
#include<math.h>

int main ()
{
double X1=0.0, Y1=0.0, X2=0.0, Y2=0.0, result=0.0;
    {
    scanf("%lf""%lf""%lf""%lf", &X1, &Y1, &X2, &Y2);
    result=sqrt(pow((X2-X1),2)+pow((Y2-Y1),2));
    printf("%.4f", result);
    }
return 0;
}
