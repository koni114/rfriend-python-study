## day 16 
### 과제 1
- 다음의 코드를 로드해주세요
~~~python
import numpy as np
a = np.arange(-5, 5)
~~~
- 위의 a 배열에서 <b>0보다 작은 수는 0으로 변환하고 나머지는 그대로 두는 코드를 작성해보세요</b>
  - (1) List Comprehension 을 활용하여 코드를 작성해보세요
  - (2) indexing 을 활용해서 코드를 작성해보세요(hint: a[a<0]) 
  - (3) np.where 을 활용해서 코드를 작성해보세요
  - (4) np.clip 을 활용해서 코드를 작성해보세요

### 과제 2
- 다음의 코드를 로드해주세요
~~~python
import numpy as np
a = np.arange(24).reshape(4, 3, 2)
~~~
- 배열(a) 에 차원을 추가해보세요
  - (1) `numpy.reshape()` 을 이용한 차원 추가
  - (2) `numpy.expand_dims()` 을 이용한 차원 추가
  - (3) `numpy.newaxis` 을 이용한 차원 추가 

### 과제 3