from flask import Flask, render_template, request

app = Flask("__name__")
@app.route('/contact', methods=['GET','POST'])

def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        msg = request.form['message']
        print('hello')
        print(f'Data Submitted: \n ${name}  \n ${email}  \n ${msg}')
        return render_template('index.html', data=f'${name} ${email} ${msg}')
    else: 
        return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
