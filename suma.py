#include <iostream>

int main() {
    // Declarar variables
    int numero1, numero2, resultado;

    // Solicitar al usuario dos números
    std::cout << "Ingrese el primer número: ";
    std::cin >> numero1;

    std::cout << "Ingrese el segundo número: ";
    std::cin >> numero2;

    // Realizar una operación matemática simple (suma en este caso)
    resultado = numero1 + numero2;

    // Mostrar el resultado
    std::cout << "El resultado de la suma es: " << resultado << std::endl;

    return 0;
}
