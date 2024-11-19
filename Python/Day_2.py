'''
식별자/ 변수명
밀접하지만 같은 개념은 아님.

식별자는 프로그래밍 언어에서 변수, 함수, 클래스, 모듈 등의 
이름을 지정하는 모든 명칭을 뜻한다.(범위가 넓음, 큰 범위 개념)

변수명은 변수의 이름을 뜻한다. 컴퓨터 안에 주소나 코드는 외울수 없어
편하게 쉽게 코딩을 하기 위해 변수명을 지정해주는 것임. 그래서 의미가 전해져야한다.
(값을 저장할 메모리 공간을 참조하기 위해 사용되는 이름)

변수는 데이터를 저장하는 컨테이너이고, 변수명은 컨테이너를 가르키는 이름이다.

https://tartan-steel-3da.notion.site/14108b43002680b59ce8cad669547c28


import keyword
print(keyword.kwlist)

#포멧 여러개 출력하기

print("{}".format(8))
print("{}{} {}".format(8,"기","백엔드")) 
#단점 컴퓨터는 기억이 한정적임. 사용하는 것 외엔 사용하지 않음
#이 단점의 보완이 변수임

#변수에 저장해야하는 이유

str="{}".format(8) #00101010
print(str)
#변수에 저장하면 출력한 내용들을 기억할 수 있다.






num=8
str_a="기"
str_b="백엔드"

print(f"{num}{str_a} {str_b}")


#format() 함수는 출력할 내용이 길때 사용하면 편리함

내장함수는 무엇이 있는지?(공부, 눈에 익히기)




print(type(777))
print(type(777.777))

#숫자형인지 문자형인지 먼저 단정짓지 않기! 모든지 의심해보기


#21+29=50

num_1=21
num_2=29

print(num_1,"+",num_2,"=",num_1+num_2)



#2가지 나누기 연산자 중요!!!!!!!!!!!!!!!!!!!!!!!
#/-나누기, //-몫 출력, %-나머지 출력

position="백엔드"
get_in="3명 타세요"

print(position*3)
print(position + get_in)
print(position + get_in * 3)
#연산자 출력 순서 확인!!!



str="초격차백엔드"

print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
#print(str[5],str[2])

print(str[-1])
#문자열은 랜덤이니 마지막 인덱스의 길이는 -1로 통일
print(len(str))
#len() 미리 만들어 놓은 기능 = 내장함수


#변수[시작위치:끝나는 위치] :시작위치부터 출력되고 끝나는 위치 -1까지만 출력된다.
print(str[:4])#끝나는 지점까지만 출력
print(str[0:7:2])#인덱스를 두칸씩 뛰어 출력

alpa="A"

print (alpa.islower()) # 대소문자를 구별해주는데, true, false로 구별해준다.

answer =alpa.islower()
#컴퓨터는 오로지 최종결과만 기억하기에 중간결과는 무의미하다. 
#answer라는 변수에 알파의 결과인 true를 할당하기에 대문자 A가 아닌 True가 출력됨.




url="https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색하고 싶은 키워드를 입력하십시요. --->") 
#input():입력을 받을 수 있도록 미리 만들어준 기능임.내장함수!!

print(keyword,url+keyword)
#원하는 사이트로 이동 가능! --> 컨트롤+마우스 클릭
'''

#if 조건 해당된다면 :  만약 @@면 아래있는 코드를 실행해

str="초격차백엔드"

if len(str) > 5 : #클론으로 마무리
    print("True") #참일 경우 탭 다음 문장부터 코드가 실행됨
#만약 틀린 걸 알려주고 싶은 코드까지 포함한 if문이면 else도 포함해주는 것이 좋음
#else가 없을때, 틀렷쥬가 실행되는 이유는 코드는 위에서부터 내려오는 코드적 언어?절차가 있음. 
#else:
#    print("틀렸쥬") 
#조건을 하나더 달 수 있는 elif

#조건에 안맞아서 다음 코드가 실행되는 거임

elif len(str) > 5 :
    print("이번에도 진짜임.")

#if 문이 너무 많으면 ㅁㅁ메모리 사용도 많고 복잡하고 가독성이 떨어짐