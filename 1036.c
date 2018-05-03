#include<stdio.h>
#include<math.h>

int main(void)
{

    double A=0, B=0, C=0, delta=0, R1=0, R2=0; {
    scanf("%lf%lf%lf", &A, &B, &C);

    delta = (pow(B,2)-(4*A*C));
    if ((A != 0) && (delta>=0)){
        R1 = (((-1)* B) + sqrt(delta))/(2*A);
        R2 = (((-1)* B) - sqrt(delta))/(2*A);
        printf("R1 = %.5lf\nR2 = %.5lf\n", R1, R2);

    }
    else{
        printf("Impossivel calcular");
    }
    }


}
