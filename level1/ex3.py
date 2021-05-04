# 1. 리스트   -> 선언 : list1 = []
list1 = [1,2,3,4]
list2 = [5,6,7,8]

print(list1[2])
print("="*50)

# 더하기(중요)
list3 = list1+ list2
print(list3)

# 3 스칼라
# [1,3,4] -> 벡터 ( 방향이 있는 것 )

# 2차원 배열 만들기
# 2차원 matrix, 3차원 tensor
list4 =[
   list1,
   list2
]

print(list4)

list1.append(10)  # 리스트에 10을 추가

del list1[0]  # 인덱스로 삭제

list1.remove(2)  # 값으로 삭제
print(list1)


list6 = list(range(10))
print(list6)

list7 = list(range(1,12))
print(list7)


# 2. 튜플 - 리스트 값음 !! 데이터 변경이 불가능(읽기 전용)
tuple1 = (1,2,3)
print(tuple1)

tuple2 = (4,5,6)

tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = [
    tuple1,
    tuple2
]

print(tuple4)

# 3. 딕셔너리
