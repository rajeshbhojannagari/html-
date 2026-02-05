from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/feedback',methods=['GET','POST'])
def feedback():
    error=None

    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        message=request.form.get('message')
        if not name or not email or not message:
            error="All fields need to entered"
            return render_template('feedback.html',error=error)
        elif '@' not in email:
            error="Invalid email address"
            return render_template('feedback.html',error=error)
        else:
            print(name,email,message)
        return render_template('thankyou.html',name=name)
    return render_template('feedback.html',error=error)
if __name__=="__main__":
    app.run(debug=True)