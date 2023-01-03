import secrets
import sys
secureNum=secrets.SystemRandom()

while True:
    print('___Welcome to our Game___')
    press1 = int(input('press 1 to Read Rule and press 2 to Play Game:>'))
    if press1==1:
        print('>Age must be more than 18:')
        print('>Show money more than 5000')
        print('>U must use more than 1000 each time:')
    if press1==2:
        uName=input('Please enter your name:>')
        uAge=int(input('Please enter your age:>'))

        while len(uName)>2 and uAge>17:
            print('You can play game now')
            print('Welcome:>', uName)
            while True:
                sMoney=int(input('Please enter your show money:>'))
                while sMoney>4999:
                    while True:
                        print('This is your money $',sMoney)
                        inputMoney=int(input('Please enter money to play:>'))
                        luckyNum=int(input('Please enter your lucky number:>'))
                        systemNum=secureNum.randint(00,99)
                        if luckyNum==systemNum:
                            print('You are win in 2D Game')
                            sMoney=(inputMoney*10)+(sMoney-inputMoney)
                            print('This is your All Money $', sMoney)
                            toQuit=int(input('Press 0 to play Again:>'))
                            if toQuit!=0:
                                sys.exit('Bye Bye')
                            else:
                                continue
                        
                        print('Try again....Luckynumber is',systemNum)
                        sMoney=sMoney-inputMoney
                        if sMoney<1000:
                            print('You have not enough money $',sMoney)
                            break

                print("Please More Money,Money is invalid")

        print('Please read again the rule')

        
