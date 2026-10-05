#include <iostream>
#include <string>

int totalBalance(int all[], int size);


int main() {
    std::cout << "How many transactions have you made in the past month? " << std::endl;
    int input;
    int transaction;
    std::cin >> input;
    int transactions[input];
    for(int i = 0; i < input; i++) {
        std::cout << "Please enter in your transaction. " << std::endl;
        std::cin >> transaction;
        transactions[i] = transaction;
    }

    std::cout << totalBalance(transactions, input) << std::endl;
}

int totalBalance(int all[], int size) {
    int total = 0;
    for(int i = 0; i<size; i++) {
        total += all[i];
    }
    return total;
}