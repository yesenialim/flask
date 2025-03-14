from flask import Flask, render_template, request
app= Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/report')
def report():
  lower_letter=False
  upper_letter=False
  contains_digit=False
  contains_special=False
  username=request.args.get('username')
  lower_letter=any(c.islower()for c in username)
  upper_letter=any(c.isupper()for c in username)
  contains_digit=any(c.isdigit() for c in username)
  special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
  contains_special= any(char in special_chars for char in username)
  report= lower_letter and upper_letter and contains_special and contains_digit 
  return render_template('report.html', report=report, lower=lower_letter, upper=upper_letter, contains_digit=contains_digit, contains_special=contains_special)

if __name__=='__main__':
  app.run(debug=True)