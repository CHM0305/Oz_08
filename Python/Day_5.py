# print("오늘도 손이 너무나 바빠핑")
# print("어떻게하면 내일 쉴 수 있을까?")

# print("오늘도 손이 너무나 바빠핑")
# print("어떻게하면 내일 쉴 수 있을까?")

# print("오늘도 손이 너무나 바빠핑")  # 손과 같은 신체 부위를 요청에 의해 바꿀 수 잇도록 개선
# print("어떻게하면 내일 쉴 수 있을까?")  # 쉬는 일자 정보를 요청에 의해 바꿀 수 있도록 개선
#             #이 바디 데이 하나하나가 매개변수
# def busy_ping(body,days):
#     print(f"오늘도 {body}이 너무나 바빠핑")
#     print(f"어떻게하면 {days} 쉴 수 있을까?")


# # #함수 실행 = 호출
# busy_ping("발","내일모레")

#반복되는 코드 작성 시 함수를 이용하면 가독성과 유지보수가 좋아진다.


#함수 만드는 방법
'''
def 함수이름():
    실행코드

def 함수이름(매개변수1, 매개변수2):
    코드 작성
    return 매개 변수를 이용한 결과값 반환
''' 


#len() 함수!
#oz_len()란 함수를 만들어 글자수를 반환해주세요  문제 잘 읽기!!

hello="안녕하세요"

def oz_len(hello):
    count=0
    for i in hello:
        count +=1
    return count
    


oz_len(hello)
print(oz_len(hello))

