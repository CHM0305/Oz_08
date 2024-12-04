'''
클래스 변수 만드는 방법 & 변수 접근 법
class 클래스 이름:
    클래스 변수= 값

클래스 변수에 접근
클래스 이름.변수 이름

'''

#학생 수 세어보는 기능 추가!!!



class CreateOzStudents:

    count=0

    def __init__(self, name, python, database, django, AWS):
        self.name=name
        self.python=python
        self.database=database
        self.django=django
        self.AWS=AWS

        CreateOzStudents.count +=1
        print(f'{CreateOzStudents.count}번째 수강생의 정보가 추가되었습니다.')

oz_students=[
    CreateOzStudents("이름1",4,2,4,2),
    CreateOzStudents("이름2",5,2,1,1),
    CreateOzStudents("이름3",4,1,5,4),
    CreateOzStudents("이름4",2,4,3,2)
]

print(f'현재 데이터가 입력된 총 수강생은{CreateOzStudents.count}명 입니다.')

'''
생성하는 방법은 일반함수랑 별반 차이가 없지만 생성 후 사용방법이 다르니 유의하기
클래스이름.변수이름

클래스 변수 외 함수도 같지만 클래스 안에 함수를 만드는 법은 또 다름

그것이 바로 @데코레이터 명칭은 클래스 데코레이터이다.

클래스 데코레이터 구문
class 클래스 이름:
    @classmethod
    def 클래스 함수명(cls-클래스명, 매개변수):
        pass
        
클래스 함수 호출
클래스이름.함수이름(매개변수)
'''

class CreateOzStudents:

    student=[]

    @classmethod
    def print(cls):
        print("수강생 데이터 정보")
        print("이름\t총정\t평균")
        for student in cls.student:
            print(str(student))



    def __init__(self, name, python, database, django, AWS):
        self.name=name
        self.python=python
        self.database=database
        self.django=django
        self.AWS=AWS
        CreateOzStudents.student.append(self)

    def get_sum(self):
        return self.python + self.database + self.django + self.AWS
    
    def get_average(self):
        return self.get_sum()/4

    def __str__(self):
        return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'


CreateOzStudents("이름1",4,2,4,2),
CreateOzStudents("이름2",5,2,1,1),
CreateOzStudents("이름3",4,1,5,4),
CreateOzStudents("이름4",2,4,3,2)


CreateOzStudents.print() #클래스에서 함수를 불러와야 우리가 원하는 결과값을 볼 수 있음
'''
class로 인스턴스를 생성하게 되면
class 안에 선언된 내부함수(매개변수에 self가 들어간 값)가 자동으로 호출됨.
그리고 클래스 함수는 CreateOzStudents.함수명()으로 실행할 수 있음.
'''