stock = {"팥붕": 10,
        "슈붕": 5,
        "잡채붕": 3
    }
#스턱이라는 값을 할당한거 기능 아님
sales={
        "팥붕": 10,
        "슈붕": 5,
        "잡채붕": 3

}

price = {"팥붕": 1500,
        "슈붕": 2000,
        "잡채붕": 2500
    }

#메인이라는 함수에 이러한 코드를 넣음, 정의
def main():
    while True:
        mode = input("원하는 모드를 선택해주세요.(1. 주문 2. 관리자 3. 종료 )\n-> ")
        if mode =="3":
            break
        if mode == "2":
            order_bread()
        if mode == "1":
            manage_bread()


#
def order_bread():
    while True:

        t_order=input("주문을 선택하셨습니다! \n주문할 붕어빵의 맛을 선택해주세요!\n->")
        
        if t_order =="뒤로가기":
            break
        t_count=int(input("주문할 붕어빵 개수를 입력하세요."))

        if stock[t_order]>=t_count:
            stock[t_order]-=t_count
            sales[t_order]+=t_count
            print(f"{t_order}{t_count}개가 판매되었습니다.")
        
        else:
            result=t_count-stock[t_order]
            print(f"죄송합니다. {t_order}의 수량이 {result}개가 부족합니다. ")


        print("\n현재 재고는")
        for b_type, b_count in stock.items():
            print(f" {b_type}: {b_count}")
            print("-----------")
        else:
            print("3가지 맛 중에 선택해주세요.")

def manage_bread():
        
    while True:
            print("재고추가를 선택하셨습니다!\n")
            b_type = input("추가할 붕어빵 종류를 입력하세요.\n -팥붕\n -슈붕\n -잡채붕\n -->")
            if b_type == "종료":
                break
            b_count = int(input("붕어빵 개수를 입력하시오")) 
            stock[b_type]+=b_count
            print(f"{b_type}의 재고를 {b_count}추가 완료했습니다.\n 현재 {stock[b_type]}입니다.")

main()

print("시스템이 종료되었습니다.")

total=0

for t_bread in sales:
    money = stock[t_bread] * price[t_bread]
    total += money

print(f"총 매출{total}")