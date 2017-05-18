int numberOf1(int n)
{
	int count = 0;
	while(n)
	{
		if(n & 1)
			count ++;
		n = n >> 1;
	}
	return count;
}


int numberOf1(int n)
{
	int count = 0;
	const int flag = 1;
	while(flag)
	{
		if(n & flag)
			count ++;
		flag = flag << 1;
	}
	return count;
}