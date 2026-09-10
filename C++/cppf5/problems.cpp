#include <iostream>

int main() {
    int val = 5;
    int* val1 = &val;
    int* p1 = val1;
    delete val1;
    *p1 = 20;
    std::cout << *val1 << std::endl;
}