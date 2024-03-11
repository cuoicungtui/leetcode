def wordBreak(string, words):
    n = len(string)
    dp = [False for i in range(n + 1)]
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if dp[j] and string[j:i] in words:
                dp[i] = True
                break

    if dp[n]:
        result = []
        i = n
        while i > 0:
            for j in range(i - 1, -1, -1):
                if dp[j] and string[j:i] in words:
                    result.append(string[j:i])
                    i = j
                    break
        return result[::-1]
    else:
        return None
s = "bedbathandbeyond"
#print(wordBreak(s, [ 'bed', 'bath', 'bedbath', 'and', 'beyond']))


def swap_bits(num):
    return int(''.join(['1' if x == '0' else '0' for x in bin(num)[2:][::-1]]), 2)
print(swap_bits(170))
