#include <stdio.h>
int main()
{
    int x = 8;
    int y = 7;
    x++;
    x += --y;

    printf("x=:%d", x);
    
}