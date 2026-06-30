#include <iostream>
#include <iomanip>
int main(){
    int si;
    std::cout << "size:";
    std::cin >> si;
    if (si<0){
        si=0;
    }
    int arr[2][si+1]={0};

    for (int i=0;i<=si;i++){
            for (int j=0;j<=i;j++){
                if (j==0 || j==i){
                    arr[1][j]=1;
                }
                else{
                    arr[1][j]=arr[0][j]+arr[0][j-1];
                }
            }
            std::cout << std::setw(2) << i << " | ";
            for (int j = 0; j <= i; ++j) {
                arr[0][j]=arr[1][j];
                std::cout << std::setw(4) << arr[0][j] << " ";
            }
            std::cout << std::endl;
    }
return 0;
}
