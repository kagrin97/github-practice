'''
스택 수열 1874번문제
이번문제는 이해하는데 족히 1시간은 넘게 걸린듯하다 나중에 보면 또까먹을지도..
이문제는 원하는 수열을 만들기위해 [4,3,6,8,7,5,2,1]
공을 스택에 쌓으면서 필요한 수열공이 발견되면 [1,2,3,4 <- 첫번쨰 수열값 발견]
그값을 빼주고 그다음 수열값을 구하기위해 더하고 뺴고 하다가 스택에 쌓은 공들 중에 수열에 필요한
값이 존재하지 않으면 불가능하다고 no를 표시한다. 수열을 완성하면 순서대로 출력한다
'''

n = int(input())  # 공의 개수
s = []  # 1~n 까지 들어갈 공의 하우스
op = []  # push, pop를 기록할 공간
count = 1
temp = True
for i in range(n):  # 공의 개수만큼 반복
    num = int(input())  # 원하는 수열을 입력받음
    while count <= num:  # 공하우스에 원하는 수열값이 나올때까지 넣기
        s.append(count)  # 1부터 계속 넣기
        op.append('+')  # 넣을때마다 push를 기록
        count += 1  # 현재 몇번째 공을 넣었는지 기록
    if s[-1] == num:  # 원하는 수열값이 공하우스 맨마지막에 있으면
        s.pop()  # 그공을 빼서 수열을 하나씩 완성
        op.append('-')  # 뺐으니까 pop을 기록
    else:
        temp = False  # 공을 넣고 빼는 과정중에 필요한 수열 값이 하우스 안에 없을때는 불가능

if temp == False:
    print('NO')
else:
    for i in op:
        print(i)
