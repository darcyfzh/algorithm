void permutation(char* str)
{
	if(str == NULL)
		return 
	support(str, str);
}

void support(char* str, char* pBegin)
{
	if(*pBegin == '\0')
		cout << str << endl;
	else
	{
		for(char* pch = pBegin; pch != '\0'; ++pch)
		{
			char temp = *pch;
			*pch = *pBegin;
			*pBegin = temp;
			support(str, pBegin + 1);
			temp = *pch;
			*pch = *pBegin;
			*pBegin = temp;
		}
	}
}