import random
import func

print('じゃんけんを始めます')

player = input('名前を入力してください:')

print('何を出しますか？(0: グー, 1: チョキ, 2: パー)')
hands = ['グー', 'チョキ', 'パー']

player_hand = int(input('数字で入力してください:'))

computer_hand = random.randint(0,2)

if func.validate(player_hand) == False:
    print('正しい数値を入力してください')
else:
    if player == '':
        player = 'ゲスト'
    print(player + 'は' + hands[player_hand] + 'を出しました')
    print('コンピューターは' + hands[computer_hand] + 'を出しました')
    print('結果は' + func.result(player_hand, computer_hand) + 'でした')

