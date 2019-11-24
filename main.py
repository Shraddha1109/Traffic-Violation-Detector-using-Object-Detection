import os
import json
from detector import detect_item
from flask import Flask,render_template,request,redirect,flash,session
from models import db,Admin
from detector import detect_item
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "my college "
db.init_app(app)
db.create_all(app=app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            admin = Admin.query.filter_by(email=email).first()
            if admin:
                if password == admin.password:
                    session['admin']=admin.name
                    session['islogged'] =True
                    flash('login successfull!')
                    return redirect('/home')
                else:
                    flash('password invalid','danger')
            else:
                flash('email invalid','danger')
        else:
            flash("could not find user details! try again",'danger')
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        phone = request.form.get('phone')
        if email and password and name and phone:
            if len(password) > 5:
                admin =Admin(email = email,password = password,name = name,phone = phone)
                db.session.add(admin)
                db.session.commit()
                flash('thanks for registering admin.')
                return redirect('/login')
            else:
                flash("password is invalid, should be greater than 5","danger")
        else:
            flash("invalid details",'danger')
    return render_template('register.html')


@app.route('/home',methods=['POST','GET'])
def home():
    if not session.get('islogged'):
        return redirect('/')
    return render_template('index.html',)

@app.route('/about',methods=['POST','GET'])
def about():
    return render_template('about.html')

@app.route('/uploads',methods=['POST','GET'])
def uploads():
    if request.method=='POST':
        if 'file' not in request.files:
            flash('No file found')
            return redirect(request.url)
        uploaded_file = request.files['file']

        if uploaded_file.filename == ' ':
            flash('No selected file')
            return redirect(request.url)
        else:
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return showtext(filename)

    return render_template('index.html')

def showtext(filename):
    path = os.path.join("static/uploads", filename)
    text = detect_item(path)
    return render_template('result.html', filename = path, data = json.loads(text))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)