from flask import Flask, render_template, request, redirect , url_for
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def dbwrite_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        msg = data["message"]
        csv_writer = csv.writer(database2, delimiter=',')
        csv_writer.writerow([email,subject,msg])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            dbwrite_csv(data)
            return redirect('/thankyou.html')
        except: 
            return 'Sorry! unsaved form'
    else:
        return 'Somthing went wrong, try again!'


if __name__ == "__main__":
    app.run()