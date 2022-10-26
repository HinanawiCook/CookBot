import os
import numpy as np
import random
genshin_pick_result_small_baodi = ''
genshin_pick_result_big_baodi = ''


def genshin_pick_small_baodi():
    global genshin_pick_result_small_baodi
    global genshin_pick_result_big_baodi
    five_star_list = os.listdir('E:/CookBot/resource/genshin/5star')
    four_star_list = os.listdir('E:/CookBot/resource/genshin/4star')
    up_four_star_list = os.listdir('E:/CookBot/resource/genshin/up4star')
    five_star_pick_list = list()
    four_star_pick_list = list()
    five_star_pick_number = list()
    four_star_pick_number = list()
    up_5star_character = '妮露'
    result = '当前卡池：妮露' + '\n' + '五星:'
    count = 0
    up_get = 0
    small_baodi = 1
    five_star_p = 0.006
    four_star_p = 0.051
    three_star_p = 0.943
    p_pick = np.array([three_star_p, four_star_p, five_star_p])
    p_wai = np.array([0.5, 0.5])
    p_small_baodi = np.array([1 - five_star_p, five_star_p])
    while up_get == 0:
        count += 1
        if count <= 73:
            if small_baodi < 10:
                pick = np.random.choice([3, 4, 5], p=p_pick.ravel())
                if pick == 5:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        five_star_pick_list.append(up_5star_character)
                        five_star_pick_number.append(count)
                        up_get = 1
                    else:
                        five_star_pick = random.choice(five_star_list)
                        five_star_pick_list.append(five_star_pick)
                        five_star_pick_number.append(count)
                        genshin_pick_big_baodi()
                        up_get = 1
                elif pick == 4:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        four_star_pick = random.choice(up_four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                    else:
                        four_star_pick = random.choice(four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                else:
                    small_baodi += 1
            else:
                pick = np.random.choice([4, 5], p=p_small_baodi.ravel())
                if pick == 5:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        five_star_pick_list.append(up_5star_character)
                        five_star_pick_number.append(count)
                        up_get = 1
                    else:
                        five_star_pick = random.choice(five_star_list)
                        five_star_pick_list.append(five_star_pick)
                        five_star_pick_number.append(count)
                        genshin_pick_big_baodi()
                        up_get = 1
                elif pick == 4:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        four_star_pick = random.choice(up_four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                    else:
                        four_star_pick = random.choice(four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
        elif count <= 89:
            five_star_p += 0.059710
            three_star_p -= 0.059710
            if small_baodi < 10:
                p_pick = np.array([three_star_p, four_star_p, five_star_p])
                pick = np.random.choice([3, 4, 5], p=p_pick.ravel())
                if pick == 5:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        five_star_pick_list.append(up_5star_character)
                        five_star_pick_number.append(count)
                        up_get = 1
                    else:
                        five_star_pick = random.choice(five_star_list)
                        five_star_pick_list.append(five_star_pick)
                        five_star_pick_number.append(count)
                        genshin_pick_big_baodi()
                        up_get = 1
                if pick == 4:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        four_star_pick = random.choice(up_four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                    else:
                        four_star_pick = random.choice(four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                else:
                    small_baodi += 1
            else:
                p_small_baodi = np.array([1 - five_star_p, five_star_p])
                pick = np.random.choice([4, 5], p=p_small_baodi.ravel())
                if pick == 5:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        five_star_pick_list.append(up_5star_character)
                        five_star_pick_number.append(count)
                        up_get = 1
                    else:
                        five_star_pick = random.choice(five_star_list)
                        five_star_pick_list.append(five_star_pick)
                        five_star_pick_number.append(count)
                        genshin_pick_big_baodi()
                        up_get = 1
                elif pick == 4:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        four_star_pick = random.choice(up_four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                    else:
                        four_star_pick = random.choice(four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
        elif count == 90:
            if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                five_star_pick_list.append(up_5star_character)
                five_star_pick_number.append(count)
                up_get = 1
            else:
                five_star_pick = random.choice(five_star_list)
                five_star_pick_list.append(five_star_pick)
                five_star_pick_number.append(count)
                genshin_pick_big_baodi()
                up_get = 1
    for i in range(len(five_star_pick_list)):
        result = result + five_star_pick_list[i] + str(five_star_pick_number[i]) + ' '
    result = result + '\n' + '四星:'
    for i in range(len(four_star_pick_list)):
        result = result + four_star_pick_list[i] + str(four_star_pick_number[i]) + ' '
    result = result + '共' + str(len(four_star_pick_list)) + '只!'
    result = result + '\n' + '共' + str(count) + '抽！'
    genshin_pick_result_small_baodi = result
    print(genshin_pick_result_small_baodi)


def genshin_pick_big_baodi():
    global genshin_pick_result_small_baodi
    global genshin_pick_result_big_baodi
    four_star_list = os.listdir('E:/CookBot/resource/genshin/4star')
    up_four_star_list = os.listdir('E:/CookBot/resource/genshin/up4star')
    five_star_pick_list = list()
    four_star_pick_list = list()
    five_star_pick_number = list()
    four_star_pick_number = list()
    up_5star_character = '妮露'
    result = '当前卡池：妮露' + '\n' + '五星:'
    count = 0
    up_get = 0
    small_baodi = 1
    five_star_p = 0.006
    four_star_p = 0.051
    three_star_p = 0.943
    p_pick = np.array([three_star_p, four_star_p, five_star_p])
    p_wai = np.array([0.5, 0.5])
    p_small_baodi = np.array([1 - five_star_p, five_star_p])
    while up_get == 0:
        count += 1
        if count <= 73:
            if small_baodi < 10:
                pick = np.random.choice([3, 4, 5], p=p_pick.ravel())
                if pick == 5:
                    five_star_pick_list.append(up_5star_character)
                    five_star_pick_number.append(count)
                    up_get = 1
                elif pick == 4:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        four_star_pick = random.choice(up_four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                    else:
                        four_star_pick = random.choice(four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                else:
                    small_baodi += 1
            else:
                pick = np.random.choice([4, 5], p=p_small_baodi.ravel())
                if pick == 5:
                    five_star_pick_list.append(up_5star_character)
                    five_star_pick_number.append(count)
                    up_get = 1
                elif pick == 4:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        four_star_pick = random.choice(up_four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                    else:
                        four_star_pick = random.choice(four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
        elif count <= 89:
            five_star_p += 0.059710
            three_star_p -= 0.059710
            if small_baodi < 10:
                p_pick = np.array([three_star_p, four_star_p, five_star_p])
                pick = np.random.choice([3, 4, 5], p=p_pick.ravel())
                if pick == 5:
                    five_star_pick_list.append(up_5star_character)
                    five_star_pick_number.append(count)
                    up_get = 1
                if pick == 4:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        four_star_pick = random.choice(up_four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                    else:
                        four_star_pick = random.choice(four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                else:
                    small_baodi += 1
            else:
                p_small_baodi = np.array([1 - five_star_p, five_star_p])
                pick = np.random.choice([4, 5], p=p_small_baodi.ravel())
                if pick == 5:
                    five_star_pick_list.append(up_5star_character)
                    five_star_pick_number.append(count)
                    up_get = 1
                elif pick == 4:
                    if np.random.choice([0, 1], p=p_wai.ravel()) == 0:
                        four_star_pick = random.choice(up_four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
                    else:
                        four_star_pick = random.choice(four_star_list)
                        four_star_pick_list.append(four_star_pick)
                        four_star_pick_number.append(count)
                        small_baodi = 1
        elif count == 90:
            five_star_pick_list.append(up_5star_character)
            five_star_pick_number.append(count)
            up_get = 1
    for i in range(len(five_star_pick_list)):
        result = result + five_star_pick_list[i] + str(five_star_pick_number[i]) + ' '
    result = result + '\n' + '四星:'
    for i in range(len(four_star_pick_list)):
        result = result + four_star_pick_list[i] + str(four_star_pick_number[i]) + ' '
    result = result + '共' + str(len(four_star_pick_list)) + '只!'
    result = result + '\n' + '共' + str(count) + '抽！'
    genshin_pick_result_big_baodi = result
    print(genshin_pick_result_big_baodi)


"""
def genshin_pick_send_message(id, to):
    global genshin_pick_result_small_baodi
    global genshin_pick_result_big_baodi
    if to == 'private':
        send_private_message(id, genshin_pick_result_small_baodi)
        send_private_message(id, genshin_pick_result_big_baodi)
    elif to == 'group':
        send_group_message(id, genshin_pick_result_small_baodi)
        send_group_message(id, genshin_pick_result_big_baodi)
    genshin_pick_result_small_baodi = ''
    genshin_pick_result_big_baodi = ''
"""

genshin_pick_small_baodi()
