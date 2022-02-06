## day 8
### 과제 1
- 다음의 데이터를 로드해보세요
~~~python
x = np.array([1, 1, 2, 2])
y = np.array([1, 2, 3, 4])
~~~
- 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 1)
~~~python
Out[6]: array([ 2., 3., 4., 5.])
~~~
- 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 2)
~~~python
Out[10]: array([ 0., 1., 1., 2.])
~~~
- 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 3)
~~~python
Out[11]: array([ 1., 0., 1., 0.])
~~~
- 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 4)
~~~python
Out[13]: array([ 2., 4., 8., 16.])
~~~
- 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 5)
~~~python
Out[25]: array([ 1., 2., 6., 8.])
~~~
- 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 6)
~~~python
Out[26]: array([ 1. , 2. , 1.5, 2. ])
~~~
- 다음의 결과를 도출해보세요. 이 때 Vectorization 연산으로 결과를 도출해보세요(-- 7)
~~~python
Out[29]: array([ 1., 2., 9., 16.])
~~~

- 다음의 데이터를 로드해보세요
~~~python
x = np.array([1, 1, 2, 2])
y = np.array([1, 2, 3, 4])
~~~
- 배열간 비교 연산을 통해, =, !=, >=, >, <=, < 6가지 케이스를 비교해서 boolean 형태로 출력해보세요  
  다음과 같은 결과값이 도출되어야 합니다.
~~~
Out[32]: array([ True, False, False, False], dtype=bool)
Out[33]: array([False, True, True, True], dtype=bool)
Out[34]: array([False, False, False, False], dtype=bool)
Out[35]: array([ True, False, False, False], dtype=bool)
Out[36]: array([False, True, True, True], dtype=bool)
Out[37]: array([ True, True, True, True], dtype=bool)
~~~
- 다음의 함수는 어떤 결과값이 도출되나요 ?
~~~python
x = np.array([1, 1, 2, 2])
y = np.array([1, 2, 3, 4])

z = y.copy()

np.array_equal(x, y) # -- (1) ? 
np.array_euqal(y, z) # -- (2) ?
~~~
- 다음의 `x`, `y` 데이터를 아래의 조건으로 비교한 결과를 도출해보세요  
  - 두 배열의 원소가 모두 0이 아니면, True 반환
  - 두 배열의 원소 중 한개라도 0이 아니면 True 반환
  - 두 배열의 원소가 서로 같지 않으면 True 반환
- 다음의 코드를 실행시키면, 어떤 결과가 도출되나요? 
~~~python
x4 = np.array([1, 1, 2, 2])
x5 = np.arange(5)
~~~

### 과제 2
- 다음의 데이터를 로드해보세요
~~~python
a_df = pd.DataFrame({'x1': [1, 2, 3, 4],
                     'x2': [5, 6, 7, 8]})
~~~
- 다음의 결과를 브로드캐스팅(broadcasting) 방법을 사용하여 도출해보세요
~~~python
Out[8]:
x1 x2
0 2 6
1 3 7
2 4 8
3 5 9
~~~
- 다음의 데이터를 로드해보세요
~~~python
b = np.arange(12).reshape((4, 3))
~~~
- 다음의 결과를 브로드캐스팅(broadcasting) 방법을 사용하여 도출해보세요
~~~python
Out[15]:
array([[ 0, 2, 4],
       [ 3, 5, 7],
       [ 6, 8, 10],
       [ 9, 11, 13]])
~~~
- 배열의 차원 크기, 모양이 다르면 모두 Broadcasting 이 일어나나요?   
  그렇지 않다면, 어떤 경우에 Broadcasting 이 일어나나요?  
  간단한 코드 예시를 통해 설명해보세요
- 다음의 데이터를 로드해보세요
~~~python
b = np.arange(12).reshape((4, 3))
~~~
- 다음의 결과를 브로드캐스팅(broadcasting) 방법을 사용하여 도출해보세요
~~~python
Out[24]:
array([[ 0, 1, 2],
       [ 4, 5, 6],
       [ 8, 9, 10],
       [12, 13, 14]])
~~~
- 다음의 데이터를 로드해보세요
~~~python
f = np.arange(24).reshape((2,4,3))
~~~
- 다음의 결과를 브로드캐스팅(broadcasting) 방법을 사용하여 도출해보세요
~~~python
Out[29]:
array([[[ 1., 2., 3.],
         [ 4., 5., 6.],
         [ 7., 8., 9.],
         [ 10., 11., 12.]],
        [[ 13., 14., 15.],
         [ 16., 17., 18.],
         [ 19., 20., 21.],
         [ 22., 23., 24.]]])
~~~

### 과제 3
- 다음의 코드를 완성시켜 보세요(-- 1)
~~~python
a = np.array([1, 2, 3, 4])
a_4_1 = 
print(a_4_1)

# result
Out[6]:
array([[ 1.],
       [ 2.],
       [ 3.],
       [ 4.]])
~~~
- 다음의 코드를 완성시켜 보세요(-- 2)
~~~python
b = np.arange(12).reshape(3, 4)
b_3_4_1 = 
print(b_3_4_1)

# result
Out[12]:
array([[[ 0],
         [ 1],
         [ 2],
         [ 3]],

        [[ 4],
         [ 5],
         [ 6],
         [ 7]],

        [[ 8],
         [ 9],
         [10],
         [11]]])
~~~
- 다음의 코드를 완성시켜 보세요(-- 3)
~~~python
A = np.array([0, 1, 2, 3])
A_2_8 =
print(A_2_8)
# result
Out[24]:
array([[ 0.,  1.,  2.,  3.,  0.,  1.,  2.,  3.],
        [ 0.,  1.,  2.,  3.,  0.,  1.,  2.,  3.]])
~~~
- 다음의 코드를 완성시켜 보세요(-- 4)
~~~python
B = np.arange(8).reshape(2, 4)
B_2_8 = 
print(B_2_8)

# result
array([[0, 1, 2, 3],
       [4, 5, 6, 7],
       [0, 1, 2, 3],
       [4, 5, 6, 7]])
~~~

### 과제 4
- 3가지 방법을 사용하여 다음의 데이터의 전치 행렬을 구해보세요  
~~~python
a = np.arange(15).reshape(3, 5)
~~~
- 다음 데이터의 `shape`은 (2, 3, 4) 입니다.  
  이를 (2, 4, 3) 으로 변경한 결과를 최소 2가지 방법 이상으로 도출해보세요
~~~python
b = np.arange(24).reshape(2, 3, 4)
~~~

### 과제 5
- 다음의 코드에서 -- 1 과 -- 2 는 같은 결과를 도출하나요?  
  아니면 다른 결과를 도출하나요? 그 이유는 무엇인가요 ? 
~~~python
d = np.arange(20).reshape(4, 5)
print(d[0:3, 1:3]) # -- 1
print(d[0:3][1:3]) # -- 2
~~~


