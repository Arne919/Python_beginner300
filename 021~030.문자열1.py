### 파이썬 문자열(1)


# 21. 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
# 실행 예: p t
print(letters[0], letters[2])


# 22. 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
# 실행 예: 2210
print(license_plate[-4:])


# 23. 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
# 실행 예: 홀홀홀
print(string[::2])


# 24. 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
# 실행 예: NOHTYP
print(string[::-1])


# 25. 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
# 실행 예: 010 1111 2222
phone_number1 = phone_number.replace('-', ' ')
print(phone_number1)


# 26. 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예: 01011112222
phone_number = "010-1111-2222"
# 실행 예: 010 1111 2222
phone_number1 = phone_number.replace('-','')
print(phone_number1)


# 27. 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
# 실행 예: kr
# print(url[-2:])
url_split = url.split('.')
print(url_split[-1])


# 28. 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
# lang = 'python'
# lang[0] = 'P'
# print(lang) # 문자열은 수정할수 없다(할당메서드를 지원하지 않음)


# 29. replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
# 실행 예: Abcdfe2A354A32A
string = string.replace('a', 'A')
print(string)


# 30. replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
string = 'abcd'
string.replace('b', 'B')
print(string) # abcd
string = string.replace('b', 'B')
print(string) # aBcd