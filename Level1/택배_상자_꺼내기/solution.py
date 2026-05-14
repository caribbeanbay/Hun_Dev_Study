def solution(n, w, num):
    answer = 0

    # step 1. 창고 배열 만들기
    import math
    rows = math.ceil(n / w) # 창고의 행 수 계산
    warehouse = []

    box = 1
    for row in range(rows):
        layer = []
        for col in range(w):
            if box <= n:
                layer.append(box)
                box += 1
            else:
                layer.append(0)  # 빈 칸은 0
        if row % 2 == 1:  # 짝수 층(1, 3, 5...)은 뒤집기
            layer.reverse()
        warehouse.append(layer)

    # step 2. num의 위치 찾기
    for row in range(rows):
        for col in range(w):
            if warehouse[row][col] == num:
                num_row, num_col = row, col
                break

    # step 3. 위에 있는 상자 카운트
    for row in range(num_row, rows):
        if warehouse[row][num_col] != 0:  # 빈 칸이 아니면 카운트
            answer += 1

    return answer

# 확인용
# print(solution(22, 6, 8))
# print(solution(13, 3, 6))