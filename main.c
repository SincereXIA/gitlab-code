#include <stdio.h>

int main(){
    char a;
    int i;
    a = 'b';
    // printf("%d", a);
    i = a;
    // printf("%d", i);
    func(&i);
    printf("%d", &i);
    func2(i);
    printf("%d", i);
}


int func(int *a) {
    printf("%d", a);
    *a = 100;
}

int func2(int a) {
    a = 0;
}