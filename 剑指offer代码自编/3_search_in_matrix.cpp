bool find(int* matrix, int cols, int rows, int k)
{
	bool found = True;
	if(matrix != NULL && cols > 0 && rows > 0)
	{
		int row = 0;
		int col = cols - 1;
		while(row < rows && col >= 0)
		{
			if(matrix[row * cols + col] == k)
				break;
			else if(matrix[row * cols + col] > k)
				-- col;
			else
				++ row;
		}
	}
	return found;
}

