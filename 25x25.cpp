#include <iostream>
#include <iomanip>
int s(int a=1,int b=1){
    return a * b;
}
int main(){
    int i;
    int j;
    for (i=1;i<=25;i++){
            for (j=1;j<=25;j++){
                        std::cout << std::setw(3) << s(i,j) << ' ';
            }
            std::cout << std::endl;
    }
std::cin >> j;
return 0;
}
