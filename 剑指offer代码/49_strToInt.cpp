int strToInt(char* a)
{
	if(a != NULL and *a != '\0')
	{
		bool positive = true;
		int num = 0;
		if(*a == '+')
			a++;
		if(*a == '-')
			positive = false;
			a++;
		if(*a != '\0')
			num = strToIntCore(a, positive);
	}
	return sum;
}

int strToIntCore(char* a, bool positive)
{
	int i = 0;
	int num = 0;
	while(*a != '\0')
	{
		if(*a >= '0' and *a <= '9')
		{
			int flag = positive ? 1 : -1;
			num = num * 10 + flag * (*a - '0');
			a++;
		}
		else
		{
			num = 0;
			break;
		}
	}
	return num;
}