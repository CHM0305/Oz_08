'''
클래스의 생성자와 메소드

class 클래스 이름:
    def __init__(self, 추가적인 매개변수):  -값을 초기화해주는 메소드 (클래스의 기본 문법이라 생각하면 됨)
    클래스 안에 선언 함수를 def 메소드라 부른다.
    클래스의 메소드를 불러올려면 .매소드명() 
    
    self는 자기 자신을 참조한다. 참조라는 것은 메모리 어딘가에 위치해 있는 지 주소를 참조하는 것.
    그래서 파이썬에 클래스 내부함수의 매개변수 첫번째인 self는 자동으로 값이 채워진다.

'''

# class CreateOzStudents:
#     def __init__(self, name, python, database, django, AWS):
#         self.name=name,
#         self.python=python,
#         self.database=database,
#         self.django=django,
#         self.AWS=AWS

# oz_students=[
#     CreateOzStudents("이름1",4,2,4,2),
#     CreateOzStudents("이름2",5,2,1,1),
#     CreateOzStudents("이름3",4,1,5,4),
#     CreateOzStudents("이름4",2,4,3,2)
# ]

# print(oz_students[0].name)
# print(oz_students[1].python)
# print(oz_students[2].database)
# print(oz_students[3].django)
# print(oz_students[4].AWS)

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

    def to_string(self):
        return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'

oz_students=[
    CreateOzStudents("이름1",4,2,4,2),
    CreateOzStudents("이름2",5,2,1,1),
    CreateOzStudents("이름3",4,1,5,4),
    CreateOzStudents("이름4",2,4,3,2)
]

print("이름","총점","평균",sep="\t")
for student in oz_students:
    print(student.to_string())