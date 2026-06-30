#include <iostream>
#include <iomanip>
int s(int a=1,int b=1){
    return a * b;
}
int main(){
    int i;
    int j;
    int si;
    std::cout << "size:";
    std::cin >> si;
    if (si<1){
        std::cout << "min is 1" << std::endl;
        si=1;
    }
    else if (si>31){
            si=31;
        std::cout << "max is 31" << std::endl;
    }
    std::cout << "    ";
    for (int q=1;q<=si;q++){
        std::cout << std::setw(3) << q << ' ';
    }
    std::cout << std::endl << "    ";
    for (int l=1;l<=si;l++){
        std::cout << "----";
    }
    std::cout << "--" << std::endl;
    for (i=1;i<=si;i++){
            std::cout << std::setw(2) << i <<" | ";
            for (j=1;j<=si;j++){
                        std::cout << std::setw(3) << s(i,j) << ' ';
            }
            std::cout << " |" << std::endl;
    }
    std::cout << "    --";
    for (int y=1;y<=si;y++){
        std::cout << "----";
    }
    std::cout << std::endl << "tipe a number and hit enter to end.";
    std::cin >> j;
return 0;
}
