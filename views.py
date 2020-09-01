import os,random
import datetime
from flask import request
from flask import render_template
from models import *
from manage import app,basedir,session

@app.route("/")
@app.route("/index/")
def index():
    return render_template("index.html")

@app.route("/update/")
def update():
    return render_template("update.html")

@app.route("/detail/")
def detail():
    return render_template("detail.html")

@app.route("/filelist/")
def filelist():
    per = 6
    filelist = Filelist.query.offset((1 - 1) * per).limit(per)
    count = Filelist.query.count()
    return render_template("filelist.html", **locals())
    # return render_template("filelist.html")

def sjtj():
    email = ['45654688@qq.com', '26578548@qq.com', '578548@qq.com', '578548@qq.com', '754578548@qq.com',
             '74878548@qq.com', '84578548@qq.com', '6342578548@qq.com', '2845278548@qq.com', '7867478548@qq.com',
             '85274578548@qq.com', '26542748@qq.com', '265762348@qq.com', '2654688548@qq.com', ]
    name = ['汤姆', '猫男爵', '露娜', '哆啦A梦', '艾露猫', '路飞', 'maliao', 'baicai', 'jounj', 'kjoia', 'hacnj', 'knjc']
    qq = ['246468', '5446', '5465465', '568568', '468598654', '5456568', '5656865', '4684635', '46885456', '654684', '165464565',
          '468543654', '654645634', '684654', '864684654', '68464']
    message = ['若能避开猛烈的欢喜，自然也不会有悲痛的来袭', '实不相瞒，还是会想你，但能克服，问题不大', '仅一夜之隔，我心竟判若两人', '所谓的世间，不就是个人吗',
               '他从人海中来。抱歉，这狂喜，我避无可避']
    for i in range(500):
        # print(i)
        nickname = random.choice(name)
        email1 = random.choice(email)
        q1 = random.choice(qq)
        print(qq,email,'/n')
        time1 = datetime.datetime.now()
        description = random.choice(message)
        art = Message(
            nickname = nickname,
            email=email1,
            qq = q1,
            time=datetime.datetime.now(),
            description=description,
        )
        session.add(art)
        session.commit()

@app.route("/gustbook/<int:num>")
def gustlist(num):
    per = 10
    message = Message.query.order_by(Message.id.desc()).offset((num-1)*per).limit(per)
    count = Message.query.count()
    return render_template("gustbook.html",**locals())

# @app.route("/gustbook/",methods=["POST","GET"])
# def gustbook():
#     if request.method == "POST":
#         formdata = request.form
#         nickname = formdata.get("nickname")
#         email = formdata.get("email")
#         qq = formdata.get("qq")
#         time = datetime.datetime.now()
#         description = formdata.get("comment")
#         # sjtj()
#         art = Message(
#             nickname = nickname,
#             email = email,
#             qq = qq,
#             time = time,
#             description = description,
#         )
#         session.add(art)
#         session.commit()
#
#     count = Message.query.count()
#     message = Message.query.filter(Message.id>count-10).order_by("id desc")
#     return render_template("gustbook.html",**locals())

# @app.route("/gustbook/")
# def gustbook():
#     message = Message.query.all()
#     count = Message.query.count()
#     return render_template("gustbook.html",**locals())

# @app.route("/aList/")
# def articleList():
#     artList = Article.query.all()
#     return render_template("article_list.html",**locals())
#
# @app.route("/article/<int:id>/")
# def article(id):
#     return render_template("article.html")
#
# @app.route("/register/",methods=["POST","GET"])
# def register():
#     if request.method == "POST":
#         formdata = request.form
#         title = formdata.get("title")
#         author = formdata.get("author")
#         types = formdata.get("types")
#         description = formdata.get("description")
#         content = formdata.get("content")
#         time = datetime.datetime.now()
#
#         fileData = request.files
#         image = fileData.get("picture")
#         path = os.path.join(
#             os.path.join(basedir,"static/images"),
#             image.filename
#         )
#         art = Article(
#             title = title,
#             author = author,
#             types = types,
#             time = time,
#             description = description,
#             content = content,
#             picture = "/static/images/"+image.filename
#         )
#         image.save(path)
#         session.add(art)
#     return render_template("register.html")
