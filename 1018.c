#include<stdio.h>

int main ()
{
    int result, ced[7];

        scanf("%d",&result);
        printf("%d\n",result);
        ced[0]=result/100;
        result=result-(ced[0]*100);
        ced[1]=result/50;
        result=result-(ced[1]*50);
        ced[2]=result/20;
        result=result-(ced[2]*20);
        ced[3]=result/10;
        result=result-(ced[3]*10);
        ced[4]=result/5;
        result=result-(ced[4]*5);
        ced[5]=result/2;
        result=result-(ced[5]*2);
        ced[6]=result/1;




    printf("%d nota(s) de R$ 100,00\n"
           "%d nota(s) de R$ 50,00\n"
           "%d nota(s) de R$ 20,00\n"
           "%d nota(s) de R$ 10.00\n"
           "%d nota(s) de R$ 5.00\n"
           "%d nota(s) de R$ 2.00\n"
           "%d nota(s) de R$ 1.00\n", ced[0], ced[1], ced[2], ced[3], ced[4], ced[5], ced[6]);


    return 0;

}
