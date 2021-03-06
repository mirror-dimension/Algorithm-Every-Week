# 병수님

- 문제 주소 및 접근방법
  - [공통원소 구하기](https://dev-soo-log.tistory.com/21)

```text
1. 두 번의 반복문을 통해 같은 요소의 경우 푸쉬시키고 리턴 시 sort해준다.


```

# 호근님

- 문제 주소 및 접근방법
  - [신규 아이디 추천](https://programmers.co.kr/learn/courses/30/lessons/72410)

```
정규표현식을 이용한 풀이
다른 사람 풀이를 확인하면 다 정규표현식으로 체크 할 수 있음
```

# 태성님

- 문제 주소 및 접근방법
  - [2개 이하로 다른 비트](https://programmers.co.kr/learn/courses/30/lessons/77885)

```text
3가지 케이스로 나뉘어서 구별하였다.
1. 모든 수가 1이면 비트 길이 - 1만큼 2에 제곱한 수를 더한다.
2. 비트의 뒷자리가 11로 끝나면 1의 연속이 끝나는 지점에서 앞자리와 숫자를 바꿔치기 한다.
3. + 1를 한다.
```

# 민호님

- 문제 주소 및 접근방법
  - [2개 이하로 다른 비트](https://programmers.co.kr/learn/courses/30/lessons/77885)

```text
태성님과 함께 풀었습니다. (각자)

저도 노트에 수 많은 경우의 수를 놓고 1시간 동안 고민한 결과,
1. 모든 수가 1이면, 즉 2진수로 바꾸고 0이 없다면, 이진수의 맨 앞자리의 1을 10으로 치환

2. 0(2진수로 바꿔도 0) 또는 앞의 수가 어떻든 이진수의 맨 마지막 자리가 '00' 이라면, 01(0은 1로) 치환

3. 마지막 케이스는 오른쪽에서 부터 01 또는 10이라는 키를 찾아야 합니다.
그래서 temp라는 변수에 이진수를 역정렬하여 담은 후,
3-1 우리가 10이라는 수에서는 11로 바꿔야 하기에 역으로 보면 01이라는 숫자를 11로 바꾸고 다시 역정렬을 해줘야 함.
3-2 01이라는 숫자는 10으로 바꿔야 하기에 역으로 보면 10이라는 숫자를 01로 바꾸고 다시 역정렬.
여기서 우측으로 부터(역정렬 기준으로는) 처음껏만 치환을 해줘야 하기에 replace의 치환 개수를 1로 지정.
```
