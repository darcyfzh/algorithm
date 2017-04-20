#include <iostream>
using namespace std;
int divide(int divident,int divisor)
{
	if(divisor == 0)
		throw divisor;
	else if(divident == 0)
		return 0;
	bool positive = (divident * divisor > 0);
	int res = 0;
	while(divident >= divisor)
	{
		int temp = divisor;
		int i = 1;
		while(divident >= temp)
		{
		    divident -= temp;
		    res += i;
		    i = i << 1;
		    temp = temp << 1;
		}
	}
    if(!positive)
    	res = -res;
    return res;
}

int main()
{
	int divident;
	int divisor;
	cin >> divident >> divisor;
	int res = divide(divident,divisor);
	cout << res << endl;
	return 0;
}
