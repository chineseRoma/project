from  flask  import Flask,request,render_template,redirect
import mysql,time
id = None
app = Flask(__name__)
@app.route("/")
# 登录页面
def login_viwe():
    return render_template('login.html')

@app.route("/login",methods=["POST"])
# 登录
def login():
    # 获取前端登录账户密码
    result = request.form.to_dict()
    # 对用户登录信息进行判断
    if mysql.sql("select name from users where password=%s",result['password']):
        # 登录成功
        global id
        id = mysql.sql("select id from users where password=%s and name=%s",result['password'],result['name'])
        # 获取用户id,方便主页面进行登录判断
        # 登录成功，返回indenx函数，跳转indenx主页面
        return indenx()
    else:
        # 登录失败,返回登录页面
        return '<script>alert("登录失败,请重新登录");location.href="/"</script>'
    return '登录失败'

@app.route("/indenx")
# 主页面
def indenx():
    # 获取所有留言，传到前端
    sql = 'select * from messages order by id desc'
    data = mysql.sql(sql)
    indenx = 0
    for i in data:
        # 获取留言总条数
        indenx = indenx+1
    if id:
        # 通过id判断是否登录成功
        return render_template('indenx.html', data=data, i=indenx)

    else:
        return render_template('fail.html')

    return render_template('fail.html')
@app.route('/insert', methods=["POST"])
def insert():
    # 添加留言
    message = request.form.to_dict()
    # 获取前端信息
    if message['text']:
        # 获取当前时间插入数据
        ti = time.strftime('%Y-%m-%d %H:%I:%S')
        mysql.sql("insert into messages(message,time) value(%s,%s)", f"{message['text']}", f"{ti}")

        return redirect('http://39.107.79.10:3344/indenx')
    else:
        return '<script>alert("留言不可为空,请填写");location.href="/indenx"</script>'
    return '<script>alert("留言不可为空,请填写");location.href="/indenx"</script>'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='3344')
