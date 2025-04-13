from flask import Flask, render_template, request, redirect, jsonify
import json

app = Flask(__name__)

# Load or initialize library data
try:
    with open("library_data.json", "r") as f:
        library_data = json.load(f)
except FileNotFoundError:
    library_data = []

# Save library data to JSON file
def save_library_data():
    with open("library_data.json", "w") as f:
        json.dump(library_data, f, indent=4)

@app.route("/")
def home():
    return render_template("index.html", library_data=library_data)

@app.route("/add", methods=["POST"])
def add_book():
    book_name = request.form["book_name"]
    author = request.form["author"]
    publish_year = request.form["publish_year"]
    total_pages = int(request.form["total_pages"])
    read_pages = int(request.form["read_pages"])

    # Calculate reading percentage
    percentage_read = (read_pages / total_pages) * 100

    # Add book details to library
    library_data.append({
        "book_name": book_name,
        "author": author,
        "publish_year": publish_year,
        "total_pages": total_pages,
        "read_pages": read_pages,
        "percentage_read": percentage_read
    })
    save_library_data()
    return redirect("/")

@app.route("/update", methods=["POST"])
def update_book():
    index = int(request.form["index"])
    read_pages = int(request.form["read_pages"])

    # Update reading progress
    library_data[index]["read_pages"] = read_pages
    library_data[index]["percentage_read"] = (read_pages / library_data[index]["total_pages"]) * 100
    save_library_data()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)