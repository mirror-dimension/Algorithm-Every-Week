# 병수님

```text
1. [큰 수 출력하기]
N(1<=N<=100)개의 정수를 입력받아, 자신의 바로 앞 수보다 큰 수만 출력하는 프로그램을 작 성하세요.(첫 번째 수는 무조건 출력한다)
▣ 입력설명
첫 줄에 자연수 N이 주어지고, 그 다음 줄에 N개의 정수가 입력된다.
▣ 출력설명
자신의 바로 앞 수보다 큰 수만 한 줄로 출력한다.
▣ 입력예제 1 6
7 3 9 5 6 12
▣ 출력예제 1 7 9 6 12
```

-   접근 방법

```text
반복문을 돌려 그 안에 조건으로 인덱스를 비교해 바로 전의 인덱스보다 큰 경우에만 새로운 배열에 push 한다.
```

```text
2. [보이는 학생]
선생님이 N(1<=N<=1000)명의 학생을 일렬로 세웠습니다. 일렬로 서 있는 학생의 키가 앞에 서부터 순서대로 주어질 때, 맨 앞에 서 있는 선생님이 볼 수 있는 학생의 수를 구하는 프로그 램을 작성하세요. (앞에 서 있는 사람들보다 크면 보이고, 작거나 같으면 보이지 않습니다.)
▣ 입력설명
첫 줄에 정수 N이 입력된다. 그 다음줄에 N명의 학생의 키가 앞에서부터 순서대로 주어진다.
▣ 출력설명
선생님이 볼 수 있는 최대학생수를 출력한다.
▣ 입력예제 1
8
130 135 148 140 145 150 150 153
▣ 출력예제 1 5
```

-   접근 방법

```text
- 맨 앞에 서 있는 선생님이 볼 수 있는 학생의 수는 자기 앞에 있는 학생들보다 큰 경우의 수와 같다.
- 초기값 0번 인덱스(맨 앞이라 보인다)가 포함된 배열과 max라는 변수에 0번째 인덱스를 할당한다.
- n명의 학생들을 반복문을 돌리고
- 조건으로 해당 인덱스가 max값보다 크다면 max값을 해당 인덱스의 값으로 다시 할당하고
answer의 값에 해당 값을 push한다.
- 최종적으로 answer의 length값을 리턴한다.
```

```text
3. [가위 바위 보]
A, B 두 사람이 가위바위보 게임을 합니다. 총 N번의 게임을 하여 A가 이기면 A를 출력하고, B가 이기면 B를 출력합니다. 비길 경우에는 D를 출력합니다.
가위, 바위, 보의 정보는 1:가위, 2:바위, 3:보로 정하겠습니다.
예를 들어 N=5이면
두 사람의 각 회의 가위, 바위, 보 정보가 주어지면 각 회를 누가 이겼는지 출력하는 프로그램 을 작성하세요.
▣ 입력설명
첫 번째 줄에 게임 횟수인 자연수 N(1<=N<=100)이 주어집니다. 두 번째 줄에는 A가 낸 가위, 바위, 보 정보가 N개 주어집니다. 세 번째 줄에는 B가 낸 가위, 바위, 보 정보가 N개 주어집니다.
▣ 출력설명
각 줄에 각 회의 승자를 출력합니다. 비겼을 경우는 D를 출력합니다.
▣ 입력예제 1 5
23313 11223
▣ 출력예제 1 A
B
A
B D
```

-   접근 방법

```text
- A가 낸 정보, B가 낸 정보를 인자로 받는 가위 바위 보라는 함수를 만든다.
- 가위바위보 함수에는 A의 입장에서 같을 때 'D'를 리턴하고 가위, 바위, 보 각각의 case일때 이기는 경우의 수일때 조건으로 'A'를 리턴하고 그 외의 경우 'B'를 리턴하게 로직을 짠다.
- n번의 반복문을 돌려 i번째 인덱스에서 A,B가 각각 낸 값을 가위바위보 함수에 인자로 넣고 리턴된 값을 배열에 넣는다.
```

```text
4. [점수 계산]
OX 문제는 맞거나 틀린 두 경우의 답을 가지는 문제를 말한다. 여러 개의 OX 문제로 만들어진 시험에서 연속적으로 답을 맞히는 경우에는 가산점을 주기 위해서 다음과 같이 점수 계산을 하기 로 하였다. 1번 문제가 맞는 경우에는 1점으로 계산한다. 앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점으로 계산한다. 또한, 연속으로 문제의 답이 맞는 경우에서 두 번째 문제는 2점, 세 번째 문제는 3점, ..., K번째 문제는 K점으로 계산한다. 틀린 문제는 0점으로 계 산한다.
예를 들어, 아래와 같이 10 개의 OX 문제에서 답이 맞은 문제의 경우에는 1로 표시하고, 틀린 경 우에는 0으로 표시하였을 때, 점수 계산은 아래 표와 같이 계산되어, 총 점수는 1+1+2+3+1+2=10 점이다.
1011100110
시험문제의 채점 결과가 주어졌을 때, 총 점수를 계산하는 프로그램을 작성하시오.
▣ 입력설명
첫째 줄에 문제의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 N개 문제의 채점 결과를 나 타내는 0 혹은 1이 빈 칸을 사이에 두고 주어진다. 0은 문제의 답이 틀린 경우이고, 1은 문제의 답이 맞는 경우이다.
▣ 출력설명
첫째 줄에 입력에서 주어진 채점 결과에 대하여 가산점을 고려한 총 점수를 출력한다.
▣ 입력예제 1
10 1011100110
▣ 출력예제 1 10


```

-   접근 방법

```text
[내가 푼 방식]
- 빈배열을 만들고 previusScore에 0을 할당한다.
- 인자로 받는 array를 반복문을 돌리는데
- 안에 조건문으로 해당 인덱스의 값이 1인지 0인지에 따라 조건을 나눈다.
  - 1일 때 아까 할당한 previousScore가 0보다 큰지 아닌지 조건을 나누어 0보다 크다면 previousScore++를 시키고 해당 previousScore를 answer에 푸쉬한다.
  - 0이라면 answer에 1을 푸쉬하고 prev값을 0으로 초기화 시킨다.

  -0일때는 prev값을 0으로만 초기화한다.
- answer의 값을 reduce로 합을 구해 return 한다.

[풀이보고 리팩토링]
- 총 값과 가사점을 뜻하는 변수를 각각 만들어 0을 할당한다.
- 인자로 받는 array를 반복문을 돌리고
- 해당 인덱스 값이 0보다 크다면 가산점값을 ++ 시키고 그 값을 sum에 더한다.
- 0이라면 가산점 값을 0으로 초기화한다.
- sum을 리턴한다.

```

# 호근님

-   문제 주소 : []()
-   접근 방법

```text

```

# 태성님

-   문제 주소 : [프로그래머스 - 피로도](https://programmers.co.kr/learn/courses/30/lessons/87946?language=python3)
-   접근 방법

```text
던전 입장전 피로도 소지여부와 던접 입장후 소모 피로도에 따른 최대로 던전을 돌 수 있는 횟수에 대해 구하는 문제이다.

처음엔 입장시 필요한 피로도와 소모 필요도의 차이가 가장 큰 값들로 정렬 후 입장시 필요한 피로도에 따른 추가 정렬로
입장 피로도가 높으면서 소모 필도가 낮은 값부터 차례로 들어가면 될것으로 생각했다.

하지만 이렇게 정렬할시 입장 필요도와 소모 필요도 차이가 같으면서 입장필요도와 소모필요도가 가장 높은 값이 먼저 계산되어
여러번 던전에 입장 할 수 있는 케이스도 한번의 입장만 가능하게 계산되었다.

그래서 던전의 갯수가 8개로 제한된 조건을 이용하여 순열로 계산하여도
8! = 40320 때문에 시간초과가 나지 않을것으로 판단하여 순열을 통한 모든 케이스 계산으로 최대값을 구하였다.
```

# 민호님

-   문제 주소 : [문서 검색](https://www.acmicpc.net/problem/1543)
-   접근 방법

```text
그리디 문제에 속한다고 되어있었는데,
문제 접근 도중에 replace로 치환하는 방법이 떠올랐다.
그리고 count 내장 함수로 내가 치환환 키워드의 개수를 세주었다.

replace와 count라는 내장 함수만 사용하였다.

이 문제는 중복을 허용하지 않기에 가능했다.
```
