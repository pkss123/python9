# 문자열은 슬라이싱시 일반적으로는 연속된 인덱스번호를 범위로
# 자료를 뽑아오지만, 번호간 간격을 1이 아닌 숫자로 지정할
# 수 있습니다 이 경우 지정된 번호만큼 범위 내에서 
# 증가시키며 문자열을 잘라옵니다
yoil = "월화수목금토일"
print(yoil[::2])
print(yoil[::-1])