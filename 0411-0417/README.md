# 병수님

- 문제 주소 및 접근방법
  - [k번째 큰 수](https://dev-soo-log.tistory.com/15)

```text
 1. 접근과정
문제는 심플하다. 서로 다른 세 수를 세 번의 반복문을 통해 뽑아 더 해 큰 수부터 정렬하여 k번째 큰 수를 리턴하면 된다.

2. 문제점
두 번째 반복문에서 i와 다른 k 라는 조건문을 걸었다고 하더라도 세 번째 반복문에서 i와 k가 다르다는 보장이 되지 않는다.
세 번째 반복문에서 sum이 초기화 되지 않은 채 계속 누적된 값이 push 되었다.
```

# 호근님

- 문제 주소 및 접근방법
  - [로또의 최고 순위와 최저 순위](https://programmers.co.kr/learn/courses/30/lessons/77484)

```
최고 순위: 7 - 0을 포함한 정답과 일치하는 숫자의 개수
최저 순위: 7 - 0을 포함하지 않고 일치하는 숫자의 개수
1개 맞을때와 모두 틀렸을때는 6위 이므로 정답개수가 0일 경우 1로 치환해서 빼줌
```

# 태성님

- 문제 주소 및 접근방법
  - [삼각 달팽이](https://programmers.co.kr/learn/courses/30/lessons/68645)

```text
처음에 규칙을 찾지 못해 해매었다.
1. 삼각형을 직각 삼각형으로 변화하여 2중 배열을 만든다.
2. 숫자가 채워지는 방향이 아래, 옆, 대각 3방향이 순환한다.
3. 한번 방향이 바꿀때마다 n-1만큼 숫자가 채워진다.

따라서 2중배열(맨위가 1 마지막이 n인)을 만들고 숫자가 채워지는 방향에 맞게 인덱스 값을 더해주면서 숫자를 채워주면 완성된다.
```

# 민호님

- 문제 주소 및 접근방법
  - []()

```text

```
