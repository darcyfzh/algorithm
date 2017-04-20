#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
int longest(string str)
{
    vector<int>dp(str.length() + 1,0);
    stack<int>stack1;
    int p;
    for(int i = 0;i < str.length(); ++i)
    {
        if(str[i] == '(')
            stack1.push(i);
        else
            if(!stack1.empty())
                p = stack1.top();
                stack1.pop();
                dp[i + 1] = dp[p] + i - p + 1;
    }
    vector<int>::iterator max = max_element(dp.begin(),dp.end());
    return *max;
}

bool compare(int a, int b)
{
	return a > b;
}
int main()
{
    string s;
    cin >> s;
    int maximum = longest(s);
    cout << maximum << endl;
    return 0;
}
