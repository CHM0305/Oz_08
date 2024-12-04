
'''
프라이빗 변수 사용코드
클래스 안에 함수 안 코드가 실행되는 변수에 
__변수명에 언더바 두개를 붙혀주면
수정을 할 수 없는 변수가 된다.
self.__변수명 

'''
import math

class OzCircle:
    def __init__(self, radius):
        self.__radius=radius
    def get_circumference(self):
        return 2*math.pi*self.__radius
    def get_area(self):
        return math.pi *(self.__radius**2)


circle = OzCircle(10)
#원래 입력 들어가는 매개변수는 10인데 반지름 값을 마음대로 입력하게해도 가능
#하지만 변경되면 안되는 값이 변경이 되었기에 이런 외부에서 내부 값을 맘대로 변경이 가능하지 못하게 하는 것이 프라이빗 변수이다. 
circle.radius = -2
print("원의 둘레:",circle.get_circumference())
print("원의 넓이:",circle.get_area())

'''
상속 
지금까지 우리가 만든 클래스 안에 일부내용을 추가하거나 변경하는 것을 상속이라 한다.

다중 상속
상속은 기존 클래스의 추가나 변경을 하는 정도라면 다중 상속은 각각의 클래스에서 원하는 속성 또는 기능만
뽑아다가 사용하는 것을 말한다.
'''

#자식 클래스를 만들 때 사용할 부모 클래스
class Parent:
    def __init__(self):
        self.value="테스트"
        print("Parent 클래스의 __init()__메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child 클래스의 __init__() 메소드가 호출 되었다.")

child=Child()

child.test()

print(child.value,"진또배기")