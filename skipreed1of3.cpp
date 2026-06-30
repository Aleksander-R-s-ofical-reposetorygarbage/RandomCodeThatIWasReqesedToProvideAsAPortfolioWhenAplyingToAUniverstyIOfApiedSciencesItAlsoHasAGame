#include <fstream>
#include <iostream>

int main() {
    std::ifstream file("skipreed1of3.txt");
    if (file.is_open()) {
        char ch;
        while (file.get(ch)) {
            file.seekg(2, std::ios::cur );
            std::cout << ch <<std::endl;
        }
        file.close();
    } else {
        std::cout << "Unable to open file";
    }
    return 0;
}