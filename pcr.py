import os
import numpy as np
import random
s = '抽卡pcrup'
if s[0:2] == '抽卡':
    game = s.replace('抽卡', '')
    if 'pcr' in game:
        three_star_list = os.listdir('E:/CookBot/resource/pcr/3star')
        two_star_list = os.listdir('E:/CookBot/resource/pcr/2star')
        one_star_list = os.listdir('E:/CookBot/resource/pcr/1star')
        list_1star = list()
        list_2star = list()
        list_3star = list()
        p_normal = np.array([0.795, 0.18, 0.025])
        p_tenth = np.array([0.975, 0.025])
        for i in range(10):
            pick = np.random.choice([1, 2, 3], p=p_normal.ravel())
            if pick == 1:
                one_star_pick = random.choice(one_star_list)
                list_1star.append(one_star_pick)
        for i in range(len(list_1star)):
            print(list_1star[i])
