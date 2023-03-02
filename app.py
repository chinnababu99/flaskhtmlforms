from flask import Flask,render_template,request

AI=Flask(__name__)

@AI.route('/firsthtml',methods=['GET','POST'])

def firsthtml():
    if request.method=='POST':
        from_data=request.form
        return from_data['name']
    
    return render_template('first.html')


if __name__=='__main__':
    AI.run(debug=True)
