//最长公共子序列长度
//伪代码
longestCommonSubSequence(x,y)
    m = x.length()
    n = y.length()
    c = [[]]
    for i in 0 to m - 1
        for j in 0 to n - 1
            c[i][j] = 0
    for i in 0 to m - 1
        for j in 0 to n - 1
            if x[i] == y[j]
                c[i][j] = c[i - 1][j - 1] + 1
            elseif c[i][j - 1] >= c[i - 1][j]
                c[i][j] = c[i][j - 1]
            else
                c[i][j] = c[i - 1][j]
    return c[m][n]