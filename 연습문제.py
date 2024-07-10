#연습문제1
a = int(input('임의의 숫자를 입력하세요 : '))
if 5 < a < 10 :
    print('ok.')
elif a <= 5 or a >= 10 :
    print('no.')

#연습문제2
fruit = ['사과', '포도', '홍시']
a = input('과일을 선택하시오 : ')
if a in fruit :
    print('정답입니다.')
else :
    print('오답입니다.')

#연습문제3
fruit = {'봄':'딸기','여름':'토마토','가을':'사과'}
a = input('요소를 선택하시오 : ')
if a in fruit.values() :
    print('정답입니다.')
else:
    print('오답입니다.')






