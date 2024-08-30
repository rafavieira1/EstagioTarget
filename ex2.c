#include <stdio.h>

int main() {
    int num, a = 0, b = 1, fib = 0;

    printf("Informe um número: ");
    scanf("%d", &num);

    if (num == 0 || num == 1) {
        printf("O número %d pertence à sequência de Fibonacci.\n", num);
        return 0;
    }

    while (fib < num) {
        fib = a + b;
        a = b;
        b = fib;
    }

    if (fib == num) {
        printf("O número %d pertence à sequência de Fibonacci.\n", num);
    } else {
        printf("O número %d NÃO pertence à sequência de Fibonacci.\n", num);
    }

    return 0;
}