#include <string> 
#include <iostream>

int main() {
    for (int i = 0; i <=10; i++) {
        std::cout << i << std::endl;
    }

    for (int i = 2; i <=10; i+=2) {
        std::cout << i << std::endl;
    }

    for (int i = 10; i >=1; i--) {
        std::cout << i << std::endl;
    }

    std::string word; 
    std::cin >> word;
     
    for (int i = 0; i <= int(word.length()) - 1; i++) {
        std::cout << word[i] << std::endl;
    }

    for (int i = word.length(); i >= 1; i--) {
        std::cout << word[i-1] << std::endl;
    }    

    int total = 0;
    for (int i = 0; i <= 100; i++) {
        total += i;
    }
    std::cout << total << std::endl;

    total = 1;
    for (int i = 1; i <= 10; i++) {
        total *= i;
    }
    std::cout << total << std::endl;

}