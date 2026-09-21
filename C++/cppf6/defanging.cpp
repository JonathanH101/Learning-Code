#include <iostream>
#include <string>

std::string defangingvalue(std::string link) {
    std::string str = "";
    for(int i = 0; i < link.length(); i++) {
        if(link[i] != '.') {
            str += link[i];
        } else {
            str += "[.]";
        }
    }
    return str;
}

void defangingref(std::string& link) {
    for(int i = 0; i < link.length(); i++) {
        if(link[i] == '.') {
            link.replace(i,1,"[.]");
            i += 2;
        }
    }
}


int main() {
    std::string link1 = "www.malware.com";
    std::cout << defangingvalue("www.malware.com") << std::endl;
    defangingref(link1);
    std::cout << link1 << std::endl;
}