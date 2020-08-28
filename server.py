from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def my_portfolio(page_name):
    return render_template(page_name)

#writing to a text file
#def write_to_file(data):
#	with open('database.txt', mode='a') as database:
#		email = data['email']
#		subject = data['subject']
#		message = data['message']
#		database.write(f"Email:{email}\nSubject:{subject}\nMessage:{message}\n\n")

#writing to a csv file
def write_to_csv(data):
	with open('database.csv',newline = '', mode = 'a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
    		data = request.form.to_dict()
    		#write_to_file(data)
    		write_to_csv(data)
    		return redirect('thankyou.html')
    	except:
    		return 'Unable to save to database.'
    else:
    	return "Somthing went wrong. Try again."