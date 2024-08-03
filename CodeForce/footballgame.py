def determine_winner():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    goals = data[1:]
    
    score_count = {}
    
    for team in goals:
        if team in score_count:
            score_count[team] += 1
        else:
            score_count[team] = 1
    
    # The winning team is the one with the maximum goals
    winning_team = max(score_count, key=score_count.get)
    print(winning_team)

# Example usage:
# To test the function locally, you can uncomment the following lines
# and run the code.

# from io import StringIO
# import sys

# test_input = "5\nA\nABA\nABA\nA\nA\n"
# sys.stdin = StringIO(test_input)
# determine_winner()  # Expected Output: A
