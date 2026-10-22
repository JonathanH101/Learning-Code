#include <iostream>
#include <string>

int main() {
    std::string name;
    std::cout << "Please input your name. " << std::endl;
    std::cin >> name;
    std::cout << "Welcome " + name + "!" << std::endl;

    int array[3][5];
    std::cout << "Please put the starting balance. " << std::endl;
        std::cin >> array[0][2];
    for(int i = 0; i < 3; i++) {
        std::cout << "You have " << 3-i << " transactions remaining." << std::endl;
        std::cout << "Please put the date. " << std::endl;
        std::cin >> array[i][1];
        std::cout << "Please put the transaction amount. " << std::endl;
        std::cin >> array[i][3];
        if(i != 0) {
            array[i][2] = array[i-1][4];
        }
        array[i][0] = i;
        array[i][4] = array[i][2] + array[i][3];
        


        std::cout << "TRANSACTION NO: " << array[i][0] << std::endl;
        std::cout << "DATE: " << array[i][1] << std::endl;
        std::cout << "STARTING BALANCE: " << array[i][2] << std::endl;
        std::cout << "AMOUNT: " << array[i][3] << std::endl;
        std::cout << "ENDING BALANCE: " << array[i][4] << std::endl;
    }
    std::cout << "Thank you for entering your transactions for this pay period! Your transaction breakdown is below:" << std::endl << std::endl;
    for(int i = 0; i < 3; i++) {
        std::cout << "TRANSACTION NO: " << array[i][0] << std::endl;
        std::cout << "DATE: " << array[i][1] << std::endl;
        std::cout << "STARTING BALANCE: " << array[i][2] << std::endl;
        std::cout << "AMOUNT: " << array[i][3] << std::endl;
        std::cout << "ENDING BALANCE: " << array[i][4] << std::endl << std::endl;
    }
  


}