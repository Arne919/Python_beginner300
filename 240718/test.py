# outers = [2, 3, 4, 5]
# inners = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for outer in outers:
#     for inner in inners:
#         print(outer, inner)

# floors = [1, 2, 3, 4, 5] #range(1,6)
# rooms = [1, 2, 3, 4]
# for floor in floors:
#     for room in rooms:
#         print(floor, room)

# floors = [0, 1]
# rooms = range(1, 5)
# for floor in floors:
#     print('\n')
#     print(f'{floor}층')
#     for room in rooms:
#         print (f'{room}호')


# elements = [['A', 'B'], ['c', 'd']]

# for elem in elements[0]:
#     print(elem)
#     for i in elements[1]:
#         print(i)

# for i in range(0, 2):
#     print(elements[0][i])
#     for j in range(0, 2):
#         print(elements[1][j])


# print(data1)

# food_list = [
#     {
#         '종류': '한식',
#         '이름': '잡채'
#     },
#     {
#         '종류': '채소',
#         '이름': '토마토'
#     },
#     {
#         '종류': '중식',
#         '이름': '자장면'
#     },
# ]

# for food in food_list:
#     if food['이름'] == '토마토':
#         food['종류'] = '과일'
#     elif food['이름'] == '자장면':
#         print('자장면엔 고춧가루지')
#     print(f"{food['이름']} 은/는 {food['종류']} (이)다.")

# while True:
#     print(f'{food_list}')
#     break


matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]

# 아래애 코드를 작성하시오.
matrix_len = 0
for each in matrix:
    matrix_len += 1

print(matrix_len)



for number in matrix:
    temporary_len = 0
    for each in number:
        temporary_len += 1
    if temporary_len <= 4:
        print(f'{number}리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.')

# elements = [['A', 'B'], ['c', 'd']]

# for elem in elements[0]:
#     print(elem)
#     for i in elements[1]:
#         print(i)

# for i in range(0, 2):
#     print(elements[0][i])
#     for j in range(0, 2):
#         print(elements[1][j])