print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP16,board.GP17,board.GP18,board.GP22,board.GP26,board.GP28)
keyboard.row_pins = (board.GP21,)
#keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    #原神音ゲーのキー配列(ヘブバンは自由に変更可能なので原神に合わせます。)
    #A,S,D,J,K,L
    [KC.A,KC.S,KC.D,KC.J,KC.K,KC.L]
]

if __name__ == '__main__':
    keyboard.go()