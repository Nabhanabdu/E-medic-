# def signup():
#     error = None
#     if request.method == 'POST':
#         # Retrieve data from form
#         fname = request.form['fname']
#         lname = request.form['lname']
#         email = request.form['email']
#         pwd = request.form['pwd']
#         cat = request.form['cat']

#         # Create a new user in the Firestore database
#         db.collection('users').add({
#             'fname': fname,
#             'lname': lname,
#             'email': email,
#             'pwd': pwd,
#             'cat': cat
#         })

#         # Redirect to the sign-up success page
#         return redirect(url_for('success'))

#     # If not a POST request, display the sign-up form
#     return render_template('register.html', error=error)