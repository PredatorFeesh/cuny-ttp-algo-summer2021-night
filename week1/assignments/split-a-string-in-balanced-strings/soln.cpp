#include <iostream>
#include <string>

using namespace std;

class Solution {
    public:
        int balancedStringSplit(string s) {
            // A few points
            // Since we are using substrings, once a substring is used it is not reused
            // Thus this problem becomes similar to balancing parenthesis
            int count = 0;
            int lrbal = 0;
            for (string::size_type i = 0; i < s.length(); i++) {
                if (s[i] == 'L')
                    lrbal += 1;
                else
                    lrbal -= 1;
                    
                if (lrbal == 0)
                    count += 1;
            }
            
            return count;
                
        }
};

int main(int argc, char* argv[]) {
    Solution soln;

    cout << soln.balancedStringSplit("RLRRLLRLRL") << endl;
    cout << soln.balancedStringSplit("RLLLLRRRLR") << endl;
    cout << soln.balancedStringSplit("LLLLRRRR") << endl;
    cout << soln.balancedStringSplit("RLRRRLLRLL") << endl; 

    return 0;
}