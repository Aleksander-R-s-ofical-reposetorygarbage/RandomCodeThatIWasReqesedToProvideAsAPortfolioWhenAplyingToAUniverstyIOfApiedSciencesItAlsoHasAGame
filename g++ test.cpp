#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    string o;
    vector<string> msg{"halo","c++","from","AR"};
    for (const string &word : msg)
    {
        cout << word << " ";
    }
    cout << endl;
    cin >> o;
}