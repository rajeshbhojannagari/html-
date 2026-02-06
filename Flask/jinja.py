from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def hello():
    res_code=45000
    list1=['rajesh','rohith','srikar']
    return render_template('jinja.html',res_code=res_code,names=list1)
if __name__=="__main__":
    app.run()