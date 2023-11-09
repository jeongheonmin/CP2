n, m = map(int,input().split()) #행,열 개수 입력받기
lst = []
for _ in range(n):
    while True:
        row = list(map(int, input().split()))

        if len(row) == m:
            lst.append(row)
            break
        else:
            print("행의 갯수가 잘못 입력되었습니다. 다시 입력해주세요. ")
def dog_meal(matrix):

    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    #값 저장할 리스트
    dp = [[0] * cols for _ in range(rows)]

    #각 위치별 지나간 길 저장할 리스트
    path = [[[] for _ in range(cols)] for _ in range(rows)]

    path[0][0] = [(0,0)]
    dp[0][0] = matrix[0][0]

    #첫 행 초기화
    for i in range(1,cols):
        dp[0][i] = dp[0][i-1] + matrix[0][i]
        path[0][i] = path[0][i-1] + [(0,i)]

    #첫 열 초기화
    for i in range(1,rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        path[i][0] = path[i-1][0] + [(i,0)]

    #길마다 최대 값 저장
    for i in range(1,rows):
        for j in range(1,cols):
            if dp[i-1][j] > dp[i][j-1]: #위에서 오는 경우
                dp[i][j] = dp[i-1][j] + matrix[i][j]
                path[i][j] = path[i-1][j] + [(i,j)] # 경로 저장
            else:                       #왼쪽에서 오는 경우
                dp[i][j] = dp[i][j-1] + matrix[i][j]
                path[i][j] = path[i][j-1] + [(i,j)] # 경로 저장
    result = path[rows-1][cols-1]
    return result

print(dog_meal(lst))