# 새로운 불면증 치료법
# 1N 입력 숫자를 리스트로 변환
# 각 N번째 숫자들을 *2 한다.
# 1N의 리스트와 각각의 KN번째까지 리스트를 합친다.
# 정렬한다.
# 리스트의 숫자들이 0부터 9까지 나왔다면 횟수를 센다.
T = int(input())
for t in range(1, T+1):
    N = int(input())
    for i in N:
        N * 2