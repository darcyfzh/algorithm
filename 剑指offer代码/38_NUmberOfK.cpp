int getFirstK(int* data, int length, int k, int start, int end)
{
	int middleIndex = (start + end) / 2;
	int middleData = data[middleIndex];
	if(middleData == k)
	{
		if(middleIndex == 0 || middleIndex >0 && data[middleIndex - 1] != k)
			return middleIndex;
		else
			end = middleIndex - 1;
	}
	else if(middleData > k)
		end = middleIndex - 1;
	else
		start = middleIndex + 1;
	return getFirstK(data, length, k, start, end);
}

int getLastK(int* data, int length, int k, int start, int end)
{
	int middleIndex = (start + end) / 2;
	int middleData = data[middleIndex];
	if(middleData == k)
	{
		if(middleIndex == length - 1 || middleIndex >0 && data[middleIndex + 1] != k)
			return middleIndex;
		else
			start = middleIndex - 1;
	}
	else if(middleData > k)
		end = middleIndex - 1;
	else
		start = middleIndex + 1;
	return getLastK(data, length, k, start, end);
}

int getNumberOfK(int* data, int length, int k)
{
	int number = 0;
	if(data != NULL || length > 0)
	{
		int first = getFirstK(data, length, k, start, end);
		int last = getLastK(data, length, k, start, end);
		number = last - first
	}
	return number;
}

