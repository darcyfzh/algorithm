void KLeastNumber(int* input, int length, int* output, int k)
{
	if(input == NULL || length <= 0)
		return;
	int start = 0;
	int end = length - 1;
	int index = Partition(input, length, start, end);
	while(index != k)
	{
		if(index < k - 1)
		{
			start = index + 1;
			index = Partition(input, length, start, end);
		}
		else
		{
			end = index - 1;
			index = Partition(input, length, start, end);
		}
	}
	for(int i =0; i < k; ++i)
	{
		output[i] = input[i];
	}
}


typedef multiset<int, greater<int> > intset;
typedef multiset<int, greater<int> >:: iterator setIter;
void getLeastNumber(vector<int> &data, intset &leastNumber, int k)
{
	if(data.size() < k || k < 1)
		return;
	vector<int>:: iterator iter = data.begin();
	for(; iter != data.end(); ++iter)
	{
		if(leastNumber.size() < k)
			leastNumber.insert(*iter);
		setIter greatest = leastNumber.begin();
		if(*iter < *greatest)
		{
			leastNumber.erase(greatest);
			leastNumber.insert(*iter);
		}
	}
}
