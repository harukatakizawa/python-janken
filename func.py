def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def result(player, computer):
    if player == computer:
        return '引き分け'
    elif player == 0 and computer == 1 or player == 1 and computer == 2 or player == 2 and computer == 0:
        return '勝ち'
    return '負け'



