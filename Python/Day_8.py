'''
isinstance(): 첫 번째 매개변수에는 인스턴스(객체),  
            두 번째 매개변수에는 클래스를 입력해주면
            두번째 매개변수로 입력한 클래스 기반으로 인스턴스가 생성되었는지를
            참과 거짓으로 변환해준다.

'''

#isinstance 사용법

# class Student:
#     def __init__(self):
#         pass

# student =Student()

# print("isinstance(student, Student):", isinstance(student , Student))        


#뭐였더라

# class Python:
#     def python(self):
#         print("파이썬 수강중")

# class Jave:
#     def java(self):
#         print("자바 수강중")

# programming_subjects = [Python(),Python(),Python(),Jave(),Python()]

# for subject in programming_subjects:
#     if isinstance(subject,Python):
#         subject.python()
#     elif isinstance(subject,Jave):
#         subject.java()


#__str__ 사용법

class CreateOzStudents:
    def __init__(self, name, python, database, django, AWS):
        self.name=name
        self.python=python
        self.database=database
        self.django=django
        self.AWS=AWS

    def get_sum(self):
        return self.python + self.database + self.django + self.AWS
    
    def get_average(self):
        return self.get_sum()/4

    def __str__(self):
        return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'

oz_students=[
    CreateOzStudents("이름1",4,2,4,2),
    CreateOzStudents("이름2",5,2,1,1),
    CreateOzStudents("이름3",4,1,5,4),
    CreateOzStudents("이름4",2,4,3,2)
]

print("이름","총점","평균",sep="\t")
for student in oz_students:
    print(str(student))

#__eq__ / == 같다라는 표시만 해도 클래스 함수가 호출되어 계산을 해준다.
#__srt__