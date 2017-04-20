#include <vector>
#include <string>
int lengthOfLongestSubstring(string s)
{
    vector<int> dic(256,-1);
    int start = maxLen = 0;
    for(int i = 0; i < strlen(s); ++i)
    {
        if(dic[s[i]] >= start)
            start = dic[s[i]] + 1;
        maxLen = max(maxLen,i - start + 1);
        dic[s[i]] = i;
    }
    return maxLen;
}