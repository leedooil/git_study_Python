def open_account():
    print("새로운 계좌가 생성되었습니다.")
    
def deposit(balance, money): # 입금
    print("{0}원 입금이 완료되었습니다. 잔액은 {1}원입니다.".format(money,balance+money))
    return balance+money

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("{0}원 출금이 완료되었습니다. 잔액은 {1}원입니다.".format(money,balance - money))
        return balance-money
    else:
        print("출금 잔액이 부족합니다. 잔액은 {0}원입니다.".format(balance))     
        return balance

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 저녁 출금 수수료 100원
    return commission, balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)    

balance = deposit(balance, 1000)
print(balance)

# balance = withdraw(balance,1000)
# print(balance)    

# balance = withdraw(balance,1000)
# print(balance)    

# balance = withdraw(balance,1000)
# print(balance)

commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))    
