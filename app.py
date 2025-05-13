from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import pymysql
from chatbot_model import get_bot_response  # Import the chatbot logic
import hashlib  # For password hashing

app = Flask(__name__)
app.secret_key = "fce4809ce78dd541eb0d1b82ff3c9de0"

# DB Connection (change details to match your setup)
db = pymysql.connect(
    host="localhost",
    user="root",
    password="Naduka1024#",
    database="university_chatbot"  # Use your actual database name
)
cursor = db.cursor()

# Route to handle chatbot interactions
@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        bot_response = get_bot_response(user_input)
        return jsonify({"response": bot_response})
    return render_template('chatbot.html')

# Route for logging out
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check form submission and print it
        print(request.form)  # To verify if form data is coming correctly
        
        username = request.form.get('username')  # Changed to .get() for safety
        password = request.form.get('password')
        
        if not username or not password:
            flash("Username and Password are required!", "danger")
            return redirect(url_for('login'))

        # Hash the password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, hashed_password))
        user = cursor.fetchone()
        
        if user:
            session['user_id'] = user[0]  # Store user ID in session
            flash("Login successful!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for('login'))
    
    return render_template('login.html')

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        
        if not username or not password or not email:
            flash("All fields are required!", "danger")
            return redirect(url_for('register'))
        
        # Hash the password before storing
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash("Username already taken. Please choose a different one.", "warning")
            return redirect(url_for('register'))
        
        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", 
                       (username, hashed_password, email))
        db.commit()
        
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Forgot password route
@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    return render_template('forgot_password.html')

# Suggestion route
@app.route('/suggestion', methods=['GET', 'POST'])
def suggestion():
    return render_template('suggestion.html')

if __name__ == '__main__':
    app.run(debug=True)
