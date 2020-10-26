from flask import *  
import os


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)  


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')  
def upload():  
    return render_template("index.html")  


# sudoku_puzzle.jpg
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        print(f.filename)
        print(type(f))
        if f and allowed_file(f.filename):
            f.filename = 'sudoku_puzzle.' + f.filename.rsplit('.', 1)[1].lower()
            f.save('static/' + f.filename)
            return render_template("success.html", name = f.filename)  
        else:
            return render_template("index.html") 


if __name__ == '__main__':  
    app.run(debug = True)  