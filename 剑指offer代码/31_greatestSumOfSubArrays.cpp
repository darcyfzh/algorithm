int findGreatestSumOfArray(int* data, int length)
{
	if(data == NULL || length <= 0)
		return 0;
	int sum = 0;
	int greatestSum = -10000000;
	for(int i = 0; i < length; ++i)
	{
		if(sum <= 0)
			sum = data[i];
		else
			sum += data[i];
		if(greatestSum < sum)
			greatestSum = sum;
	}
	return greatestSum;
}