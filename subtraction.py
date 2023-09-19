from flask import Flask, request, render_template

app = Flask(__name__)

# Function to perform subtraction
def subtract(x, y):
    return x - y

@app.route('/subtract', methods=['GET', 'POST'])
def calculator_subtract():
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = subtract(num1, num2)
            return render_template('result.html', result=result, operation="Subtraction")
        except ValueError:
            error_message = "Invalid input. Please enter valid numbers."
            return render_template('calculator.html', error_message=error_message, operation="Subtraction")
    return render_template('calculator.html', operation="Subtraction")

@app.route('/')
def hi():
    return 'Welcome to Calculator!'

if __name__ == '__main__':
    app.run(debug=True)
