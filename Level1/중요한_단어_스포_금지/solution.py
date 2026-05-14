def solution(message, spoiler_ranges):
    answer = 0
    
    # Step 1. 단어 파싱
    words = []  # (시작 인덱스, 끝 인덱스, 단어)
    i = 0
    while i < len(message):
        if message[i] != ' ':
            j = i
            while j < len(message) and message[j] != ' ':
                j += 1
            words.append((i, j - 1, message[i:j]))
            i = j
        else:
            i += 1
    
    # step 2. 스포일러 범위에 포함되지 않는 단어를 블랙리스트에 추가
    blacklist  = set()
    for (ws, we, word) in words:
        is_spoiler = any(ws <= re and we >= rs for rs, re in spoiler_ranges)
        if not is_spoiler:
            blacklist.add(word)

    # step 3. 시뮬레이션
    seen = set()
    for (rs, re) in spoiler_ranges:
        for (ws, we, word) in words:
            if ws <= re and we >= rs:  # 이 구간에 걸치는 단어
                if word not in blacklist and word not in seen:
                    answer += 1
                    seen.add(word)

    print(blacklist)
    return answer

# test 예제
# message = "here is muzi here is a secret message"
# spoiler_ranges = [[0, 3], [23, 28]]
# solution(message, spoiler_ranges)