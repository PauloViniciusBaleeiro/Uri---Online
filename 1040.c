#include<stdio.h>

int main ()
{
    double n1, n2, n3, n4, n5, media, nmedia;
    scanf("%lf%lf%lf%lf", &n1, &n2, &n3, &n4);
    media = ((n1*2)+(n2*3)+(n3*4)+n4)/10;
    printf("Media: %.1f\n", media);
    if (media>=7)
        printf("Aluno aprovado.\n");
    else if (media>=5){
        printf("Aluno em exame.\n");
        printf("Nota do exame: ");
        scanf("%lf", &n5);
        media = (media + n5)/2;

            if (media>=5)
                printf("Aluno aprovado.\nMedia final: %.1f\n", media);
            else
                printf("Aluno reprovado.\nMedia final: %.1f\n", media);

    }
    else
        printf("Aluno reprovado.\n");

    return 0;
}
