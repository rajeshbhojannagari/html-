from flask import Flask,redirect,url_for,session,Response,request

app=Flask(__name__)
app.secret_key="supersecretkey"
@app.route('/', methods=['POST','GET'])
def login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        if username=='admin' and password=='123':
            session['user']=username
            return redirect(url_for('Welcome'))
        else:
            return Response('Invalid credentials',401)
    return '''
        <form method="POST">
            Username: <input name="username" required><br>
            Password: <input name="password" type="password" required><br>
            <input type="submit">
        </form>'''
@app.route('/welcome')
def Welcome():
    if 'user' in session:
        return f"Welcome {session['user']}"
    '''<a href={url_for('logout')}></a>'''
    return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))
if __name__=="__main__":
    app.run(debug=True)