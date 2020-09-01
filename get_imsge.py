# @Time : 2019/8/19 23:27 
# @Author : 白菜先森
# @File : get_imsge.py 
# @RSS ： https://blog.csdn.net/young_foryou/rss/list
# @Software: PyCharm

import requests,json,os

def get_img(keyword,page_size):
    url = 'http://image.baidu.com/search/acjson?'
    parameters = {
            "tn": "resultjson_com",
            "ipn": "rj",
            "ct": "201326592",
            "fp": "result",
            "queryWord": keyword,
            "cl": 2,
            "lm": -1,
            "ie": "utf-8",
            "oe": "utf-8",
            "st": -1,
            "ic": 0,
            "word": keyword,
            "face": 0,
            "istype": 2,
            "nc": 1,
            "pn": "",
            "rn": page_size,
            "gsm": "1e"
        }
    requests.get(url=url,params=parameters)
    # response = requests.get(url).content.decode('UTF-8')
    # data = json.loads(response)
    # print(type(data))
    # img = data['data'][0:-1]
    # j = 1
    # for i in img:
    #     print(i['middleURL'])
    #     pic = requests.get(i['middleURL'])
    #     if not os.path.exists(r'g:\img') :
    #         os.mkdir(r'g:\img')
    #     with open(r'g:\img\%d.jpg'%j,'wb') as f:
    #         f.write(pic.content)
    #     j+=1


# import requests
# r = requests.get('http://img2.imgtn.bdimg.com/it/u=3891665632,2012752376&fm=26&gp=0.jpg')
# with open('avatar.jpg','wb') as f:
#     f.write(r.content)