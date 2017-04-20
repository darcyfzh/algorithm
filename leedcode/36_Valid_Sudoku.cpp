#include <vector>
#include <map>
#include <iostream>
using namespace std;
bool isValid(vector<vector<char>> &board)
{
	for(int i = 0; i < 9; ++i)
	{
		unordered_map<char,bool> dic1;
		unordered_map<char,bool> dic2;
	    unordered_map<char,bool> dic3;
	    for(int j = 0; j < 9; ++j)
	    {
	    	if(board[i][j] != '.')
	        {
	        	if(dic1[i][j] == true)
	        		return false;
	        	dic1[i][j] == true;
	        }
	        if(board[j][i] != '.')
	        {
	        	if(dic2[i][j] == true)
	        	    return false;
	        	dic2[j][i] == true;
	        }
	        if(board[i/3*3+j/3][i%3*3+j%3] != '.')
	        {
	        	if(dic3[i/3*3+j/3][i%3*3+j%3] == true)
	        		return false;
	        	dic3[i/3*3+j/3][i%3*3+j%3] == true;
	        }
	    }
	}
	return true;
}

int main()
{
	vector<vector<char>> board;
	for(int i = 0; i < 9; ++i)
	{
		for(int j = 0; j < 9; ++j)
		    cin >> board[i][j];
	}
	bool result;
	result = isValid(board);
	return result;
}

