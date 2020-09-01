import random,datetime

email = ['45654688@qq.com', '26578548@qq.com', '578548@qq.com', '578548@qq.com', '754578548@qq.com',
         '74878548@qq.com', '84578548@qq.com', '6342578548@qq.com', '2845278548@qq.com', '7867478548@qq.com',
         '85274578548@qq.com', '26542748@qq.com', '265762348@qq.com', '2654688548@qq.com', ]
name = ['汤姆', '猫男爵', '露娜', '哆啦A梦', '艾露猫', '路飞', 'maliao', 'baicai', 'jounj', 'kjoia', 'hacnj', 'knjc']
qq = ['246468', '5446', '5465465', '568568', '468598654', '5456568', '5656865', '4684635', '46885456', '654684', '165464565',
      '468543654', '654645634', '684654', '864684654', '68464']
message = ['若能避开猛烈的欢喜，自然也不会有悲痛的来袭', '实不相瞒，还是会想你，但能克服，问题不大', '仅一夜之隔，我心竟判若两人', '所谓的世间，不就是个人吗',
           '他从人海中来。抱歉，这狂喜，我避无可避']
print(type(random.choice(email)))
# for i in range(500):
#     # print(i)
#     nickname = random.choice(name)
#     print(nickname)
#     email = random.choice(email)
#     qq = random.choice(qq)
#     time1 = datetime.datetime.now()
#     description = random.choice(message)
    # art = Message(
    #     nickname=nickname,
    #     email=email,
    #     qq=qq,
    #     time=datetime.datetime.now(),
    #     description=description,
    #
    # )