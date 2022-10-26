import os
import random


def pcr_chouqian():
    pcr_chouqian_list = os.listdir('E:/CookBot/resource/pcr/chouqian')
    pcr_chouqian_pick = random.choice(pcr_chouqian_list)
    cq_pcr_chouqian_pick = '[CQ:image,file=file:///' + 'E:/CookBot/resource/pcr/chouqian/' + pcr_chouqian_pick + ']'
    print(cq_pcr_chouqian_pick)


s = '抽签'
if s == '抽签':
    pcr_chouqian()
