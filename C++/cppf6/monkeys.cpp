#include <iostream>
#include <string>

void monkeys(std::string& word);

std::string monkeysvalue(std::string word) {
    int len = word.length();
    for(int i=0;i<len;i++) {
        word.insert(rand()%word.length(),1,char(97+(rand()%26)));
    }
    return word;
}

std::string monkeysconst(const std::string& word3) {
    std::string word = word3;
    int len = word.length();
    for(int i=0;i<len;i++) {
        word.insert(rand()%word.length(),1,char(97+(rand()%26)));
    }
    return word;
}

int main() {
    srand(time(0));
    std::string word2 = "bananas";
    monkeys(word2);
    std::cout << word2 << std::endl;
    std::cout << monkeysvalue(word2) << std::endl;
    std::cout << monkeysconst(word2) << std::endl;
        
}

void monkeys(std::string& word) {
    int len = word.length();
    for(int i=0;i<len;i++) {
        word.insert(rand()%word.length(),1,char(97+(rand()%26)));
    }
}


//char(97)
//insert(int index, int quantity, char newChar)
