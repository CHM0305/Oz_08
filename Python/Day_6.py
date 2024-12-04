'''
객체 지향 프로그래밍: 클ㅐ스 기반의 객체를 우선으로 생각하는 프로그래밍
(언어: 자 파썬 php등)

객체: 구현하고자 하는 대상의 속성과 기능을 가지는 프로그램 단위
->현실세계는 표현할 것이 너무 나 많아 객체를 구성하는 필요한 속성만을
객체를 표현하는 개념을 추상화라고 하낟. 




oz_students=[
    {"name":"이름1","python":4,"database":3,"Django":4,"AWS":4},
    {"name":"이름2","python":3,"database":5,"Django":3,"AWS":2},
    {"name":"이름3","python":2,"database":4,"Django":3,"AWS":1},
    {"name":"이름4","python":4,"database":3,"Django":2,"AWS":3}
]
# 속성값을 나타냄
print("이름","총점","평균",sep="\t")

for student in oz_students:
    ablity_sum = student["python"]+student["database"]+student["Django"]+student["AWS"]
    ablity_average=ablity_sum / 4

    print(student["name"],ablity_sum,ablity_average,sep="\t")

'''

# def create_oz_students(name,python, database, django, AWS):
#     return{
#         "name" : name,
#         "python" : python,
#         "database" :database,
#         "Django":django,
#         "AWS": AWS
#     }

# oz_students=[
#     create_oz_students("이름1",4,2,4,2),
#     create_oz_students("이름2",5,2,1,1),
#     create_oz_students("이름3",4,1,5,4),
#     create_oz_students("이름4",2,4,3,2)
# ]

# print("이름","총점","평균",sep="\t")

# for student in oz_students:
#     ablity_sum = student["python"]+student["database"]+student["Django"]+student["AWS"]
#     ablity_average=ablity_sum / 4

#     print(student["name"],ablity_sum,ablity_average,sep="\t")




def create_oz_students(name,python, database, django, AWS):
    return{
        "name" : name,
        "python" : python,
        "database" :database,
        "Django":django,
        "AWS": AWS
    }

def get_sum(student):
    return student["python"]+student["database"]+student["Django"]+student["AWS"]

def get_average(student):
    return get_sum /4 

def to_string(student):
    return f'{student["name"]}\t{get_sum(student)}\t{get_average(student)}'

oz_students=[
    create_oz_students("이름1",4,2,4,2),
    create_oz_students("이름2",5,2,1,1),
    create_oz_students("이름3",4,1,5,4),
    create_oz_students("이름4",2,4,3,2)
]

print("이름","총점","평균",sep="\t")

for student in oz_students:
    print(to_string(student))

'''
객체와 관련 코드를 분라헐 수 있게 하는 것이 객체 지향 프로그램의 핵심.
개발자들은 이런 객체 지향 프로그램을 반복적으로 만들다보니 구조를 자동으로 만들어줄 클래스의 구조를 만들게 됨.


클래스 선언!!!!!

class 첫자리대문자 클래스 이름:
    클래스 내용
    ...

oz student -> OzStudent

ex)))))))))))

클래스 선언
class Test: 첫 자리는 무조건 대문자
    pass

클래스의 이름과 동일한 함수로 객체를 만들어야 함.
객체이자 인스턴스(클래스를 이용해서 만든 객체) = 클래스 명과 동일한 생성자 함수()
student=Test()




'''





