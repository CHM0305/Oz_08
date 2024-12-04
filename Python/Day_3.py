'''
__[문제 1: 잔액 확인]__

현재 잔액은 1000원입니다. 현재 잔액을 출력하세요. 

(변수명 예시 : 잔액 - balance)



balance = 1000


__[문제 2: 입금]__

가지고 있는 돈을 입금합니다.

입금 금액을 입력받고, 잔액을 갱신한 후 새로운 잔액을 출력하세요. 입금 거래를 영수증 리스트에 기록하세요.

- 입금 금액은 input()을 이용해 받습니다.
- 영수증은 list()로 선언합니다.
- 영수증에 들어가는 정보는 튜플 형태입니다.
- 튜플에 담기는 정보는 (입금 or 출금, 입금 or 출금 금액, 현재 잔액)순 입니다.

(변수명 예시: 영수증 리스트 - receipts, 입금 금액 - deposit_amount)



receipts =[]
balance=1000

#입금기능
deposit_amount=int(input("입금할 금액을 입력해주세요 : "))
balance = balance+deposit_amount 
receipts.append(("입금",deposit_amount,balance))
print(f'입금하신 금액은 {deposit_amount}원 입니다. 현재 잔액은 {balance}원 입니다.')

print(receipts)



__[문제 3: 출금]__

사용자가 돈을 출금합니다. 출금 금액을 입력받고, 잔액을 갱신한 후 새로운 잔액을 출력하세요. 출금 거래를 영수증 리스트에 기록하세요. 

- 출금 금액은 input()을 이용해 받습니다.
- 현재 잔액보다 출금 요청 금액이 많을 경우 현재 잔액 만큼만 출금되도록 합니다.
- 영수증에 들어가는 정보는 튜플 형태입니다.
- 튜플에 담기는 정보는 (입금 or 출금, 입금 or 출금 금액, 현재 잔액)순 입니다.

(변수명 예시: 출금금액 - withdraw_amount)


withdraw_amount=int(input("출금할 금액을 입력해주세요 : "))
withdraw_amount=min(balance, withdraw_amount) #(4000 6000)/(5000 10000) 둘 중 출금 가능한 금액을 min으로 비교해준다.
balance -= withdraw_amount 
receipts.append(("출금",withdraw_amount,balance))# append의 결과 값은 바로 출력이 불가능하다. 그래서 f문만을 이용해서 출력 가능함
print(f'출금하신 금액은 {deposit_amount}원 입니다. 현재 잔액은 {balance}원 입니다.')

'''
receipts =[] #while 문 안에 있으면 영수증 값이 계속해서 초기화되니 주의!!
balance=1000


while True:
    num = int(input("사용하실 기능을 선택해주세요(1. 입금 2.출금 3.영수증 4.종료)"))
    if num==1 :
        #입금기능
        deposit_amount=int(input("입금할 금액을 입력해주세요 : "))
        balance = balance+deposit_amount 
        receipts.append(("입금",deposit_amount,balance))
        print(f'입금하신 금액은 {deposit_amount}원 입니다. 현재 잔액은 {balance}원 입니다.')
    elif num==2 :
        #출금기능
        withdraw_amount=int(input("출금할 금액을 입력해주세요 : "))
        withdraw_amount=min(balance, withdraw_amount) #(4000 6000)/(5000 10000) 둘 중 출금 가능한 금액을 min으로 비교해준다.
        balance -= withdraw_amount 
        receipts.append(("출금",withdraw_amount,balance))# append의 결과 값은 바로 출력이 불가능하다. 그래서 f문만을 이용해서 출력 가능함
        print(f'출금하신 금액은 {deposit_amount}원 입니다. 현재 잔액은 {balance}원 입니다.')
    elif num==3:
        print(receipts)
    elif num==4:
        break
print("서비스 종료")