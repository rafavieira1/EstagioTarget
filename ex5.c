#include <stdio.h>
#include <string.h>

void inverter_string(char *str) {
    int inicio = 0;
    int fim = strlen(str) - 1;
    char temp;
    
    while (inicio < fim) {
        temp = str[inicio];
        str[inicio] = str[fim];
        str[fim] = temp;
        inicio++;
        fim--;
    }
}

int main() {
    char str[100];
    
    printf("Digite a string que deseja inverter: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';
    inverter_string(str);
    printf("String invertida: %s\n", str);
    return 0;
}