from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
    return url_for('static', filename='style.css')
    return url_for('static', filename='img.jpg')



@app.route('/login.html')
def login():
    return render_template("login.html")
    return url_for('static', filename='style.css')
    return url_for('static', filename='img.jpg')


@app.route('/index.html')
def index():
    return render_template("index.html")
    return url_for('static', filename='style.css')
    return url_for('static', filename='img.jpg')

@app.route('/logged_in.html')
def logged_in():
	return render_template("logged_in.html")
	return url_for("static",filename='style.css')
	return url_for('static',filename='img.jpg')


@app.route('/wrong.html')
def wrong_username_password():
  return render_template("wrong.html")
  return url_for("static",filename='style.css')
  return url_for('static',filename='img.jpg')

@app.route('/sent.html')
def message_sent_succesfully():
  return render_template("sent.html")
  return url_for("static",filename='style.css')
  return url_for('static',filename='img.jpg')


def read_csv(data,data2):
     with open("data.csv",'r') as my_data:
         reader = csv.reader(my_data)
         next(reader)
         print(reader)
         


         for x,y in reader:
                if x  ==  data and y== data2:
                       
                       
                    return redirect("/logged_in.html")
                                    
                elif data and data2 is None:
                  raise FileNotFoundError



         else :
              return redirect("/wrong.html")


@app.route('/login.html', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      
        response = request.form["username"]
        response2 = request.form['passkey']
       
        return read_csv(response,response2)

    





def write_to_csv(data3):
  with open('data2.csv', newline='', mode='a') as database2:
    name = data3["name"]
    email = data3["email"]
    message = data3["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([name,email,message])


@app.route('/logged_in.html', methods=['POST', 'GET'])
def submit_form2():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/sent.html")
      except:
        return 'did not save to database'
    else:
      return 'something went wrong. Try again!'


