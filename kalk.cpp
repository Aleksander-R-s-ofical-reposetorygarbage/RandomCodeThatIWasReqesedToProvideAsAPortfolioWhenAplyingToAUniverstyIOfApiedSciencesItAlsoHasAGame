#include <iostream>
#include <string>
using namespace std;
void wykonajOperacje( int liczba1, string str, int liczba2 )
{
    if( str == "plus" )
    {
        cout << liczba1 + liczba2 << endl;
    } else if( str == "minus" )
    {
        cout << liczba1 - liczba2 << endl;
    } else if( str == "razy" )
    {
        cout << liczba1 * liczba2 << endl;
    } else if( str == "dziel" )
    {
        cout << liczba1 / liczba2 << endl;
    } else
    {
        cout << "Nieznana operacja \"" << str << "\" - nie mozna wykonac obliczen." << endl;
    }
}
int main(){
    int i1; int i2; string a1;
    cin >> i1 >> a1 >> i2;
    wykonajOperacje(i1,a1,i2);
    cin >> i1;
}