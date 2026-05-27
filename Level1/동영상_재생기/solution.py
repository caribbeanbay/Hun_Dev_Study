def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    # mm:ss -> 초 단위 변환
    def to_sec(time):
        mm, ss = map(int, time.split(":"))
        return mm * 60 + ss
    
    # 초 단위 -> mm:ss 변환
    def to_time(sec):
        return f"{sec // 60:02d}:{sec % 60:02d}"
    
    video = to_sec(video_len) # 영상 길이
    cur = to_sec(pos) # 재생위치
    op_s = to_sec(op_start) # 오프닝 시작
    op_e = to_sec(op_end) # 오프닝 끝
    
    # 오프닝 구간 체크
    def check_opening(cur):
        if op_s <= cur <= op_e:
            cur = op_e
        return cur
    
    # 시작 위치 오프닝 체크
    cur = check_opening(cur)
    
    for cmd in commands:
        if cmd == "prev":
            cur = max(0, cur - 10) # 0 미만 방지
        elif cmd == "next":
            cur = min(video, cur + 10) # 영상 길이 초과 방지
        cur = check_opening(cur)
    
    answer = to_time(cur)
    return answer