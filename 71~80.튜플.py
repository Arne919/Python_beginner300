### 파이썬 튜플


# 71. 
# my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(type(my_variable))
# <class 'tuple'>


# 72.
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 
# 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키
movie_rank = ('닥터 스트레인지', '스프릿', '럭키')
print(movie_rank)


# 73. 
# 숫자 1 이 저장된 튜플을 생성하라.
my_tuple = (1, )
print(type(my_tuple))
# <class 'tuple'>
print(my_tuple)



# 74. 
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
t = (1, 2, 3)
# t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
# tuple은 원소(element)의 값을 변경할 수 없습니다.


# 75. 
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. 
# t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4
print(type(t))
# <class 'tuple'>
# 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야하지만,
# 사용자 편의를 위해 괄호 없이도 동작합니다.


# 76.
# 변수 t에는 아래와 같은 값이 저장되어 있다. 
# 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)


# 77. 
# 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest)
print(data)


# 78. 
# 다음 리스트를 튜플로 변경하라.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data = tuple(interest)
print(data)


# 79.
# 다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# apple banana cake


# 80. range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# (2, 4, 6, 8 ... 98)
data = tuple(range(2, 100, 2))
print(data)