from flask import Flask,request,render_template,session
app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def login():
	if request.method=="POST":
		username=request.form.get('username')
		password=request.form.get('password')
		if (username=='admin' and password=='123'):
			#session['user']=username
			return f"Logged in {username}"
		else:
			return "incorrect login"
	return render_template("new.html")
if __name__=="__main__":
	app.run()

