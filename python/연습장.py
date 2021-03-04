from itertools import combinations 
from collections import defaultdict

def solution(infos, queries):
    answer = []
    info_dict = defaultdict(list) # 딕셔너리 value의 default를 list로 설정
    for info in infos:
        info = info.split()
        info_key = info[:-1] # 점수를 제외
        info_val = int(info[-1]) # 점수
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)
                # 총 16가지 조합을 만듦 왜냐하면 한가지 info가 있을때 통과가 가능한 조합이
                # 총 16가지가 되기때문이다
                # 해설 사이트  https://velog.io/@study-dev347/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%EA%B2%80%EC%83%89
                  
    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.split(" ")
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3):
            query.remove('and')
        while '-' in query:
            query.remove('-')
        tmp_q = ''.join(query)
        
        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        
        else:
            answer.append(0)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))

