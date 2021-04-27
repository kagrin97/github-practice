def check(a):
    for x, y, what in a:
        if what == 0:
            if y == 0 or [x-1, y, 1] in a or [x, y, 1] in a or [x, y-1, 0] in a:
                continue
            else:
                return False
        elif what == 1:
            if [x, y-1, 0] in a or [x+1, y-1, 0] in a or ([x-1, y, 1] in a and [x+1, y, 1] in a):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []

    for x, y, what, how in build_frame:
        if how:
            answer.append([x, y, what])
            if not check(answer):
                answer.remove([x, y, what])
        else:
            answer.remove([x, y, what])
            if not check(answer):
                answer.append([x, y, what])

    answer.sort()

    return answer

n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],
[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

print(solution(n, build_frame))