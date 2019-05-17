from flask import Flask,render_template,request,redirect,url_for
from db import db
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/combo')
def combo():
  return render_template('combo.html')

@app.route('/blog')
def blog():
   return render_template('blog.html')
   
@app.route('/blog-single')
def blog_singer():
   return render_template('blog-single.html')

@app.route('/tour-single')
def tour_singer():
   return render_template('tour-single.html')

@app.route('/thank')
def thank():
   return render_template('thank.html')

@app.route('/tour-form')
def tour_form():
   return render_template('tour-form.html')

@app.route('/tour-form',methods=['POST'])
def post_tour_form():
   name = request.form.get('name')
   namsinh = request.form.get('namsinh')
   address = request.form.get('address')
   address2 = request.form.get('address2')
   yc = request.form.get('yc')
   dicung = request.form.get('dicung')
   songuoi = request.form.get('songuoi')
   db.tour.insert_one({'name':name,'namsinh':namsinh,'address':address,'address2':address2,'yc':yc,'dicung':dicung,'songuoi':songuoi})
   return render_template('tour-form.html')

   
if __name__ == '__main__':
  app.run(debug=True)



 