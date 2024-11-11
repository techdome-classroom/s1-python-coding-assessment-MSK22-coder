def decode_message( s: str, p: str) -> bool:
        m, n = len(message), len(decoder_key)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

    # Initialize first row for patterns that can match an empty message
        for j in range(1, n + 1):
                if decoder_key[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]

    # Fill the DP table
        for i in range(1, m + 1):
                for j in range(1, n + 1):
                        if decoder_key[j - 1] == '*':
                        dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                        elif decoder_key[j - 1] == '?' or decoder_key[j - 1] == message[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
# write your code here
  
     