def solution(keymap, targets):
    answer = [] # 결과를 저장할 리스트
    for target in targets: # 각각의 문자열에 대해
        count = 0 # 누른 횟수를 저장할 변수
        prev = '' # 이전에 누른 문자를 저장할 변수
        for char in target: # 문자열의 각 문자에 대해
            for i in range(len(keymap)): # keymap을 순회하며
                if char in keymap[i]: # 해당 문자가 keymap[i]에 있으면
                    if prev == keymap[i].index(char): # 이전에 누른 문자와 같은 문자를 누르면
                        count += 1 # 누른 횟수를 증가시키지 않음
                    else: # 이전에 누른 문자와 다른 문자를 누르면
                        count += keymap[i].index(char) + 1 # 누른 횟수를 증가시킴
                        prev = keymap[i].index(char) # 이전에 누른 문자를 현재 문자로 변경
                    break # 문자를 찾았으므로 더 이상 순회하지 않음
            else: # 문자를 찾지 못한 경우
                count = -1 # 누를 수 없으므로 -1 저장
                break # 더 이상 순회하지 않음
        answer.append(count) # 결과 리스트에 누른 횟수 추가
    return answer # 결과 반환