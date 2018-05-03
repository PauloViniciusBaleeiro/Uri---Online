#include <stdio.h>

int main (void)
{
    int tempo, H, M, S;
    scanf ("%d", &tempo);
    H= tempo/3600;
    M= (tempo-(H*3600))/60;
    S= (tempo-(H*3600)-(M*60));
    printf("%d:%d:%d\n", H, M, S);

    return 0;
}
