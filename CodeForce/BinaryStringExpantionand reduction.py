def smallest_original_length(s):
    left = 0
    right = len(s) - 1
    
    while left < right and s[left] != s[right]:
        left += 1
        right -= 1
    
    return right - left + 1

def solve():
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        results.append(smallest_original_length(s))
    
    for result in results:
        print(result)

solve()