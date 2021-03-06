# 병수님

```text
1. [등수 구하기 x]
N(1<=N<=100)명의 학생의 국어점수가 입력되면 각 학생의 등수를 입력된 순서대로 출력하는 프로그램을 작성하세요.
▣ 입력설명
첫 줄에 N(3<=N<=1000)이 입력되고, 두 번째 줄에 국어점수를 의미하는 N개의 정수가 입력 된다. 같은 점수가 입력될 경우 높은 등수로 동일 처리한다. 즉 가장 높은 점수가 92점인데 92점이 3명 존재하면 1등이 3명이고 그 다음 학생은 4등이 된다.
▣ 출력설명
입력된 순서대로 등수를 출력한다.
▣ 입력예제 1
5
87 89 92 100 76
▣ 출력예제 1
43215
```

-   접근 방법

```text
- 접근 자체가 힘들었다.
문제의 키는 2차원 탐색이라는 것을 빨리 캐치하고 이중포문을 돌리는 데 있다.
- 배열 answer를 Array.from 메소드를 사용해 1로 인자로 받는 arr.length(=n)만큼 배열을 만든다
- 점수인 인자 arr를 이중 포문을 돌려 자신 보다 큰 수가 있을 때만 answer[i]에 ++ 를 해준다.

```

```text
2. [격자판 최대합 x]
5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합 니다.
▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.
▣ 출력설명 최대합을 출력합니다.
▣ 입력예제 1
5
10 13 10 12 15 12 39 30 23 11 11 25 50 53 15 19 27 29 37 27 19 13 30 13 19
▣ 출력예제 1 155
```

-   접근 방법

```text
- 이 문제는 문제를 이해하기가 힘들었다.
문제의 시작은 위와 같이 2차원 탐색으로 이중포문을 돌려야 된다는 인식으로 시작된다.
- 행의 합은 arr[i][j] 열의 합은 arr[j[i]]
- 대각선의 합은 각각 arr[i][i], arr[i][n-i-1] 이다
- 대각선은 2개 밖에 없으므로 이중포문으로 각 행과 각열의 합을 구하고 그 중 최대값을 answer에 넣는다
- 대각선의 합을 구하는 반복문 각 대각선의 합을 구하고 아까 구한 answer와 값을 비교하여 그 중 큰 값을 리턴한다.
-
```

```text
3. [봉우리]

지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
격자의 가장자리는 0으로 초기화 되었다고 가정한다.
만약 N=5 이고, 격자판의 숫자가 다음과 같다면 봉우리의 개수는 10개입니다.

▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는 다.
▣ 출력설명
봉우리의 개수를 출력하세요.
▣ 입력예제 1
5
53723
37161
72534
43641
87352
▣ 출력예제 1
10
```

-   접근 방법
-   이 문제도 쉽지 않았지만 2차원 탐색을 인지하고 차분히 문제를 풀었다.
    [내가 푼 방식]
-   해당 값의 상하좌우를 비교할 때 가장자리에 있는 것을 어떻게 할 것인지가 포인트였다.
-   나는 문제에서 제시된 격자의 가장자리는 0으로 초기화됐다는 예시처럼 n\*n의 격자판에 0을 둘러 새로운 배열을 만들었다.
-   그 배열을 이중 포문으로 돌리고 (시작은 1 max는 length-1해서 해당 arr만 돌게 만듬)

```js
if(newArray[i][j] > Math.max(newArray[i-1][j],newArray[i][j+1],newArray[i+1][j],newArray[i][j-1])) {
```

로 상하좌우보다 큰 값일 경우에만 answer++ 시켜 리턴했다.

[풀이방식]

-   풀이는 dx, dy를 만들어 위에 내가 수기로 4개 비교한 것을 배열로 반복문을 한번 더 돌려 nx, ny값이 나오게 만들었다.

```text

```

# 호근님

-   문제 주소 : [프로그래머스 - 없는 숫자 구하기](https://programmers.co.kr/learn/courses/30/lessons/86051)
-   접근 방법

```
0에서 9까지 반복문에서 해당 배열에 없는 숫자만 더해줌
```

# 태성님

-   문제 주소 : [프로그래머스 - 캐시](https://programmers.co.kr/learn/courses/30/lessons/17680?language=python3)
-   접근 방법

```text
간단하게 캐시 히트가 되면 캐시에서 꺼내고 아니면 캐쉬에 넣고 호출하는 것을 물어보는 문제이다.
캐시 교체 알고리즘을 LRU를 사용했다 따라서 캐시에 없으면 넣으면 되고 캐시 용량이 차면 먼저들어온 데이터를 삭제하고 데이터를 넣으면된다.
또한 캐시 히트가 되면 히트된 캐시를 가장 늦게 들어온 위치로 옮기면 된다.
```

# 민호님

- 문제 주소 : 너무 많음 ㅜ
- 접근 방법

```text

```
