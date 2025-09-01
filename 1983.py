# 배열로 학점 나눠주기
grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    score = [] #총점 담아둘 리스트


    for i in range(N):                                  #학생 수 만큼 반복
        mid, fin, ass = map(int, input().split())       # 중간,기말,과제 
        total= 0.35*mid + 0.45*fin + 0.2*ass            #총점 계산
        score.append(total)                             #계산된 총점 리스트에 넣기

same_grade = N // 10                                    #같은 학점을 받는 학생수 구하기

k_score = score[K - 1]                                  #K학생의 학점 지정
sorted_scores = sorted(score, reverse=True)             #점수들 내림차순 정렬  
rank = sorted_scores.index(k_score)                     #K학생의 점수 등수를 위해 인덱스 뽑아 정의

result = grades[rank // same_grade]                     #학점 달아주기[등수(인덱스)에서 같은 학점 학생수 나누면 몇명까지 같은 학점인지 정해진다]

print(f"#{tc} {result}")


# 조건문으로 학점 나눠주기
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    score = [] #총점 담아둘 리스트


    for i in range(N):                                  #학생 수 만큼 반복
        mid, fin, ass = map(int, input().split())       #중간,기말,과제 
        total= 0.35*mid + 0.45*fin + 0.2*ass            #총점 계산
        score.append(total)                             #계산된 총점 리스트에 넣기

    k_score = score[K - 1]                              #k학생 총점
    higher = 0                                          #총점이 더 높은 사람 수
    for s in score:                                     #총점 수 만큼 반복
        if s > k_score:                                 #k학생 총점이 낮을시
            higher += 1                                 #등수 하락(본인보다 높은 인원 추가)

    rank = higher + 1                                   #등수 변수 지정
    same_grade = N // 10                                #같은 학점 수

    if rank <= same_grade * 1:                          #A+. 등수 1 ~ same_grade명.
        grade = "A+"
    elif rank <= same_grade * 2:
        grade = "A0"
    elif rank <= same_grade * 3:
        grade = "A-"
    elif rank <= same_grade * 4:
        grade = "B+"
    elif rank <= same_grade * 5:
        grade = "B0"
    elif rank <= same_grade * 6:
        grade = "B-"
    elif rank <= same_grade * 7:
        grade = "C+"
    elif rank <= same_grade * 8:
        grade = "C0"
    elif rank <= same_grade * 9:
        grade = "C-"
    else:
        grade = "D0"

    print(f"#{tc} {grade}")