### 파이썬 반복문(3)


# 151.
# 리스트에는 네 개의 정수가 저장돼 있다.
리스트 = [3, -20, -3, 44]
# for문을 사용해서 리스트의 음수를 출력하라.
# -20
# -3
for i in 리스트:
    if i < 0:
        print(i)


# 152.
# for문을 사용해서 3의 배수만을 출력하라.
리스트 = [3, 100, 23, 44]
# 3
for i in 리스트:
    if i%3 == 0:
        print(i)


# 153.
# 리스트에서 20 보다 작은 3의 배수를 출력하라
리스트 = [13, 21, 12, 14, 30, 18]
# 12
# 18
for i in 리스트:
    if i % 3 == 0 and i < 20:
        print(i)


# 154.
# 리스트에서 세 글자 이상의 문자를 화면에 출력하라
리스트 = ["I", "study", "python", "language", "!"]
# study
# python
# language
for i in 리스트:
    if len(i) >= 3:
        print(i)


# 155.
# 리스트에서 대문자만 화면에 출력하라.
리스트 = ["A", "b", "c", "D"]
# A
# D
# (참고) isupper() 메서드는 대문자 여부를 판별합니다.
# >> 변수 = "A"
# >> 변수.isupper()
# True
# >> 변수 = "a"
# >> 변수.isupper()
# False
for i in 리스트:
    if i.isupper():
        print(i)


# 156.
# 리스트에서 소문자만 화면에 출력하라.
리스트 = ["A", "b", "c", "D"]
# b
# c
for i in 리스트:
    if not i.isupper():
        print(i)


# 157.
# 이름의 첫 글자를 대문자로 변경해서 출력하라.
리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot
# (참고) upper() 메서드는 문자열을 대문자로 변경합니다.
# >> 변수 = "a"
# >> a.upper()
# A
# >> 변수 = "abc"
# >> 변수.upper()
# ABC
for i in 리스트:
    print(i[0].upper()+i[1:])


# 158.
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro
for i in 리스트:
    split = i.split(".")
    print(split[0])


# 159.
# 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# define.h
for i in 리스트:
    split = i.split(".")
    if split[1] == "h":
        print(i)


# 160.
# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# intra.c
# define.h
for i in 리스트:
    split = i.split(".")
    if split[1] =="h" or split[1] =="c":
        print(i)