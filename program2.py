def decode_message( s: str, p: str) -> bool:

# write your code here
        m=len(s)
        n=len(p)
        dp[0][0]=True
        
        for i in range(1,n+1):
                if p[i-1]=='*':
                        dp[0][i]=dp[0][i-1]
  
        return False