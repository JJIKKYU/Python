#[문제3] 문자열 바꾸기1

#아래와 같은 문자열이 있다.[ a:b:c:d ]
#replace를 활용하여 [ #a#b#c#d ] 로 고치시오.

st = "a:b:c:d"
st = st.replace(':','#')
print(st)