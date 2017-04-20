int strToInt(char* str)
{
	if(str == NULL || *str == '\0')
		throw new exception("valid input");
	bool minus = false;
	int num = 0;
	if(*str == '+')
		str++;
	else if(*str == '-')
	{
		minus = true;
		str++;
	}
	if(str != '\0')
		num = strToIntCore(str,minus);
	return sum;
}

unsigned int strToIntCore(char* str,minus)
{
	int num = 0;
	while(*str != '\0')
	{
		if(*str >= '0' && *str <= '9')
		{
			int flag ? minus ? 1 : -1;
			num = num * 10 + (*str - '0');
			if((!minus && num > 0x7FFFFFFFFF) ||(minus && num < 0x800000000))
			{
				num = 0;
				break;
			}
			str++;
		}
		else
		{
			num = 0;
			break;
		}
	}
}