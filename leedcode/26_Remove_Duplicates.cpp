#include <iostream>
using namespace std;
int remove(int nums[], int length)
{
	if(nums == NULL or length <= 0)
		return 0;
	int tail = 1;
	for(int i = 1; i < length; ++i)
	{
		if(nums[i - 1] != nums[i])
		{
			tail ++; 
		}
	}
	return tail;
}

int main()
{
    int length;
    cin >> length;
    int nums[length];
    for(int i = 0; i < length; i++)
    {
    	cin >> nums[i];
    }
    int result = remove(nums,length);
    cout << result << endl;
    return 0;
}