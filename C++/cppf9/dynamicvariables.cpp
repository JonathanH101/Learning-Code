#include <iostream>
#include <string>

int main() {
    int* p1 = new int;
    std::cin >> *p1;
    std::cout << *p1 << std::endl;
    delete p1;
}