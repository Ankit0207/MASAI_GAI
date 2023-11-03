from flask import Flask, request, render_template, redirect

app = Flask(__name__)

users = {}


@app.route('/create', methods=['GET', 'POST'])
def create_user_form():
    if request.method == 'POST':
        # Retrieve users from the form
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']

        # Create a new entry in the dictionary
        users[name] = {'email': email, 'phone': phone, 'gender': gender}
        return redirect('/read')

    return render_template('user_form.html')


@app.route('/read')
def read_users():

    return render_template('read_users.html', users=users)


@app.route('/update/<name>', methods=['GET', 'POST'])
def update_user(name):
    if request.method == 'POST':
        # Retrieve users from the form
        updated_email = request.form['email']
        updated_phone = request.form['phone']
        updated_gender = request.form['gender']

        # Update an existing entry in the dictionary
        users[name] = {'email': updated_email,
                       'phone': updated_phone, 'gender': updated_gender}

        return redirect('/read')

    email = users[name]['email']
    phone = users[name]['phone']
    gender = users[name]['gender']
    return render_template('update_users.html', name=name, email=email, phone=phone, gender=gender)


@app.route('/delete/<name>')
def delete_user(name):
    # Delete an existing entry from the dictionary
    del users[name]
    return redirect('/read')


if __name__ == '__main__':
    app.run()
