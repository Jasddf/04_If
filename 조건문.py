# if 3 > 2 :
#     print('3은 1보다 큽니다.')
#     print('연산을 종료합니다.')
# print('-'*30)
# print('저는 들여쓰기를 하지 않은 라인입니다.')

# a = '장영수'
# b = '한별'
#
# if a == b :
#     print('두 사람의 이름은 같습니다.')
# elif a != b :
#     print('두 사람의 이름은 다릅니다.')

num_1 = 10
num_2 = 3

if num_1 < num_2 :
    print("num_1은 num_2보다 크기가 작습니다.")
elif num_1 == num_2 :
    print("num_1은 num_2보다 크기가 같습니다.")
elif num_1 > num_2 :
    print("num_1은 num_2보다 크기가 큽니다.")


# #연습문제1
# #1 사용자로부터 입력 받아
# a = input('부디 안녕하세요를 입력해주세요 : ')
# #2 입력받은 값이 '안녕하세요'인 경우
# if a == '안녕하세요.' :
# #3 화면에 '반갑습니다'를 출력
#     print('반갑습니다.')

#연습문제2
#1 사용자한테 값 입력 받아
a = int(input('임의의 수를 입력하세요 : '))
#2 해당값에 100을 더해라
b = a + 100
#3 계산한 값이 150 이상이면
if b >= 150 :
    print(b)
elif b < 150 :
    print("값이 부족합니다.")

#연습문제3
#1 사용자 나이 입력받아
age = int(input('나이를 입력하세요 : '))
#2 나이가 19보다 크면 '성인입니다.'출력하고 작으면 '미성년자입니다.'출력
if age > 19 :
    print('성인입니다.')
elif age <= 19 :
    print('미성년자입니다.')

#and, or 연산자
apple = '사과'
pear = '감자'

if apple == '사과' or pear == '배' :
    print('문자열이 모두 정확합니다')

var = [1,2,3]
if 3 in var:
    print('숫자 3이 var 변수에 있습니다.')