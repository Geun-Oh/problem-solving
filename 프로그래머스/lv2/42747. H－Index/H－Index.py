def solution(citations):
    h = 0
    while True:
        cnt = 0
        for i in citations:
            if i >= h:
                cnt += 1
        if cnt >= h:
            h += 1
        else:
            h -= 1
            break
    
    return h