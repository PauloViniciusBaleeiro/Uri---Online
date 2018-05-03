//FALTA CONSERTAR

#include <stdio.h>

int main()
{
int ent[3], i, p=0, j;
int ord[3];
    scanf("%d%d%d", &ent[0], &ent[1], &ent[2]);

    for (i=0;i<3;i++){
        ord[i]= ent[i];
    }
    i=0;
    for(j=3-1;j>1;j--){
        for (i=0;i<3;i++){
        if (ord[i]> ord[i+1])
            p = ord[i];
            ord[i] = ord[i+1];
            ord[i+1] = p;
        }
    }
    i=0;
    for(i=0;i<3;i++){
        printf("%d\n", ord[i]);
    }
    printf("\n");
    i=0;
    for(i=0;i<3;i++){
    printf("%d\n", ent[i]);
    }

}
