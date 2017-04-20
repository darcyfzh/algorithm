#include <iostream>
#include <vector>
#include <string.h>
using namespace std;
int longestPalindromicSubstring(char* str)
{
	if(str == NULL)
		return 0;
	n = strlen(str);
	vector<vector<int>> dic(n,vector<int>(n));
	for(int j = 0; j < n; j++)
	{
		dic[j][j] = 1;
		for(int i = j - 1; i >= 0; i--)
		{
			if(str[i] = str[j])
				dic[i][j] = dic[i - 1][j - 1] + 2;
			else
				dic[i][j] = max(dic[i - 1][j],dic[i][j - 1]);
		}
	}
	return dic[0][n - 1];
}