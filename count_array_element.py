from itertools import combinations


def solution(n, arr):
    def calculate_score(container1, container2, container3):
        min_score = float('inf')
        for w1 in container1:
            for w2 in container2:
                for w3 in container3:
                    score = abs(w1 - w2) + abs(w2 - w3) + abs(w3 - w1)
                    min_score = min(min_score, score)
        return min_score

    max_score = float('-inf')

    # Loop to try all possible splits
    for c1_size in range(1, n - 1):  # Container 1 should have at least 1 element
        for c1_indices in combinations(range(n), c1_size):  # All combinations for container 1
            remaining_indices = set(range(n)) - set(c1_indices)
            for c2_size in range(1, len(remaining_indices)):  # Container 2 should have at least 1 element
                for c2_indices in combinations(remaining_indices, c2_size):  # All combinations for container 2
                    c3_indices = remaining_indices - set(c2_indices)  # Container 3 gets the remaining elements
                    
                    container1 = [arr[i] for i in c1_indices]
                    container2 = [arr[i] for i in c2_indices]
                    container3 = [arr[i] for i in c3_indices]
                    
                    min_score = calculate_score(container1, container2, container3)
                    max_score = max(max_score, min_score)

    return max_score


n = int(input())
arr = list(map(int,input().split()))  # Ensure this is a list of integers, not a single number
print(solution(n, arr))