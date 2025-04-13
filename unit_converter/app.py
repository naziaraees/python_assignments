from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion functions
def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kg_to_pounds(kg):
    return kg * 2.20462

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    conversion_type = None
    value = None

    if request.method == "POST":
        conversion_type = request.form["conversion_type"]
        value = float(request.form["value"])

        if conversion_type == "km_to_miles":
            result = f"{value} kilometers = {km_to_miles(value):.2f} miles"
        elif conversion_type == "celsius_to_fahrenheit":
            result = f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F"
        elif conversion_type == "kg_to_pounds":
            result = f"{value} kilograms = {kg_to_pounds(value):.2f} pounds"

    return render_template("index.html", result=result, conversion_type=conversion_type, value=value)

if __name__ == "__main__":
    app.run(debug=True)