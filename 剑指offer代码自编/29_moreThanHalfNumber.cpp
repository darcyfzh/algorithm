int moreThanHalfNumber(int* numbers, int length)
{
	if(numbers == NULL || length <= 0)
		return 0;
	int middle = length >> 1;
	int start = 0;
	int end = length - 1;
	int index = Partition(numbers, length, start, end);
	while(index ! middle)
	{
		if(middle > index)
		{
			start = index + 1;
			index = Partition(numbers, length, start, end);
		}
		else
		{
			end = index - 1;
		}
	}
	int result = numbers[middle];
}