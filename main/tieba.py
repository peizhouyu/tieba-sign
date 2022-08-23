#! python3
# -*- coding:utf-8 -*-

import requests
import re
import hashlib
import json
import time
from urllib import request
from urllib import parse
from urllib.request import urlopen


class tieba:
    # bduss
    bduss = ''
    # 填入自己的百度id
    myid = ''

    url = 'http://tieba.baidu.com/home/main?un=' + myid + '&fr=index'
    headers = {'Cookie': 'BDUSS=' + bduss}
    lists = []

    def __init__(self):
        self.get_list()

    def chlis(self, kw):
        for i in range(len(self.lists)):
            if self.lists[i]['name'] == kw:
                self.lists[i]['is_sign'] = 1

    def get_list(self):
        r = requests.get(self.url, headers=self.headers)
        rul = re.findall(r'forumArr":(\[.+?), "ihome"', r.text)[0]
        ruls = re.findall(r'{.+?}', rul)
        for i in ruls:
            one = eval(i)
            self.lists.append(
                {'name': one['forum_name'], 'is_sign': one['is_sign']})

    def getPostData(self, kws):
        tbs = requests.get('http://tieba.baidu.com/dc/common/tbs',
                           headers=self.headers).json()['tbs']
        get_fid_url = 'http://tieba.baidu.com/f/commit/share/fnameShareApi?ie=utf-8&fname=%s' % kws
        fid = requests.get(get_fid_url, headers=self.headers).json()[
            'data']['fid']
        return {'fid': fid, 'kw': kws, 'BDUSS': self.bduss, 'tbs': tbs}

    def getData(self, postDict):
        return {'ie': 'utf-8', 'kw': postDict['kw'], 'tbs': postDict['tbs']}

    def sign(self, kw):
        postDict = self.getPostData(kw)
        data = self.getData(postDict)
        postData = parse.urlencode(data).encode('utf-8')
        print(postData)
        headers_arg = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        cookies = {
            'BDUSS': tieba.bduss
        }
        r = requests.post(
            'https://tieba.baidu.com/sign/add', data=data, headers=headers_arg, cookies=cookies)
        info = r.json()
        if info['error'] == '':
            self.chlis(kw)
            print('Success:%s' % kw)
            return 0
        else:
            print('Fail:%s' % kw)
            return 1


def main():
    tb = tieba()
    flag = 1
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    print('********************')
    while flag:
        try:
            flag = sum([tb.sign(k['name']) for k in tb.lists if not k['is_sign']])
        except ValueError:
            print("error")

    print('********************\nAll Finished!\n\n')


if __name__ == '__main__':
    main()
