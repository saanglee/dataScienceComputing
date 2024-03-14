- 순서를 매길 수 있는 데이터를 정해진 순서대로 나열하는 문제
- [3, 5, 4] -> [3, 4, 5]
- CS에서 전통적으로 중요한 문제
  - 정렬된 데이터의 처리가 훨씬 효율적이기 때문
  - 수 많은 sorting알고리즘들이 있음
  - 순서열, 선택selection정렬, 삽입insert정렬, 합병merge정렬, 퀵정렬, 버블정렬

# 순서열 Sequence

여러 데이터를 순서에 맞춰 나열한 데이터 구조

- python에서 제공하는 순서열: list, tuple, range(정수범위), 문자열
- index(위치번호)로 접근 가능
- 수정 가능mutable 순서열: list
- immutable: tuple, range, 문자열

## list

```py
odds = [1, 3, 5, 6, 9]
odds[1] #3
```

## tuple

- 괄호로 표현
- immutable
- 수정이 안되는데 수정하고 싶으면 새 튜플을 만들면 됨

## 문자열 string

- immutable

## 정수범위 range

- range(n)은 0 부터 n-1까지 간격 1의 정수열
- range(5) 는 0, 1, 2, 3, 4
- immutable
- range(m, n, k)
  - m부터 n-1까지 k간격의 정수열
  - k지정 안하면 1
  - k가 -1이면 거꾸로 순서

## 리스트의 귀납 정의

- 빈 리스트 []도 리스트다.
- x가 임의의 원소이고, L이 임의의 리스트이면
- [x] - L도 리스트이다.
- 그 외에 다른 리스트는 없다.
