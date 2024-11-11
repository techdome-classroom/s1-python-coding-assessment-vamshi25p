def decode_message(s: str, p: str) -> bool:

    # write your code here
    m = len(s)
    n = len(p)
dp[0][0] = True

    for i in range(1, n+1):
        if p[i-1] == '*':
            dp[0][i] = dp[0][i-1]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif p[j-1] == '?' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]

    return dp[m][n]
