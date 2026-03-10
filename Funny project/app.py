from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    result = ""

    if request.method == "POST":

        day = request.form["day"].lower()

        time.sleep(1)

        if day == "monday":
            result = "🎉 Next day is Tuesday"
        elif day == "tuesday":
            result = "🎉 Next day is Wednesday"
        elif day == "wednesday":
            result = "🎉 Next day is Thursday"
        elif day == "thursday":
            result = "🎉 Next day is Friday"
        elif day == "friday":
            result = "🎉 Next day is Saturday 😎 Weekend coming!"
        elif day == "saturday":
            result = "🎉 Next day is Sunday 🥳 Party time!"
        elif day == "sunday":
            result = "💀 Next day is Monday... back to work 😂"
        else:
            result = "❌ Error 404: Day not found in this universe 🌍"

    return render_template("index.html", result=result)

app.run(debug=True)