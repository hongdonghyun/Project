import chat
import sys

def turn_on():
    print(' = Turn on game=')

    while True:
        choice = input('1 : go to shop, 2 : play game, 3 : print_message, 4 : sum, 0 : exit')
        if choice =='0':
            break
        elif choice =='1':
            pass
        elif choice =='2':
            pass
        elif choice =='3':
            chat.send_message()
        else:
            print('다시 입력')


if __name__ == '__main__':
    turn_on()
