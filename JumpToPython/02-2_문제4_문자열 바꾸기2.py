#[문제4] 문자열 바꾸기2

#아래와 같은 문자열이 있다.[ a:b:c:d ]
#split과 join함수를 활용하여 [ #a#b#c#d ] 로 고치시오.

st = "a:b:c:d"
st = st.split(':')
st = '#'.join(st)
print(st)