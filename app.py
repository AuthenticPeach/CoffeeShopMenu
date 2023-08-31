from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def back_to_main_menu():
    return '<a href="/">Return to main menu</a>'

@app.route("/cold_drink")
def cold_drink():
    return "You selected a cold drink. " + back_to_main_menu()

@app.route("/refreshing_drink")
def refreshing_drink():
    return "You selected a refreshing drink. " + back_to_main_menu()

@app.route("/hot_drink")
def hot_drink():
    return "You selected a hot drink. " + back_to_main_menu()

@app.route("/coffee")
def coffee():
    return "You selected coffee. " + back_to_main_menu()

@app.route("/view_menu")
def view_menu():
    # You can replace this with code to display an image or any other menu representation you prefer
    return "Viewing the full menu... " + back_to_main_menu()


if __name__ == "__main__":
    app.run(debug=True)
