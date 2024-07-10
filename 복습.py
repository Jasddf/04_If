a = [1,2,3]
print(a[0] + a[2])

a = [1,2,3,4,5]
a.append(10)
a.remove(2)
print(len(a))

b = list(range(1,12))
print(b)

person = {'이름' : '장영수', '나이' : 29}
print(person.keys())

is_true = True
is_false = False
print(is_true, is_false, type(is_true), type(is_false))

if is_true:
    print('이것은 참입니다.')