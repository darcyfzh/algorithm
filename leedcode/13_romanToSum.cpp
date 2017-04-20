#include <string>
#include <map>
int romanToSum(string s)
{
	int sum = 0;
	map<string,int> dic = {{'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}};
	for(int i = 0; i <= strlen(s) - 1; i++)
	{
	    if(str[i] < str[i + 1])
	       sum -= str[i]
	    else
	       sum += str[i + 1]
	}
	sum += str[strlen(s) - 1];
	return sum;
}