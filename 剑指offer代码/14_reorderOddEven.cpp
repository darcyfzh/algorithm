void reOrderOddEven(int* data, int length)
{
	if(data == NULL || length == 0)
		return;
	int* begin = data;
	int* end = data + length - 1;
	while(begin < end)
	{
		while(*begin % 2 != 0)
			begin ++;
		while(*end %2 == 0)
			end --;
		if(begin < end)
		{
			int temp = *begin;
			*begin = *end;
			*end = temp;
		}
	}
}