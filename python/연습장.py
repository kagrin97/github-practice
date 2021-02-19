def solution(n, stages):
    result = {}
    num_people = len(stages)
    for i in range(1, n + 1):
        if num_people != 0:
            count = stages.count(i)
            result[i] = count / num_people
            num_people -= count
        else:
            result[i] = 0

    return sorted(result, key=lambda x : -dict[x])

n = 5
a1 = [2, 1, 2, 6, 2, 4, 3, 3]	
print(solution(n, a1))



