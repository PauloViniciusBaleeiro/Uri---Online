#include <stdio.h>

int main (void)
{
    int T=0, A=0, M=0, D=0;

    scanf("%d", &T);
    A=T/365;
    M=(T-(A*365))/30;
    D=(T-(A*365)-(M*30));
    printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", A, M, D );
    return 0;
}
