from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)
list1=[]
@app.route('/',methods=['POST','GET'])
def Register():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        course=request.form.get('course')
        list1.append({
            "name":name,
            "email":email,
            "course":course
        })
        con=sqlite3.connect('new_db.db')
        cursor=con.cursor()
        cursor.execute(
            "INSERT INTO user (name, email, course) VALUES (?, ?, ?)",
            (name, email, course)
        )
        con.commit()
        con.close()
        return render_template('Register.html',list1=list1)
    return render_template('Form.html')
    
@app.route('/students')    
def show():
    return render_template('Students.html',list1=list1)
if __name__=="__main__":
    app.run(debug=True)