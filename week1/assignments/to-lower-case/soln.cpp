#include <string>
#include <locale>
#include <iostream>

using namespace std;

class Solution {
    public:
        string toLowerCase(string s) {
            locale loc;
            string test = "";
            for (string::size_type i = 0; i < s.length(); i++)
                test += tolower(s[i], loc);
            return test;
        }
};

int main(int argc, char* argv[]) {
    Solution soln;

    cout << soln.toLowerCase("aBcDeFgHiJ") << endl;
    cout << soln.toLowerCase("abcdefg") << endl;
    cout << soln.toLowerCase("ABCDEFG") << endl;

    return 0;
}