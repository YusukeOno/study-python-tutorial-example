# 最初のコード
import random

options = ['グー', 'チョキ', 'パー']  # 選択肢
print('{1} グー\n{2} チョキ\n{3} パー')
human_choice = options[int(input('「グー」か「チョキ」か「パー」を番号で選んでください'))-1]
