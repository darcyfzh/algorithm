char first(char* string)
{
	if(string == NULL)
		return '\0';
	const int hashSize = 256;
	int hashTable[hashSize];
	for(int i = 0; i < hashSize; ++i)
		hashTable[i] = 0;
	char* pKey = string;
	while(*pKey != '\0')
	{
		hashTable[*pKey] ++;
		pKey++; 
	}
	pKey = string;
	while(*pKey != '\0')
	{
		if(hashTable[*pKey] == 1)
			return *pKey;
		pKey++
	}
	return '\0';
}