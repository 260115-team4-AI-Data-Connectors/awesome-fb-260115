# range 범위를 (1, 31 + 1)로 수정하여 31까지 출력하게 합니다.
for i in range(1, 32): 
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
