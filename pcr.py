import os
import numpy as np
import random


def pcr_pick_ten():
    three_star_list = os.listdir('E:/CookBot/resource/pcr/3star')
    two_star_list = os.listdir('E:/CookBot/resource/pcr/2star')
    one_star_list = os.listdir('E:/CookBot/resource/pcr/1star')
    pick_list = list()
    p_normal = np.array([0.795, 0.18, 0.025])
    p_tenth = np.array([0.975, 0.025])
    for i in range(9):
        normal_pick = np.random.choice([1, 2, 3], p=p_normal.ravel())
        if normal_pick == 3:
            three_star_pick = random.choice(three_star_list)
            pick_list.append('#' + three_star_pick + '#')
        elif normal_pick == 2:
            two_star_pick = random.choice(two_star_list)
            pick_list.append(two_star_pick)
        elif normal_pick == 1:
            one_star_pick = random.choice(one_star_list)
            pick_list.append(one_star_pick)
    tenth_pick = np.random.choice([2, 3], p=p_tenth.ravel())
    if tenth_pick == 3:
        three_star_pick = random.choice(three_star_list)
        pick_list.append('#' + three_star_pick + '#')
    elif tenth_pick == 2:
        two_star_pick = random.choice(two_star_list)
        pick_list.append(two_star_pick)
        print('十连！')
        print(pick_list)


s = '抽卡pcrup'
if s[0:2] == '抽卡':
    game = s.replace('抽卡', '')
    if 'pcr' in game:
        pcr_pick_ten()
