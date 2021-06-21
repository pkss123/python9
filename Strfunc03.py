# startswith() 는 시작 문자열을 검사하고
# endswith() 는 끝나는 문자열을 검사해
# 내가 제시한 문자열과 일치하면 True 일치하지않으면 False

name = "홍길동"

if name.startswith("홍"):
    print("홍씨 입니다")
if name.startswith("박"):
    print("박씨 입니다")
print()

file = "cat.jpg"

if file.endswith(".jpg"):
    print("그림파일 입니다")
print()    

domain = "www.koo.co.kr"
if domain.endswith(".kr"):
    print("한국 도메인 입니다")
    
# 문자 요소 확인
# .isalpha() - 알파벳으로만 구성된 문자열인지 검사
# .islower(), .isupper() - 소문자, 대문자로 구성되었는지 검사
# .isdecimal() - 숫자로만 이루어졌는지 검사

height = input("당신의 키를 입력해주세요:")
if height.isdecimal():
    print("키 : " + height + "cm")
else:
    print("숫자만 입력해주세요")