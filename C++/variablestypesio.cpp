#include <iostream>
#include <string>

//type varName = value;

int main() {
    // int test = 5;
    // float test2 = 5.5;
    // bool test4 = true;
    std::string test5 = "abcghi";
    std::string test6 = "def";
    std::string test7 = "hello";
    double test3 = 5.555555555555555; 
    std::cout << (int) test3 << std::endl;
    std::cout << test5 + test6 << std::endl;
    std::cout << test5.insert(3, test6) << std::endl;
    std::cout << test7.insert(4, 3, 'o') << std::endl;
    std::cout << "Enter your name:" << std::endl;
    std::string name;
    std::cin >> name;
    std::cout << "Hello, " + name + "!" << std::endl;
    return 0;
}