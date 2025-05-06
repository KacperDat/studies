#include <stdio.h>
#include <stdlib.h>
/*kacper data 179472*/
/*zad1*/
struct Harmoniczny
{
    int n;
    double* values;
};
/*zad2*/
void wyswietlHarmoniczny(struct Harmoniczny h)
{
    if (h.values==NULL)
    {
        return;
    }

    printf("\nharmonczny :");
    for (int i = 0; i < h.n; i++)
    {
        printf("%f ", h.values[i]);
    }

}
/*zad3*/
struct Harmoniczny* stworzHarmoniczny(int n)
{
    struct Harmoniczny* h = (struct Harmoniczny*)malloc(sizeof(struct Harmoniczny));


    h->n = n;
    h->values = (double*)malloc(n * sizeof(double));



    for (int i = 0; i < n; i++)
    {
        h->values[i] = 1.0 / (i + 1);
    }
    return h;
}
/*zad4*/
/*void zaktualizujHarmoniczny(struct Harmoniczny* h, int n)
{
    h->n=n;
    if(h->n==NULL)
    {
        h->values = (double*)malloc(n * sizeof(double));
    }
    for (int i = 0; i < n; i++) {
        h->values[i] = 1.0 / (i + 1);
    }
    return h;

}*/





int main()
{
    int n;

    printf("Podaj liczbe n: ");
    scanf("%d", &n);

    struct Harmoniczny* h = stworzHarmoniczny(n);

    printf("Podaj nowa n:");
    int nowan;
    scanf("%d",&nowan);
    wyswietlHarmoniczny(*h);
    /*  zaktualizujHarmoniczny(*h,nowan);*/
    return 0;
}
