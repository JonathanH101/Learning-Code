#include <iostream>
#include <string>


class Object {
    public:
        std::string name;
        double weight;
        Object(std::string n, double w) : name(n), weight(w) {}
        void print() {
            std::cout << "This object is named " << name << " and its weight is " << weight/2.205 << " kgs." << std::endl;
        }

};  

int main() {
    std::string exit;
    std::string name;
    double weight;
    while(name!="!quit") {
        std::cout << "What is its name? (type !quit to quit)" << std::endl;
        std::cin >> name;
        if(name == "!quit") {
            break;
        }
        std::cout << "What is the weight? " << std::endl;
        std::cin >> weight;
        Object* p1 = new Object(name, weight);
        (*p1).print();
        delete p1;
    }

}
